from django.db import models

# Custom fields

# Create your models here.

class MenuItem(models.Model):
    # Define the choices for the category field
    MAIN = 'Main'
    SIDE = 'Side'
    DRINK = 'Drink'

    CATEGORY_CHOICES = [
        (MAIN, 'Main'),
        (SIDE, 'Side'),
        (DRINK, 'Drink'),
    ]

    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='menu_images/')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=MAIN,
    )
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Order(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    customer_name = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    
    items = models.CharField(max_length=200)
    
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} - {self.status}"
