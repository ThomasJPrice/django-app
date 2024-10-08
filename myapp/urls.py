from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("", views.home, name='home'),
  
  path('order/', views.order, name='Order'),
  path('fulfilment/', views.fulfilment, name='Fulfilment'),
  path('progress/', views.progress, name='Progress'),
  
  # api routes
  path('checkout/', views.checkout, name='checkout'),
  path('get-orders/', views.getOrders, name='get-orders'),
  path('get-all-items/', views.getAllItems, name='get-all-items'),
  path('complete-order/', views.completeOrder, name='complete-order'),
  
  path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)