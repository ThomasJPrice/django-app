from django.contrib import admin
from .models import MenuItem, Order

# Register your models here.
admin.site.register([MenuItem, Order])