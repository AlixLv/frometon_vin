from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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
        product_object = get_object_or_404(Cheese, id=id)
        
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./cheese-product.html", context=context)



def detail_wine_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = get_object_or_404(Wine, id=id)
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./wine-product.html", context=context)    



def get_pairing(request):
    objects_pairing_list = []
    
    
    try:
        # Récupère la valeur du paramètre 'product_name' du QueryDict envoyé via form
        name_product = request.GET.get('product_name')
        searched_product = get_object_or_404(Cheese, name = name_product)
        id_product = searched_product.id
        
        if id_product:
            pairings_list = Pairing.objects.filter(cheese=id_product)
            print("🐍 ", pairings_list)
            pairings_id_list = get_list_or_404(Pairing.objects.filter(cheese=id_product).values_list("id", flat=True))
            print("🦚 ", pairings_id_list)
            
            for pairing in pairings_list:
                objects_pairing_list.append(Wine.objects.get(id=pairing.wine.id))

            print("🦑", objects_pairing_list, type(objects_pairing_list))        
            
            context = {
                "searched_product": searched_product,
                "pairings_list": pairings_list,
                "objects_pairing_list": objects_pairing_list
            }

            return render(request, './pairing.html', context=context)
        
        else:
            return render(request,'./not-found.html')
    
    except:
        return redirect('not-found')
 
 
 
def data_not_found(request):
    
    return render(request, './not-found.html')