from django.urls import path
from . import views 

urlpatterns = [
  path('all-cheeses/', views.get_cheeses, name="all-cheeses"),
  path('all-wines/', views.get_wines, name="all-wines"),
  path('cheese-product/<int:id>/', views.detail_cheese_product_view, name="cheese-product"),
  path('wine-product/<int:id>/', views.detail_wine_product_view, name="wine-product"),
  path('send/data', views.search_product_view, name="send-data"), 
  path('not-found', views.data_not_found, name="not-found"),
]