from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("User authenticated")
            else:
                return HttpResponse("Invalid creds ")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
