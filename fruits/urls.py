from django.urls import path, include
from . import views
from .views import product_list

urlpatterns = [
    path('', views.online_store, name="online_store"),
    path('fruits/', product_list, name='product_list')
]