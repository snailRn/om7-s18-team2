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
from book import views

urlpatterns = [
    path('get-by-id/<int:id>/', views.book_by_id,  name = 'book-by-id'),
    path('all/<str:sort>/', views.all_book,  name = 'book_sort'),
    path('unordered/', views.unodered_books,  name = 'book_unodered'),
    path('filter/', views.filter_book, name='filter_book'),
    
]