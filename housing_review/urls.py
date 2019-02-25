from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('all-reviews/', views.allReviews.as_view(), name='all-review'),
]
