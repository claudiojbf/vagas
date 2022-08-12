from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Inscricao
from app_empresa.models import Vagas
from django.contrib.auth.models import User
from app_usuario.models import TipoDeUsuario

@login_required
def inscricao(request, id):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario) 
    vaga = get_object_or_404(Vagas, pk=id)  
    dados = {
        "tipos": tipo,
        "vaga":vaga
    }
    return render(request, "inscricao/inscricao.html", dados)

@login_required
def inscrito(request):
    if request.method == "POST":
        usuario = request.user.id
        pontos = 0
        user = get_object_or_404(User, pk = usuario)
        vaga = request.POST['vaga_id']
        vaga_ob = get_object_or_404(Vagas, pk = vaga)
        empresa = get_object_or_404(User, pk = vaga_ob.usuario_id_id)
        experiencias = request.POST['experiencias']
        faixa_salarial = request.POST['faixa_salarial']
        escolaridade = request.POST['escolaridade']
        if escolaridade == vaga_ob.escolaridade:
            pontos += 1
        if faixa_salarial == vaga_ob.faixa_salarial:
            pontos += 1
        inscricao = Inscricao.objects.create(faixa_salarial = faixa_salarial, experiencia = experiencias, escolaridade = escolaridade, usuario = user, empresa = empresa, vaga = vaga_ob, pontos = pontos)
        inscricao.save()
        return redirect('/')
