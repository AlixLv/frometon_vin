from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model
from products.models import Cheese
from users.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


#on override la class UserCreationForm pour ajouter le champs email comme obligatoire
class RegisterForm(UserCreationForm):       
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    
    # *args, **kwargs permettent de définir une fonction avec un nombre inconnu et variable d'arguements
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        
    class Meta:
        #get_user_model() permet d'utiliser la class personnalisée CustomUser
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=65)
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
    

        
      