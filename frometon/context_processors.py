from products.models import Cheese, Wine


def get_cheeses(request):
    cheeses = Cheese.objects.all()
    print("🥠 ", cheeses)
    return {'cheeses': cheeses}



def get_wines(request):
    wines = Wine.objects.all()
    return {'wines': wines}


def cheese_categories(request):
    types_of_milk = Cheese.category_cheese
    return {'cheese_categories': types_of_milk}


def wine_categories(request):
    colors = Wine.category_wine.all()
    return {'wine_categories': colors}

