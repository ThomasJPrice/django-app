from django.shortcuts import render, redirect
from .models import MenuItem, Order
import json
from django.http import JsonResponse

# Create your views here.
def home(request):
  return redirect('/order')

def order(request):
  categories = MenuItem.CATEGORY_CHOICES  # Get the category choices defined in your model
  items_by_category = {category[0]: MenuItem.objects.filter(category=category[0]) for category in categories}
  
  return render(request, "order.html", {
      "items_by_category": items_by_category,
      "categories": categories
  })

def fulfilment(request):
  orders = Order.objects.all()
  return render(request, "fulfilment.html", {"orders": orders})

def progress(request):
  orders = Order.objects.all()
  return render(request, "progress.html", {"orders": orders})


# API routes

# checkout
def checkout(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    cart = data.get('cart', [])
    customer_name = data.get('customer_name', 'Anonymous')