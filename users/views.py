from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import LoginForm, RegisterForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from products.models import Cheese, Wine, Pairing
from .models import Favourite, CustomUser
from django.http import Http404, HttpResponse
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
    #print("🔥 ", request.user.id)
    # on récupère le texte de l'input
    query_dict = request.GET
    print("🍋 query dict: ", query_dict)
    query = query_dict.get("q")
    
    # on vérifie qu'on reçoit bien la data:
    if query is not None:
        try:
            cheeses_to_display = get_list_or_404(Cheese.objects.filter(name__icontains=query)) 
            print("🧀 cheeses to display:", cheeses_to_display, type(cheeses_to_display))
             
            context = {
                "cheeses": cheeses_to_display,
                "wines": None
            }
            return render(request, './home.html', context)
        
        except Http404:
                try:
                    wines_to_display = get_list_or_404(Wine.objects.filter(name__icontains=query))
                    print("🍷 wines to display: ", wines_to_display)
                
                    context = {
                        "wines": wines_to_display,
                        "cheeses": None
                    }
                    return render(request, './home.html', context)
                except:
                    return redirect('not-found')
            
    else:
        context = {
            "cheeses": None,
            "wines": None
        }
        return render(request, './home.html', context) 
      
      

def goodbye(request):
    username = request.user.username
    
    context = {
        "username": username
    }
    return render(request, './goodbye.html', context)



def get_profile(request, id=None):
    username = None
    if request.user.is_authenticated:
        print("👀 ", request.user.username, request.user.email, request.user.id)
        user_info = get_object_or_404(CustomUser.user_info.filter(id=request.user.id))
        print("🍕 ", user_info, type(user_info))

        context = {
            "id":user_info.id,
            "username": user_info.username,
            "email": user_info.email
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
                print("🥗 ", user.id, type(user.id))
                
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


def get_favourites(request, id=None):
    if request.user.is_authenticated:
        print("🟣 ", request.user, id)  
        #favourites_user = Favourite.objects.filter(user__id=id).select_related('pairing__cheese', 'pairing__wine').order_by('pairing__cheese__family')
        favourites_user = Favourite.user_favourites.filter(user=id)
        print("🟡 ", favourites_user)
        
        grouped_favourites = {}
        for favourite in favourites_user:
            fam = favourite.pairing.cheese.family
            if fam not in grouped_favourites:
                grouped_favourites[fam] = []
            grouped_favourites[fam].append(favourite)    
        print("🐹 ", grouped_favourites, type(grouped_favourites))

        context = {
            "grouped_favourites": grouped_favourites,
        }
            
        return render(request, './favourites.html', context)      


def add_favourite(request):
    if request.method == 'POST':
        pairing_str = request.POST.get('favourite_pairing')
        print("💙 ", pairing_str, type(pairing_str))
        pairing_int = int(pairing_str)
        in_list = None
        
        try:
            #pairing_to_add = get_object_or_404(Pairing, id=pairing_str)
            pairing_to_add = get_object_or_404(Pairing.pairing_objects.get_pairing_object(id=pairing_int))
            print("💛 ", pairing_to_add, type(pairing_to_add), pairing_to_add.id)
        
            #user_logged = get_object_or_404(CustomUser, id=request.user.id)
            user_logged = get_object_or_404(CustomUser.user_info, username = request.user)
            print("👑 ", user_logged)
            
            check_favourites = Favourite.user_favourites.filter(user__username=user_logged)
            print("🥨 ", check_favourites)
            
            for favourite in check_favourites:
                if favourite.pairing.id == pairing_to_add.id:
                    print("🍉", favourite, favourite.pairing.id, "----", pairing_to_add.id)
                    in_list= True
                    break
                else:
                    in_list=False
                    
            if in_list == True:
                return HttpResponse("Vous avez déjà enregistré cet accord !", status=404)
            else:
                Favourite.objects.create(user=user_logged, pairing=pairing_to_add)
            
            return redirect('favourites', id=request.user.id)
        # toute exception se produisant dans le bloc try est capturée dans le bloc except
        # e représente l'instance de classe Exception et permet d'accéder aux infos de l'erreur
        except Pairing.DoesNotExist:
            return HttpResponse("L'accord demandé n'existe pas.", status=404)
        except CustomUser.DoesNotExist:
            return HttpResponse("L'utilisateur.rice n'existe pas.", status=404)
        except Exception as e:
            return HttpResponse(f"Erreur inattendue : {str(e)}", status=400)   
    
    return HttpResponse("Méthode non autorisée", status=405)


def delete_favourite(request):
    if request.method == 'POST':
        favourite_str = request.POST.get('favourite_pairing')
        print("❌ ", favourite_str, type(favourite_str)) 
       
        try:
            cheese_id = favourite_str.split('cheese:')[1].split('-')[0]
            print("🧀 cheese id: ", cheese_id, )
            
            wine_id = favourite_str.split('wine:')[1]
            print("🍷 wine id: ", wine_id)
            
            #pairing_obj = get_object_or_404(Pairing, cheese=cheese_id, wine=wine_id)
            pairing_obj = get_object_or_404(Pairing.cheese_objects.get_cheese_pairing(cheese_id=cheese_id, wine_id=wine_id))
            print("💔 pairing to delete: ", pairing_obj, type(pairing_obj))
            print(pairing_obj.id)
            
            #user_logged = get_object_or_404(CustomUser, id=request.user.id)
            user_logged = get_object_or_404(CustomUser.user_info, username=request.user)
            print("👑 user: ", user_logged, type(user_logged))
            
            user_favourites = get_list_or_404(Favourite.user_favourites.filter(user=user_logged))
            print("💛 user's favourites: ", user_favourites, type(user_favourites))
            
            for favourite in user_favourites:
                # identification de l'id de l'instance Pairing associée au favoris (relation ForeignKey)
                if favourite.pairing.id == pairing_obj.id:
                    print("✅ pairing object associated id: ", favourite.pairing.id, "favourite pairing object id: ", pairing_obj.id)
                    favourite.delete()
                    break
            
            #updated_user_favourites = Favourite.objects.filter(user__username=user_logged)    
            updated_user_favourites = get_list_or_404(Favourite.objects.filter(user=user_logged))
            print("💝 update user's favourites: ", updated_user_favourites, len(updated_user_favourites))
            
            return redirect('favourites', id=request.user.id)
        
        except CustomUser.DoesNotExist:
            return HttpResponse("L'utilisateur.rice n'existe pas.", status=404) 
        except Pairing.DoesNotExist:
            return HttpResponse("L'accord recherché n'existe pas.", status=404) 
        except Exception as e:
            return HttpResponse(f"Erreur inattendue : {str(e)}", status=400)      
    return HttpResponse("Méthode non autorisée", status=405)         