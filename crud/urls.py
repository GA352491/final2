"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from sales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('stock/', views.stock, name='stock'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('order_create', views.create_invoice, name='createinvoice'),
    path('order_update/<str:pk>', views.update_invoice, name='updateinvoice'),
    path('order_delete/<str:pk>', views.delete_invoice, name='deleteinvoice'),
    path('customer_list/', views.customer_list, name='customerlist'),
    path('dataset/', views.dataset, name='dataset'),
    path('placerder/<str:pk>', views.place_order, name='placeorder'),
    path('createcustomer/', views.create_cust, name='create_cus'),
    path('createstock/', views.stock_create, name='create_stock'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('updatecustomer/<str:pk>', views.update_customer, name='updatecustomer'),
    path('deleteecustomer/<str:pk>', views.delete_customer, name='deletecustomer'),
    path('whatsapp/<str:pk>', views.whatsapp, name='whatsapp'),
    path('product/<str:pk>', views.pro_list, name='product'),

]
