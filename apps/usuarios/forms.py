from django import forms

class loginForms(forms.Form):
    nome_login = forms.CharField (
        label='Nome de login',
        required=True,
        max_length=100,
         widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex. João Silva",
            }
         )
    )
    senha = forms.CharField (
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ) 
    )

class cadastroForms(forms.Form):
    nome_cadastro = forms.CharField (
        label='Nome de cadastro',
        required=True,
        max_length=100,
         widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex. João Silva",
            }
         )
    )

    email = forms.EmailField (
        label='E-mail',
        required=True,
        max_length=100,
         widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex. joaosilva@exemple.com",
            }
         )
    )

    senha_1 = forms.CharField (
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ) 
    )

    senha_2 = forms.CharField (
        label='Confirme sua Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme sua senha",
            }
        ) 
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não pode conter espaços dentro desse campo")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são identicas")
            else:
                return senha_2