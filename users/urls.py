from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('send/data', views.search_product_view, name="send-data"), 
    path('goodbye/', views.goodbye, name="goodbye"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register")
]