import googlemaps #for geocoding
import json

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Review, NEIGHBORHOODS, UTILITIES, AMENITIES

def index(request):
  return HttpResponse("Hello, world. You're ready to review housing options now.")

def map(request):
  return render(request, "housing_review/map.html", {'lat':38.0314867, 'lng':-78.5090342}) #38.0314867,-78.5090342

class ReviewView(generic.View):
  def get(self, request, *args, **kwargs):
    return render(request, "housing_review/review_form.html", {'neighborhoods':NEIGHBORHOODS, 'utilities':UTILITIES, 'amenities':AMENITIES})

  def post(self, request, *args, **kwargs):
    text = request.POST['text']
    pub_date = timezone.now()
    address = request.POST['address']

    #gmaps api gecoding
    gmaps = googlemaps.Client(key='AIzaSyBLDfHtyt6C7NqimxtXZ8imfqHinj_dVNY')
    geocode_result = gmaps.geocode(address)
    location = json.dumps( geocode_result[0]['geometry']['location'] )
    print("wtf")
    print(location)

    stars = int(request.POST['stars'])
    price = float(request.POST['price'])
    utilities_cost = float(request.POST['utilities_cost'])
    bathrooms = int(request.POST['bathrooms'])
    bedrooms = int(request.POST['bedrooms'])

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

    reviewer = 1 #get primary key
    distance_to_newcomb = 1.00 #Get This somehow

    neighborhood = ",".join(hood_arr)
    utilities = ",".join(util_arr)
    amenities = ",".join(amen_arr)

    #note no reviewer in this. Need to add this in later
    r = Review(text=text, pub_date=pub_date, neighborhood=neighborhood, address=address, stars=stars, price=price, utilities=utilities, amenities=amenities,
     utilities_cost=utilities_cost, bathrooms=bathrooms, bedrooms=bedrooms, distance_to_newcomb=distance_to_newcomb, location=location)
    r.save()

    return HttpResponseRedirect(reverse('index'))

class allReviews(ListView):
  model = Review
  template_name = 'housing_review/all_reviews.html'
  def get_queryset(self):
    return Review.objects.all()
