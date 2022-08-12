from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import TipoDeUsuario
from p_vagas_todo import utils

def cadastro(request):
    return render(request, 'usuario/cadastro.html')

def cadastro_empresa(request):
    if request.method == 'POST':
        n_empresa = request.POST['n_empresa']
        cnpj = request.POST['cnpj']
        email = request.POST['email']
        senha = request.POST['senha1']
        senha2 = request.POST['senha2']
        
        if utils.confirmacao(n_empresa,cnpj,email):
            if utils.confima_senha(senha, senha2):
                usuario = User.objects.create_user(username = email, email = email, first_name = n_empresa, password = senha)
                usuario.save()
                usuario_at = get_object_or_404(User, username = email)
                tipo = TipoDeUsuario.objects.create(usuario = usuario_at, tipo = 'emp')
                tipo.save()
                return redirect('login')

    return render(request, 'usuario/cadastro_empresa.html')

def cadastro_candidato(request):
    if request.method =='POST':
        nome = request.POST['n_candidato']
        email = request.POST['email']
        cpf = request.POST['CPF']
        senha = request.POST['senha1']
        senha2 = request.POST['senha2']
        if utils.confirmacao(nome,cpf,email):
            if utils.confima_senha(senha, senha2):
                usuario = User.objects.create_user(username = email, email = email, first_name = nome, password = senha)
                usuario.save()
                usuario_at = get_object_or_404(User, username = email)
                tipo = TipoDeUsuario.objects.create(usuario = usuario_at, tipo = 'cad')
                tipo.save()
                return redirect('login')

    return render(request, 'usuario/cadastro_candidato.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = auth.authenticate(request, username = email, password = senha)
        if user is not None:
            auth.login(request, user)
            tipo = get_object_or_404(TipoDeUsuario, usuario_id = user.id)
            if tipo.tipo == "emp":
                return redirect('vagasempresa')
            elif tipo.tipo == "cad":
                return redirect('index')
    else:
        return render(request, 'usuario/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')