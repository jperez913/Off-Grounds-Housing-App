from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Profile(models.Model):
    user = models.OneToOneField(
        User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
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


NEIGHBORHOODS = ['Wertland', '14th St', 'JPA']
UTILITIES = ['Electricity', 'Water', 'Internet']
AMENITIES = ['Parking', 'Pets', 'Pool']


def belongsToAUser(value):
    try:
        user = User.objects.get(pk=value)
    except user.DoesNotExist:
        raise ValidationError(
            _('%(value)s does not belong to a user'),
            params={'value': value},
        )


def lastBelongsToAReview(value):
    try:
        s = " ".split(value)[-1]  #get last
        review = Review.objects.get(pk=s)
    except review.DoesNotExist:
        raise ValidationError(
            _('%(value)s does not belong to a review'),
            params={'value': value},
        )


# Create your models here.
class Review(models.Model):
    text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=100)
    stars = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    reviewer = models.IntegerField(validators=[belongsToAUser], default=1)
    neighborhood = models.CharField(max_length=10000, null=True)
    price = models.FloatField(null=True)
    bedrooms = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(100)], null=True)
    bathrooms = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(100)], null=True)
    distance_to_newcomb = models.FloatField(null=True)  #we generate this
    utilities_cost = models.FloatField(null=True)
    utilities = models.CharField(max_length=10000, null=True)
    amenities = models.CharField(max_length=10000, null=True)
    location = models.CharField(max_length=1000, null=True)



class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False, default="legacy")
