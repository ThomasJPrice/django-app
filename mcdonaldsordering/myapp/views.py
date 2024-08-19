from django.shortcuts import render, redirect
from .models import MenuItem, Order

# Create your views here.
def home(request):
  return redirect('/order')

def order(request):
  items = MenuItem.objects.all()
  return render(request, "order.html", {"items": items})

def fulfilment(request):
  orders = Order.objects.all()
  return render(request, "fulfilment.html", {"orders": orders})

def progress(request):
  orders = Order.objects.all()
  return render(request, "progress.html", {"orders": orders})