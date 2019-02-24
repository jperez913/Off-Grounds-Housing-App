from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Review(models.Model):
  neighborhoods = (
    ('Wertland', 'Wertland'),
    ('Rugby', 'Rugby'),
    ('14th Street', '14th Street'),
    ('JPA', 'JPA',),
    ('Main Street', 'Main Street')
)
  text = models.CharField(max_length=10000, blank=False)
  pub_date = models.DateTimeField('date published', blank=False)
  reviewer = models.ForeignKey('User', on_delete=models.PROTECT, blank=False)
  neighborhood = models.CharField(max_length=3, choices=neighborhoods)
  address = models.CharField(max_length=100, blank=False)
  stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], blank=False)
  price = models.FloatField(blank=True)
  parking = models.BooleanField(blank=True)
  bedrooms = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], blank=True)
  bathrooms = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], blank=True)
  pets = models.BooleanField(blank=True)
  pool = models.BooleanField(blank=True)
  distance_to_newcomb = models.FloatField(blank=True) #we generate this
  utilities_cost = models.FloatField(blank=True)
  utilities_provided = models.CharField(max_length=500, blank=True)
  amenities_provided = models.CharField(max_length=500, blank=True)



class User(models.Model):
  first_name = models.CharField(max_length=30, blank=False)
  last_name = models.CharField(max_length=30, blank=False)
  reviews = models.ManyToManyField(Review)