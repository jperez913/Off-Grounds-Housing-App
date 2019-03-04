from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('map/', views.map, name='map')
]
