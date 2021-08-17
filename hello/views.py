from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,"hello/index.html")

def noman(request):
  return HttpResponse("Hello, Noman!")

def greet(request,name):
  return HttpResponse(f"Hello, {name}")
