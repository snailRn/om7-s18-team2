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

from django.urls import path
from authentication import views

# Routers provide an easy way of automatically determining the URL conf.
 
urlpatterns = [
    path('all_users/', views.users,  name = 'all_users'),  
    path('user_info/<int:id>/', views.add_user_info,  name = 'add_user_info'),
    path('delete_user/<int:id>/', views.delete_user,  name = 'delete_user'),
    path('add-information/', views.add_info,  name = 'add_info'),
      
]