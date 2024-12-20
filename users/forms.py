from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    email = forms.EmailField(max_length=70, widget=forms.EmailInput)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    