from django import forms
from django.contrib.auth.models import User

class loginforms(forms.Form):
    user_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva",
            }
        )
    )
    password = forms.CharField(
        label="Senha", 
        required=True, 
        max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class signupforms(forms.Form):
    user_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João_Silva",
            }
        )
    )
    first_name = forms.CharField(
        label="Primeiro nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João",
            }
        )
    )
    last_name = forms.CharField(
        label="Sobrenome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Silva",
            }
        )
    )
    email = forms.EmailField(
        label="Email (opcional)",
        required=False,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com",
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True, 
        max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    password_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        user_name.strip()

        if user_name and " " in user_name:
            raise forms.ValidationError("Nome de usuário inválido. Somente letras e números são permitidos. Sem espaço.")
        elif User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("Nome de usuário já existente. Tente novamente.")
        else:
            return user_name
        
    def clean_password_2(self):
        password = self.cleaned_data.get("password")

        if password != self.cleaned_data.get("password_2"):
            raise forms.ValidationError("As senhas não coincidem. Tente novamente.")
        else:
            return password
