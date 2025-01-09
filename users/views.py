from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, SearchForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from products.models import Cheese



def login_view(request):
    #si la méthode est POST, soumission du formulaire:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #fonction authenticate() vérifie les données postées, si les données sont valides, une instance de la classe User est retournée
            user = authenticate(request, username=username, email=email, password=password)
            if user is not None:
                #fonction login() créée un id de session dans le server et le renvoie au navigateur sous la forme d'un cookie
                auth_login(request, user)
                return redirect('home')
            else:
             #si le formulaire n'est pas valide ou que le user n'est pas authentifié    
                messages.error(request, f'Les informations sont erronnées') 
    
    else:  
        #si la méthode est GET, on affiche le formulaire 
        form = LoginForm() 
     
     #rendu du template avec le formulaire   
    return render(request, './login.html', {'form': form})


def logout_view(request):
    logout(request) 
       
    return redirect('goodbye')


def register_view(request):
    #si la méthode est POST, on créée une instance du formulaire 
    if request.method == "POST":
        form = RegisterForm(request.POST)
        #si le formulaire est valid, on l'enregistre avec les nouvelles data
        if form.is_valid():
            #form.save() se charge de cleaner les data
            user = form.save()
            return redirect('login')
    else:
        #si la méthode est GET, on affiche le formulaire 
        form = RegisterForm()    
    #si le formulaire n'est pas valide, on affiche de nouveau le formulaire vide    
    return render(request, './register.html', {"form": form})


def home(request):
    username = request.user.username
    
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            product_object = form.save()
            return redirect(search_product_view)
    else:
        form = SearchForm()    
    
    context = {
        "username": username,
        "form": form
    }
    return render(request, './home.html', context)


def goodbye(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './goodbye.html', context)


def detail_product_view(request, id=None):
    print("hey")
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
    print("coucou")
    return(detail_product_view(request, id=5))
    
 
  