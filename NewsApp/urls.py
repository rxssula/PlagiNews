from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('sport/', views.sport, name="sport"),
    path('edu/', views.edu, name="edu"),
]