from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


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


@login_required()
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})
