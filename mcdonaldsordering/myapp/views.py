from django.shortcuts import render, redirect
from .models import MenuItem, Order
import json
from django.http import JsonResponse

# Create your views here.


def home(request):
    return redirect('/order')


def order(request):
    # Get the category choices defined in your model
    categories = MenuItem.CATEGORY_CHOICES
    items_by_category = {category[0]: MenuItem.objects.filter(
        category=category[0]) for category in categories}

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

        orderItems = []
        for item in cart:
            orderItems.append(item['id'])

        order = Order.objects.create(
            customer_name=customer_name, items=str(orderItems))

        response_data = {
            'message': 'Order placed successfully',
            'order_id': order.id
        }

        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def getOrders(request):
    orders = Order.objects.filter(status=Order.IN_PROGRESS)
    
    orders_data = [{
        'id': order.id
    } for order in orders]
    
    
    return JsonResponse({'orders': orders_data})