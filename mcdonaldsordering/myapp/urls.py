from django.urls import path, include
from . import views

urlpatterns = [
  path("", views.home, name='home'),
  
  path('order/', views.order, name='Order'),
  path('fulfilment/', views.fulfilment, name='Fulfilment'),
  path('progress/', views.progress, name='Progress'),
  
  path("__reload__/", include("django_browser_reload.urls")),
]