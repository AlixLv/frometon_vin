from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout 
from django.contrib.auth.forms import UserCreationForm

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
                print(f"🌈 {request}")
                return redirect('home')
            else:
             #si le formulaire n'est pas valide ou que le user n'est pas authentifié    
                messages.error(request, f'Les informations sont erronnées') 
    
    else:  
        #si la méthode est GET, on affiche le formulaire 
        print(f"⭐️ HEY")
        form = LoginForm() 
     
     #rendu du templace avec le formulaire   
    return render(request, './login.html', {'form': form})


def logout_view(request):
    logout(request) 
       
    return redirect('goodbye')


def register_view(request):
    #si la méthode est POST, on créée une instance du formulaire 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #si le formulaire est valid, on l'enregistre avec les nouvelles data
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #si la méthode est GET, on affiche le formulaire 
        form = UserCreationForm()    
    #si le formulaire n'est pas valide, on affiche de nouveau le formulaire vide    
    return render(request, './register.html', {"form": form})


def home(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './home.html', context)


def goodbye(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './goodbye.html', context)