from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ReviewCreate.as_view(), name='create'),
    path('createpost/', views.createpost, name='createpost'),
]
