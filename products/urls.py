from django.urls import path
from . import views 
from products.views import CheesesView, WinesView

urlpatterns = [
  path('all-cheeses/', CheesesView.as_view(), name="all-cheeses"),
  path('all-wines/', WinesView.as_view(), name="all-wines"),
  path('cheese-product/<int:id>/', views.detail_cheese_product_view, name="cheese-product"),
  path('wine-product/<int:id>/', views.detail_wine_product_view, name="wine-product"),
  path('pairing/', views.get_pairing, name="pairing"), 
  path('not-found/', views.data_not_found, name="not-found"),
]