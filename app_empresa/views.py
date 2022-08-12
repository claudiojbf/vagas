from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app_usuario.models import TipoDeUsuario
from app_inscricao.models import Inscricao
from .models import Vagas

@login_required
def cadastroVaga(request):
    usuario = request.user.id
    user = get_object_or_404(User, pk = usuario)
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    if request.method == "POST":
        nome = request.POST.get("n_vaga")
        requisitos = request.POST.get("requisitos")
        faixa_salarial = request.POST.get("faixa_salarial")
        escolaridade = request.POST.get("escolaridade")
        vaga = Vagas.objects.create(
            usuario_id = user, 
            nome_vaga = nome, 
            faixa_salarial = faixa_salarial, 
            requisitos = requisitos,
            escolaridade = escolaridade
        )
        vaga.save()
        return redirect("index")
    dados = {
        "tipos" : tipo,
    }
    return render(request, "empresa/cadastra_vagas.html", dados)

@login_required
def vagasEmpresa(request):
    usuario = request.user.id
    user = get_object_or_404(User, pk = usuario)
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    vagas = Vagas.objects.filter(usuario_id_id = user)
    dados = {
        "tipos" : tipo,
        "vagas" : vagas,
    }
    return render(request, "empresa/vagas_empresa.html", dados)

@login_required
def visualizarVaga(request, id):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    vaga = get_object_or_404(Vagas, pk=id)
    inscricao = Inscricao.objects.filter(vaga = id).count
    dados = {
        "tipos" : tipo,
        "vaga": vaga,
        "inscritos": inscricao
    }
    return render(request,'empresa/visualizar_vaga.html',dados )

@login_required
def deletarVaga(request, id):
    vaga =get_object_or_404(Vagas, pk=id)
    vaga.delete()
    return redirect('vagasempresa')

@login_required
def editarVaga(request, id):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    vaga = get_object_or_404(Vagas, pk=id)
    dados = {
        "vaga":vaga,
        "tipos":tipo,
    }
    return render(request, "empresa/editar_vaga.html", dados)

@login_required
def atualizarVaga(request):
    if request.method == "POST":
        vaga_id = request.POST["vaga_id"]
        v = Vagas.objects.get(pk=vaga_id)
        v.nome_vaga = request.POST["n_vaga"]
        v.requisitos = request.POST["requisitos"]
        v.faixa_salarial = request.POST["faixa_salarial"]
        v.escolaridade = request.POST["escolaridade"]
        v.save()
        return redirect("vagasempresa")

@login_required
def visualizarInscritos(request, id):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    inscritos = Inscricao.objects.filter(vaga = id).order_by('pontos')
    dados = {
        "tipos":tipo,
        "inscritos" : inscritos
    }
    return render(request, "empresa/visualizar_inscritos.html", dados)

@login_required
def detalhes_inscrito(request, id):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    inscrito = get_object_or_404(Inscricao, pk=id)
    dados = {
        "tipos":tipo,
        "inscrito": inscrito
    }
    return render(request, "empresa/detalhe_inscrito.html", dados)