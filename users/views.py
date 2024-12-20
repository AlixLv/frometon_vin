from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, './login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #fonction authenticate() vérifie les données postées, si les données sont valides, une instance de la classe User est retournée
            user = authenticate(request, username=username, email=email, password=password)
            if user:
                #fonction login() créée un id de session dans le server et le renvoie au navigateur sous la forme d'un cookie
                login(request, user)
                messages.success(request, f'Bonjour {user.username.title()}')
                return redirect('home')
        #si le formulaire n'est pas valide ou que le user n'est pas authentifié    
        messages.error(request, f'Les informations sont erronnées')
        return render(request, './login.html', {'form': form})
    
    
def get_home(request):
    return HttpResponse("HOMEPAGE !")