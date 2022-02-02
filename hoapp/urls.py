"""hotel URL Configuration

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
from.import views
from django.urls import path,include

urlpatterns = [
    path('',views.first),
    path('contact/',views.cont),
    path('about/',views.about),
    path('room/',views.room),
    path('service/',views.service),
    path('shortcodes/',views.short),
    path('login/',views.login),
    path('registration/',views.registration),
    path('admin_a/',views.admin_a),
    path('cust/',views.cust),
    path('add_room/',views.add_room),
    path('roomdetails/',views.details),
    path('single/',views.single),
    path('upd/',views.upd),
    path('update/',views.update),
    path('remove/',views.remove),
    path('book/',views.book),
    path('out/',views.out),
    path('b_room/',views.b_room),
    path('status/',views.status),
    path('room1/',views.room1),
    path('c_home/',views.home),
    path('c_about/',views.c_about),
    path('c_service/',views.c_service),
    path('c_contact/',views.c_contact),
    path('c_book/',views.c_book),
    path('approve/',views.approve),
    path('remove/',views.remove),
    path('bill/',views.bill),
    path('payment/',views.payment),
    path('c_pay/',views.c_pay),
    path('pro/',views.pro),

    ]
   
