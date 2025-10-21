from django.shortcuts import render
from .models import Usuario

# Create your views here.

# Vista 1: Usuario del club
def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_club/usuario/usuario.html', {})