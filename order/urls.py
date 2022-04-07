"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from order import views

urlpatterns = [
    path('not_on_time', views.not_on_time,  name = 'not-on-time'),
    path('sorting/<str:address>', views.selection_date,  name = 'order-by-date'),
    path('user_books/<int:id>', views.user_books,  name = 'user_books'),
    path('', views.all_orders,  name = 'all_orders'),
    path('add-order/', views.add_order_info,  name = 'add_order_info'),
    path('change-order/<int:id>', views.add_order_info,  name = 'change_order_info'),
    path('close-order/<int:id>', views.close_order,  name = 'close_order'),
    
    
    
]