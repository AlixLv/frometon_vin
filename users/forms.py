from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

#on override la class UserCreationForm pour ajouter le champs email comme obligatoire
class RegisterForm(UserCreationForm):       
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "email"
        
    class Meta:
        #get_user_model() permet d'utiliser la class personnalisée CustomUser
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')