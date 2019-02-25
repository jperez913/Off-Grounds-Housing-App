from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
  list_display = ('address', 'text', 'pub_date', 'stars', 'reviewer', 'neighborhood', 'price', 'bedrooms', 'bathrooms', 'distance_to_newcomb', 'utilities_cost', 'utilities', 'amenities')
admin.site.register(Review, ReviewAdmin)