from django.shortcuts import render
from django.contrib import messages

from . import forms, oktaapi


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            session = oktaapi.login(data['username'], data['password'])

            if not session:
                messages.error(request, 'Authentication was unsuccessful!')
                request.session['sessionToken'] = session
