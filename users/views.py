from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, SearchForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from products.models import Cheese, Wine


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
    # on récupère le texte de l'input
    query_dict = request.GET
    print("🌈 ", query_dict)
    query = query_dict.get("q")
    print("⭐️ ", query)
    
    # on vérifie qu'on reçoit bien la data:
    if query is not None:
        print("🌵 ", query)

        try:
            # on récupère l'id de l'objet fromage cherché
            id_cheese = Cheese.objects.filter(name__icontains=query).values('id')
            print("🍎 ", id_cheese, type(id_cheese))
            
            if len(id_cheese) == 0:
                id_wine = Wine.objects.filter(name__icontains=query).values('id')
                print("🌼 ", id_wine, type(id_wine))
                id_to_send = id_wine[0]['id']
                print("🌸 ", id_to_send, type(id_to_send))
                wine_to_display = Wine.objects.get(id=id_to_send)
                print("🌺 ", wine_to_display, type(wine_to_display))
                
                context = {
                    "id_wine": id_to_send,
                    "wine": wine_to_display
                }
                return render(request, './home.html', context)
            
            elif id_cheese is not None:   
                # id nettoyé, sorti du QuerySet
                id_to_send = id_cheese[0]['id']
                print("🍐 ", id_to_send, type(id_to_send))
                cheese_to_display = Cheese.objects.get(id=id_to_send)
                print("🍏 ", cheese_to_display, type(cheese_to_display))
                
                context = {
                    "id_cheese": id_to_send,
                    "cheese": cheese_to_display
                }
                return render(request, './home.html', context)
            
            else:
                pass
             
        except:
            return redirect('not-found') 
            
    else:
        pass  
      
    context = {
    }
    return render(request, './home.html', context)


def goodbye(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './goodbye.html', context)



    
 
  