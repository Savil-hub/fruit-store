from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='buy'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]