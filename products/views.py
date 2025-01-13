from django.shortcuts import render, redirect
from products.models import Cheese, Wine 
from django.forms.models import model_to_dict


def get_cheeses(request):
    cheeses = Cheese.objects.all()
    return render(request, './all-cheeses.html', {'cheeses': cheeses})


def get_wines(request):
    wines = Wine.objects.all()
    return render(request, './all-wines.html', {'wines': wines})


def detail_product_view(request, id=None):
    product_object = None
    if id is not None:
        id_object = id
        product_object = Cheese.objects.get(id=id)
    context = {
            "product_object" : product_object, 
            "id" : id_object       
    }
    return render(request, "./product.html", context=context)


def search_product_view(request):
    # on vérifie qu'on reçoit bien la data:
    if len(request.session['query']) != 0:
        query = request.session['query']
        print("🌵 ", query)

        try:
            # on récupère l'id de l'objet fromage cherché
            id_cheese = Cheese.objects.filter(name__icontains=query).values('id')
            print("🥥 ", id_cheese, type(id_cheese))
            # id nettoyé, sorti du QuerySet
            id_to_send = id_cheese[0]['id']
            print("🥐 ", id_to_send, type(id_to_send)) 
            return redirect('product', id=id_to_send) 
    
        except:
            return redirect('not-found') 
            
    else:
        return redirect('home')        
 
 
def data_not_found(request):
    
    return render(request, './not-found.html')