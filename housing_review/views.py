import googlemaps  #for geocoding
import json

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Review, NEIGHBORHOODS, UTILITIES, AMENITIES

from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import transaction
from .models import Profile
from .forms import UserForm, ProfileForm
from django.utils.decorators import method_decorator


@login_required
def Home(request):
    return render(request, 'home/home.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


''' DEPRECATED
def index(request):
  return HttpResponse("Hello, world. You're ready to review housing options now.")

def map(request):
  return render(request, "housing_review/map.html", {'lat':38.0314867, 'lng':-78.5090342}) #38.0314867,-78.5090342
'''


@method_decorator(login_required, name='dispatch')
class ReviewView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "housing_review/review.html", {
                'neighborhoods': NEIGHBORHOODS,
                'utilities': UTILITIES,
                'amenities': AMENITIES, 
                'address_error':False
            })

    def post(self, request, *args, **kwargs):
        text = request.POST['text']
        pub_date = timezone.now()
        address = request.POST['address']

        #gmaps api gecoding
        try:
            gmaps = googlemaps.Client(
                key='AIzaSyBLDfHtyt6C7NqimxtXZ8imfqHinj_dVNY')
            geocode_result = gmaps.geocode(address)
            location = json.dumps(geocode_result[0]['geometry']['location'])
        except:
            return render(
            request, "housing_review/review.html", {
                'neighborhoods': NEIGHBORHOODS,
                'utilities': UTILITIES,
                'amenities': AMENITIES, 
                'address_error': True
            })
        # print("location stored in model " + location)
        try:
          stars = int(request.POST['stars'])
          if stars < 1 or stars > 5:
            raise Exception
          price = float(request.POST['price'])
          if price < 0 or price > 2500:
            raise Exception
          utilities_cost = float(request.POST['utilities_cost'])
          if utilities_cost < 0 or utilities_cost > 2500:
            raise Exception
          bathrooms = int(request.POST['bathrooms'])
          if bathrooms < 0 or bathrooms > 6:
            raise Exception
          bedrooms = int(request.POST['bedrooms'])
          if bedrooms < 0  or bedrooms > 10:
            raise Exception
        except:
            return render(
            request, "housing_review/review.html", {
                'neighborhoods': NEIGHBORHOODS,
                'utilities': UTILITIES,
                'amenities': AMENITIES, 
                'address_error': False
            })

        hood_arr = []
        util_arr = []
        amen_arr = []
        for hood in NEIGHBORHOODS:
            x = request.POST.get(hood, "")
            if x != "":
                hood_arr.append(x)
        for util in UTILITIES:
            x = request.POST.get(util, "")
            if x != "":
                util_arr.append(x)
        for amen in AMENITIES:
            x = request.POST.get(amen, "")
            if x != "":
                amen_arr.append(x)
        user = User.objects.get(email=request.user.email)
        distance_to_newcomb = 1.00  #Get This somehow

        neighborhood = ", ".join(hood_arr)
        utilities = ", ".join(util_arr)
        amenities = ", ".join(amen_arr)

        r = Review(
            text=text,
            pub_date=pub_date,
            neighborhood=neighborhood,
            address=address,
            stars=stars,
            price=price,
            utilities=utilities,
            amenities=amenities,
            utilities_cost=utilities_cost,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            reviewer=user.pk,
            distance_to_newcomb=distance_to_newcomb,
            location=location)
        r.save()

        return HttpResponseRedirect(reverse('all-review'))


@method_decorator(login_required, name='dispatch')
class Manage(generic.View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.email)
        Reviews = Review.objects.filter(reviewer=user.pk)
        return render(
            request, "housing_review/manage.html", {
                'Reviews': Reviews,
                'neighborhoods': NEIGHBORHOODS,
                'utilities': UTILITIES,
                'amenities': AMENITIES
            })

    def post(self, request, *args, **kwargs):
        submit_type = request.POST['submit_type']
        if submit_type == "update":
            print(request.POST)
            pub_date = timezone.now()
            #address = request.POST['address']
            try:
              text = request.POST['text']
              if(text == ""):
                raise Exception;
              stars = int(request.POST['stars'])
              if stars < 1 or stars > 5:
                raise Exception
              price = float(request.POST['price'])
              if price < 0 or price > 2500:
                raise Exception
              utilities_cost = float(request.POST['utilities_cost'])
              if utilities_cost < 0 or utilities_cost > 2500:
                raise Exception
              bathrooms = int(request.POST['bathrooms'])
              if bathrooms < 0 or bathrooms > 6:
                raise Exception
              bedrooms = int(request.POST['bedrooms'])
              if bedrooms < 0  or bedrooms > 10:
                raise Exception
            except:
              return HttpResponseRedirect(reverse('manage'))
            hood_arr = []
            util_arr = []
            amen_arr = []
            for hood in NEIGHBORHOODS:
                x = request.POST.get(hood, "")
                if x != "":
                    hood_arr.append(x)
            for util in UTILITIES:
                x = request.POST.get(util, "")
                if x != "":
                    util_arr.append(x)
            for amen in AMENITIES:
                x = request.POST.get(amen, "")
                if x != "":
                    amen_arr.append(x)
            print(hood_arr, util_arr, amen_arr)
            user = User.objects.get(email=request.user.email)
            distance_to_newcomb = 1.00  #Get This somehow
            neighborhood = ", ".join(hood_arr)
            utilities = ", ".join(util_arr)
            amenities = ", ".join(amen_arr)

            pk = request.POST['pk']
            review = Review.objects.get(pk=pk)
            review.text = text
            review.pub_date = pub_date
            review.neighborhood = neighborhood
            #review.address = address
            review.stars = stars
            review.price = price
            review.utilities = utilities
            review.utilities_cost = utilities_cost
            review.amenities = amenities
            review.utilities = utilities
            review.bathrooms = bathrooms
            review.bedrooms = bedrooms
            review.reviewer = user.pk
            review.distance_to_newcomb = distance_to_newcomb
            if(review.reviewer == user.pk):
              review.save()

        elif submit_type == "delete":
            pk = request.POST['pk']
            review = Review.objects.get(pk=pk)
            user = User.objects.get(email=request.user.email)
            if(review.reviewer == user.pk):
              review.delete()

        return HttpResponseRedirect(reverse('manage'))


@method_decorator(login_required, name='dispatch')
class allReviews(generic.View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        if(len(request.GET.get('reset_type', [])) > 0):
          return HttpResponseRedirect(reverse('all-review'))
        try:
          stars = int(request.GET.get('stars', '1'))
          min_price = int(request.GET.get('min_price', '0'))
          max_price = int(request.GET.get('max_price', '2500'))
          #max_bed = request.GET.get('max_bed', 10)
          min_bed = int(request.GET.get('min_bed', '1'))
          #max_bath = request.GET.get('max_bath', 10)
          min_bath = int(request.GET.get('min_bath', '1'))
        except:
          return HttpResponseRedirect(reverse('all-review'))
        #address = request.GET.get('address', '')
        location = request.GET.get('location', '')
        # print("printing location!!")
        # print(request.GET.get('location', ''))
        if stars < 1 or stars > 5 or min_bed < 1 or min_bed > 10 or min_bath < 1 or min_bath > 6 or min_price < 0 or max_price < 0 or max_price > 2500 or min_price >2500:
          return HttpResponseRedirect(reverse('all-review'))

        hood_arr = []
        util_arr = []
        amen_arr = []
        for hood in NEIGHBORHOODS:
            x = request.GET.get(hood, "")
            if x != "":
                hood_arr.append(x)
        for util in UTILITIES:
            x = request.GET.get(util, "")
            if x != "":
                util_arr.append(x)
        for amen in AMENITIES:
            x = request.GET.get(amen, "")
            if x != "":
                amen_arr.append(x)
        try:
          objects = Review.objects.all().filter(stars__gte=stars)
          objects = objects.filter(price__gte=min_price)
          objects = objects.filter(price__lte=max_price)
          objects = objects.filter(bedrooms__gte=min_bed)
          #objects = objects.filter(bedrooms__lte=max_bed)
          objects = objects.filter(bathrooms__gte=min_bath)
          #objects = objects.filter(bathrooms__lte=max_bath)
          for hood in hood_arr:
              objects = objects.filter(neighborhood__contains=hood)
          for amen in amen_arr:
              objects = objects.filter(amenities__contains=amen)
          for util in util_arr:
              objects = objects.filter(utilities__contains=util)

          if location != '':
              objects = objects.filter(location=location)

          objects = objects.order_by('-pub_date')
        except:
          return HttpResponseRedirect(reverse('all-review'))
        print(stars)
        return render(
            request, "housing_review/all_reviews.html", {
                'location' : location,
                'stars': stars,
                'min_price': min_price,
                'max_price': max_price,
                'min_bed': min_bed,
                'min_bath': min_bath,
                'hood_arr': hood_arr,
                'util_arr': util_arr,
                'amen_arr': amen_arr,
                'neighborhoods': NEIGHBORHOODS,
                'utilities': UTILITIES,
                'amenities': AMENITIES,
                'object_list': objects,
                'five_arr': [0,1,2,3,4]
            })
