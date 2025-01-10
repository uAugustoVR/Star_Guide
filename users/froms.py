from django import forms

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
                "placeholder": "Ex.: João Silva",
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
        label="Email",
        required=True,
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