from django.urls import path
from . import views 
from products.views import CheesesView, WinesView, RawCowCheeses, PasteurisedCowCheeses
from products.views import RawSheepCheeses, RawGoatCheeses, RedWines, WhiteWines, RoseWines

urlpatterns = [
  path('all-cheeses/', CheesesView.as_view(), name="all-cheeses"),
  path('all-wines/', WinesView.as_view(), name="all-wines"),
  path('raw-cow-cheeses/', RawCowCheeses.as_view(), name="raw-cow-cheeses"),
  path('pasteurised-cow-cheeses/', PasteurisedCowCheeses.as_view(), name="pasteurised-cow-cheeses"),
  path('raw-sheep-cheeses/', RawSheepCheeses.as_view(), name="raw-sheep-cheeses"),
  path('raw-goat-cheeses/', RawGoatCheeses.as_view(), name="raw-goat-cheeses"),
  path('red-wines', RedWines.as_view(), name='red-wines'),
  path('white-wines', WhiteWines.as_view(), name='white-wines'),
  path('rose-wines', RoseWines.as_view(), name='rose-wines'),
  path('cheese-product/<int:id>/', views.detail_cheese_product_view, name="cheese-product"),
  path('wine-product/<int:id>/', views.detail_wine_product_view, name="wine-product"),
  path('pairing/', views.get_pairing, name="pairing"), 
  path('not-found/', views.data_not_found, name="not-found"),
]


#blanc
#rouge
#rosé