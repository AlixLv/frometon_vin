from products.models import Cheese, Wine

def cheese_categories(request):
    # values_list pour retourner une liste de valeurs sur le champs "type_of_milk"
    # argument flat=True pour indiquer qu'on veut une liste simple de valeurs, pas de tuples
    # distinct() pour garantir des valeurs uniques
    types_of_milk = Cheese.objects.values_list('type_of_milk', flat=True).distinct()
    return {'cheese_categories': types_of_milk}


def wine_categories(request):
    colors = Wine.objects.values_list('color', flat=True).distinct()
    return {'wine_categories': colors}

