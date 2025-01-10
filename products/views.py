from django.shortcuts import render
from products.models import Cheese, Wine 
from django.http import HttpRequest, HttpResponse


def get_cheeses(request):
    cheeses = Cheese.objects.all()
    return render(request, './all-cheeses.html', {'cheeses': cheeses})


def get_wines(request):
    wines = Wine.objects.all()
    return render(request, './all-wines.html', {'wines': wines})


def detail_product_view(request, id=None):
    print("🌺", id)
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
    # if request.method == 'POST':
    # on choppe le texte de l'input, on fait la requête à la db pour trouver l'id correspondant
    # on affiche template product.html
    # else:
    # on affiche home.html
    if request.session.has_key('user_search'):
        product_object = request.session['user_search']
        print("🍇", product_object)
    return(detail_product_view(request, id=5))