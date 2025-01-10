from django.shortcuts import render
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
    all_cheeses_names = Cheese.objects.values_list('name', flat=True).distinct()
    
    # on vérifie qu'on reçoit bien la data:
    if request.session.has_key('query'):
        query = request.session['query']
        # on itère sur tous les noms de fromages de la db
        for cheese_name in all_cheeses_names:
            if query == cheese_name:
                # on récupère l'objet fromage cherché
                cheese_to_display = Cheese.objects.filter(name=cheese_name)
                # on récupère l'id
                id_cheese = cheese_to_display.values_list('id', flat=True)
                # id nettoyé, sorti du QuerySet
                id_to_send = id_cheese[0]  
  
    return(detail_product_view(request, id=id_to_send))