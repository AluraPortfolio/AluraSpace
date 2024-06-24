from django.shortcuts import render, redirect
from usuarios.forms import loginForms, cadastroForms

from django.contrib.auth.models import User

def login(request):
    form = loginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = cadastroForms()

    if request.method == 'POST':
        form = cadastroForms(request.POST)    

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro')
            
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():     
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save()
            return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})