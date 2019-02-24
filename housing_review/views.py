from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Review, User

def index(request):
  return HttpResponse("Hello, world. You're ready to review housing options now.")

class ReviewCreate(generic.CreateView):
  model = Review
  fields = ('text', 'reviewer', 'neighborhood', 'address', 'stars', 'price', 'parking', 'bedrooms', 'bathrooms', 'pets', 'pool', 'distance_to_newcomb', 'utilities_cost', 'utilities_provided', 'amenities_provided')

def createpost(request):
  text = request.POST.get("text")
  s = Review(text=text)
  s.save()