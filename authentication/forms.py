from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='username', widget=forms.PasswordInput())
