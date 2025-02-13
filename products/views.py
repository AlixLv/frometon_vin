from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from products.models import Cheese, Wine, Pairing 
from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
import requests



class CheesesView(TemplateView):
    template_name = "all-cheeses.html"
    
 
class WinesView(TemplateView):
    template_name = "all-wines.html"  
    

class RawCowCheeses(TemplateView):
    template_name = "raw-cow-cheeses.html"


class PasteurisedCowCheeses(TemplateView):
    template_name = "pasteurised-cow-cheeses.html" 


class RawSheepCheeses(TemplateView):
    template_name = "raw-sheep-cheeses.html"             


class RawGoatCheeses(TemplateView):
    template_name = "raw-goat-cheeses.html"


class RedWines(TemplateView):
        template_name = "red-wines.html"    


class WhiteWines(TemplateView):
    template_name = "white-wines.html"


class RoseWines(TemplateView):
    template_name = "rose-wines.html"    


def fetch_cheeses(request):
    base_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/fromagescsv-fromagescsv/records?"

    records_number = "5"

    complete_url = base_url + "?limit=0" + records_number

    response = requests.get(complete_url)
    data = response.json()
    print("🌈 ", data)
    return JsonResponse(data)


def detail_cheese_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = get_object_or_404(Cheese.detail_cheese.filter(id=id_object))
        print("🍿 ", product_object)
        
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./cheese-product.html", context=context)



def detail_wine_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = get_object_or_404(Wine.detail_wine.filter(id=id_object))

    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./wine-product.html", context=context)    



def get_pairing(request):
    objects_pairing_list = []
    product_type = None
    
    # Récupère la valeur du paramètre 'product_name' du QueryDict envoyé via form
    name_product = request.GET.get('product_name')
    print("🐙", name_product, type(name_product))
    
    if name_product is not None:
        try:
            searched_product = get_object_or_404(Cheese, name = name_product)  
            print("🐢 ", searched_product, type(searched_product))
            id_product = searched_product.id
            print("🪲", id_product, type(id_product))   
            product_type = "cheese"
            print("🥑 ", product_type)
            
            #pairings_list = Pairing.objects.filter(cheese=id_product)
            pairings_list = get_list_or_404(Pairing.cheese_objects.get_list_cheese_pairings(cheese=id_product))
            print("🐍 ", pairings_list)

        except Http404:
            try:
                searched_product = get_object_or_404(Wine, name=name_product)
                print("🐢 ", searched_product, type(searched_product))  
                id_product = searched_product.id
                print("🦞", id_product, type(id_product))
                product_type = "wine"
                print("🥑 ", product_type)
                
                #pairings_list = Pairing.objects.filter(wine=id_product)
                pairings_list = get_list_or_404(Pairing.wine_objects.get_list_wine_pairings(wine=id_product))
                print("🐍 ", pairings_list)

            except:
                    return redirect('not-found')
        
        pairings = {}
    
        for pairing in pairings_list:
            print(pairing.id)   
            id = pairing.id
            if id not in pairings:
                pairings[id] = []
            pairings[id].append(pairing)
        print("🦁 ", pairings)               
                       
                
        context = {
            "searched_product": searched_product,
            "product_type": product_type,
            "pairings": pairings
        }

        return render(request, './pairing.html', context=context)
    
    else:
        return redirect('not-found')
 
 
 
def data_not_found(request):
    
    return render(request, './not-found.html')