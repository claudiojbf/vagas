from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_inicio.urls')),
    path('accounts/', include('app_usuario.urls')),
    path('empresa/', include('app_empresa.urls')),
    path('inscricao/', include('app_inscricao.urls')),
]
