from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import LoginForm, RegisterForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from products.models import Cheese, Wine
from django.http import Http404
from django.urls import reverse


def login_view(request):
    #si la méthode est POST, soumission du formulaire:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print("🦋 ", username)
            email = form.cleaned_data['email']
            print("🦋 ", email)
            password = form.cleaned_data['password']
            print("🦋 ", password)
            #fonction authenticate() vérifie les données postées, si les données sont valides, une instance de la classe User est retournée
            user = authenticate(request, username=username, email=email, password=password)
            print("🦄 ", request.user, request.user.username)
            if user is not None:
                #fonction login() créée un id de session dans le server et le renvoie au navigateur sous la forme d'un cookie
                auth_login(request, user)
                print("🌈 ", request.user)
                print("👑 ", user)
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
    print("🔥 ", request.user.id)
    # on récupère le texte de l'input
    query_dict = request.GET
    query = query_dict.get("q")
    
    # on vérifie qu'on reçoit bien la data:
    if query is not None:

        try:
            cheeses_to_display = get_list_or_404(Cheese.objects.filter(name__icontains=query)) 
            print("🐶 ", cheeses_to_display)
             
            context = {
                "cheeses": cheeses_to_display
            }
            return render(request, './home.html', context)
        
        except Http404:
                try:
                    wines_to_display = get_list_or_404(Wine.objects.filter(name__icontains=query))
                    print("🐱", wines_to_display)
                
                    context = {
                        "wines": wines_to_display
                    }
                    return render(request, './home.html', context)
                except:
                    return redirect('not-found')
            
    else:
        return render(request, './home.html') 
      
      

def goodbye(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './goodbye.html', context)



def get_profile(request, id=None):
    username = None
    if request.user.is_authenticated and id == request.user.id:
        print("👀 ", request.user.username, request.user.email, request.user.id)
        username = request.user.username
        email = request.user.email  
        id = request.user.id
        context = {
            "username": username,
            "email": email,
            "id": id
        }
        return render(request, './profile.html', context)
    else:
        print("⛔️ NOT ALLOWED")
        return render(request, './register.html')  



def update_profile(request, id=None):
    if request.user.is_authenticated and id == request.user.id:
        if request.method == "POST":
            form = UpdateUserForm(request.POST, instance=request.user)
            print("✅ ", form)
            if form.is_valid():
                user = form.save()
                
                context = {
                    "username": user.username,
                    "email": user.email,
                    "id": user.id
                }
                return render(request, './profile.html', context)
        else:
            form = UpdateUserForm()      
        return render(request, './edit-profile.html', {"form": form})
    
    else:
        print("⛔️ NOT ALLOWED")
        return render(request, './register.html') 


def update_password(request, id=None):
    if request.method == "POST":
        message = None
        form = PasswordChangeForm(user = request.user, data=request.POST)
            
        if form.is_valid():
            user = form.save()
            print("⭐️ ", user) 
            # type de messages stockés temporairement dans la session
            messages.success(request, "Votre mot de passe a été modifié avec succès. Veuillez vous reconnecter.")
                   
            return redirect(reverse('login'))
            
        else:
            messages.error(request, f'Veuillez entrer un nouveau mot de passe') 
            
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, './edit-password.html', {"form": form})    
         