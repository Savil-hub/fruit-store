"""
URL configuration for fruitselling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from  django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from user_auth.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/', include('fruits.urls')),
    path('contact/', include('contact.urls')),
    path('buy/', include('buy.urls')),
    path('home/', include('home.urls')),
    path('user_auth/', include("user_auth.urls")),
    path('', user_login, name='root_login'),  # Ensure this view is correctly defined
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




