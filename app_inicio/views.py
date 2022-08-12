from django.shortcuts import render
from app_usuario.models import TipoDeUsuario
from app_empresa.models import Vagas

def index(request):
    usuario = request.user.id
    tipo = TipoDeUsuario.objects.filter(usuario_id = usuario)
    vagas = Vagas.objects.filter()
    dados = {
        "tipos" : tipo,
        "vagas" : vagas
    }
    return render(request, 'index.html', dados)
