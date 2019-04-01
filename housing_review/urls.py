from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
#from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('review/', views.ReviewView.as_view(), name='review'),
    path('manage/', views.Manage.as_view(), name='manage'),
    path('', views.allReviews.as_view(), name='all-review'),
    #path('map/', views.map, name='map'), Now in all-review
    url(r'^login/$', views.Home, name='login'),
    url(r'^profile/$', views.update_profile, name='profile'),
    url(r'^account/logout/$', views.Logout, name='logout'),
]
