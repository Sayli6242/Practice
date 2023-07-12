from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about',views.about, name = 'blog-about'),
    # # path('services',views.services,name = 'blog-services'),
    # path('contacts', views.contacts, name='blog-ontacts'),
]
