from django.db import models

# Create your models here.

class User(model.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class Review(model.Model):
    UTILITIES = [('light', 'light bill'), ('water', 'water bill'), ('electric', 'electricity bill'), ('gas', 'gas bill'), ('internet', 'internet bill')]
    AMENITIES = [('furniture', 'furniture'), ('refrigerator', 'refrigerator'), ('bed', 'bed frame')]
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    about_text = models.TextField()
    price = models.CharField(max_length=8)
    parking = models.BooleanField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    pets = models.BooleanField()
    distance_to_central_grounds = models.DecimalField()
    included_utilities = models.CharField(choices=UTILITIES, max_length=5, blank=True)
    included_amenities = models.CharField(choices=AMENITIES, max_length=3, blank=True)
    pool = models.BooleanField()