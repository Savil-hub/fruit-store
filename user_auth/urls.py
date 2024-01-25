from django.urls import path, include
from . import views



app_name = 'user_auth'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.registration_view, name='register'),
    path('show_user/', views.show_user, name='show_user'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
]