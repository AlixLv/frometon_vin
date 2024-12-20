from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('home/', views.home, name="home"), 
    path('goodbye/', views.goodbye, name="goodbye"),
    path('logout', views.logout_view, name="logout")
]