from django.shortcuts import render, HttpResponse
from .models import MenuItem

# Create your views here.
def home(request):
  return render(request, "home.html")

def menu(request):
  items = MenuItem.objects.all()
  return render(request, "menu.html", {"items": items})