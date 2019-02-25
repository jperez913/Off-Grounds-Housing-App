from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're ready to review housing options now.")

def home(request):
  return render(request, 'home.html')