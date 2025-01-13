from django.urls import path
from . import views 

urlpatterns = [
  path('all-cheeses/', views.get_cheeses, name="all-cheeses"),
  path('all-wines/', views.get_wines, name="all-wines"),
  path('product/<int:id>/', views.detail_product_view, name="product"),
  path('send/data', views.search_product_view, name="send-data"), 
]