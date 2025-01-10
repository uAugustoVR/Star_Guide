from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.froms import loginforms, signupforms

def log_in(request):
    form = loginforms()
    
    if request.method == 'POST':
        form = loginforms(request.POST)

        if not form.is_valid():
            return render(request, 'users/log_in.html', {'form': form})

        password = form.cleaned_data.get('password')
        user_name = form.cleaned_data.get('user_name')

        # Verificar se as senhas coincidem
        if password != password:
            messages.error(request, "Senha incorreta. Tente novamente.")
            return redirect('log in')
        
        messages.success(request, "Login realizado com sucesso!")
        return redirect('index')

    return render(request, 'users/log_in.html', {"form": form})

def sign_up(request):
    form = signupforms()
    
    if request.method == 'POST':
        form = signupforms(request.POST)

        if not form.is_valid():
            return render(request, 'users/sign_up.html', {'form': form})

        password = form.cleaned_data.get('password')
        password_2 = form.cleaned_data.get('password_2')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user_name = form.cleaned_data.get('user_name')
        email = form.cleaned_data.get('email')

        # Verificar se as senhas coincidem
        if password != password_2:
            messages.error(request, "As senhas não coincidem. Tente novamente.")
            return redirect('sign up')

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "Este nome de usuário já está em uso. Escolha outro.")
            return redirect('sign up')

        # Criar o usuário
        user = User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return redirect('log in')
    
    return render(request, 'users/sign_up.html', {"form": form})
