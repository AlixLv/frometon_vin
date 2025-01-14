from django.shortcuts import render, redirect
from products.models import Cheese, Wine, Pairing 


def get_cheeses(request):
    cheeses = Cheese.objects.all()
    return render(request, './all-cheeses.html', {'cheeses': cheeses})


def get_wines(request):
    wines = Wine.objects.all()
    return render(request, './all-wines.html', {'wines': wines})


def detail_cheese_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = Cheese.objects.get(id=id)
        print("🍋 ", product_object, type(product_object))
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./cheese-product.html", context=context)


def detail_wine_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = Wine.objects.get(id=id)
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./wine-product.html", context=context)    


def get_list_pairings(request, id=None):
    pairings_list = None
    if id is not None:
        id_product = id
        print("🪼 ", id_product, type(id_product))
        pairings_list = Pairing.objects.filter(cheese=id_product)
        print("🐍 ", pairings_list)
        pairings_id_list = pairings_list.values_list("id", flat=True)
        print("🦄 ", pairings_id_list)
        
        context = {
            "id_pairings": pairings_id_list
        }
    
    return redirect(get_pairing, context)


def get_pairing(request):
    pairing_object = None
    print("🦊 ", request)
    
    if id is not None:
        id_pairing = id
        pairing_object = Pairing.objects.filter(id=id)
        print("🐙 ", pairing_object, type(pairing_object))
    
    context = {

    }
    return render(request, './pairing.html', context=context)
 
 
def data_not_found(request):
    
    return render(request, './not-found.html')