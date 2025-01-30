from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, SignupForms
from .forms import SignupForms

def log_in(request):
    if request.user.is_authenticated:
        messages.warning(request, "Você já esta conectado!")
        return redirect('index')
    else:
        form = LoginForms()
        
        if request.method == 'POST':
            form = LoginForms(request.POST)

            if not form.is_valid():
                return render(request, 'users/log_in.html', {'form': form})

            password = form.cleaned_data.get('password')
            user_name = form.cleaned_data.get('user_name')

            user_login = auth.authenticate(
                request,
                username=user_name,
                password=password
            )

            if not user_login:
                messages.error(request, "Nome do usuário ou senha incorreto.")
                return redirect('log in')
            else:
                auth.login(request, user_login)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index')

        return render(request, 'users/log_in.html', {"form": form})

def sign_up(request):
    if request.user.is_authenticated:
        messages.warning(request, "Você já esta conectado!")
        return redirect('index')
    else:
        form = SignupForms()
        
        if request.method == 'POST':
            form = SignupForms(request.POST)

            if not form.is_valid():
                return render(request, 'users/sign_up.html', {'form': form})

            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user_name = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect('log in')
        
        return render(request, 'users/sign_up.html', {"form": form})

def log_out(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Nenhuma conta conectada!")
        messages.warning(request, "Faça login ou cadastre-se agora!")
        return redirect('log in')
    else:
        auth.logout(request)
        messages.success(request, "Desconectado!")
        return redirect('log in')