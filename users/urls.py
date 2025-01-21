from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('goodbye/', views.goodbye, name="goodbye"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),
    path('profile/<int:id>/', views.get_profile, name="profile"),
    path('edit-profile/<int:id>', views.update_profile, name="edit-profile"),
    path('edit-password/<int:id>', views.update_password, name="edit-password")
]