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
from author import views

urlpatterns = [
    path('authors/', views.authors,  name = 'base_author'),
    path('author_info/<int:id>/', views.add_author_info,  name = 'add_author_info'),
    path('delete_author/<int:id>/', views.delete_author,  name = 'delete_author'),
    path('authors_book/<int:id>/', views.author_books,  name = 'author_books'),

]


