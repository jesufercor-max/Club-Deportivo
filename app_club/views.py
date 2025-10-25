from django.shortcuts import render
from .models import Usuario

# Create your views here.

# Vista Urls: index.html
def index(request):
   return render(request, 'index.html')

# Vista 1: Usuario del club
def mostrar_usuario(request):
   usuarios = Usuario.objects.all()
   return render(request, 'app_club/usuario.html', {"mostrar_usuario":usuarios})

