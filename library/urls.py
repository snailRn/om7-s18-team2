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
from library import views
from authentication import views as userviews
from order import views as orderviews
from author import views as authorviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', userviews.UserViewSet)
router.register(r'order', orderviews.OrderViewSet)
router.register(r'author', authorviews.AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),
    path('authentication/', include('authentication.urls')),
    path('author/', include('author.urls')),
    path('options/',views.options, name='options'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/v1/', include(router.urls)),


]
