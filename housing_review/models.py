from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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



class User(models.Model):
  first_name = models.CharField(max_length=30, blank=False)
  last_name = models.CharField(max_length=30, blank=False)
  email = models.CharField(max_length=30, blank=False, null=True)
  reviews = models.ManyToManyField(Review)
