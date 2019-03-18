from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

NEIGHBORHOODS = ['Wertland','Rugby','14th Street','JPA','Main Street']
UTILITIES = ['Electricity','Water','Internet']
AMENITIES = ['Parking','Pets','Pool']

# Create your models here.
class Review(models.Model):
  text = models.CharField(max_length=10000)
  pub_date = models.DateTimeField('date published')
  address = models.CharField(max_length=100)
  stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
  reviewer = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
  neighborhood = models.CharField(max_length=10000, null=True)
  price = models.FloatField(null=True)
  bedrooms = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=True)
  bathrooms = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=True)
  distance_to_newcomb = models.FloatField(null=True) #we generate this
  utilities_cost = models.FloatField(null=True)
  utilities = models.CharField(max_length=10000, null=True)
  amenities = models.CharField(max_length=10000, null=True)
  location = models.CharField(max_length=1000, null=True)



class User(models.Model):
  first_name = models.CharField(max_length=30, blank=False)
  last_name = models.CharField(max_length=30, blank=False)
  email = models.CharField(max_length=30, blank=False, null=True)
  reviews = models.ManyToManyField(Review)
