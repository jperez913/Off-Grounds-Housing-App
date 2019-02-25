from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from . import views
from .views import home

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')), 
    url(r'^$', home, name='home'),
]
