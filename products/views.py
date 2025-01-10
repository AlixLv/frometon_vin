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
        all_cheeses_names = Cheese.objects.values_list('name', flat=True).distinct()
        print("🥨", all_cheeses_names)
        print(type(all_cheeses_names))
        for cheese_name in all_cheeses_names:
            print("🥝", cheese_name)
            if product_object == cheese_name:
                print("🍇", cheese_name)
                print(type(cheese_name))
    return(detail_product_view(request, id=5))