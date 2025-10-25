from django.shortcuts import render
from .models import Usuario, Entrenador

# Create your views here.

# Vista Urls: index.html
def index(request):
   return render(request, 'index.html')

# Vista 1: Usuario del club
def mostrar_usuario(request):
   usuarios = Usuario.objects.all()
   return render(request, 'app_club/usuario.html', {"mostrar_usuario":usuarios})
   usuarios = (Usuario.objects.raw("SELECT * FROM app_club_usuario"))

# Vista 2: Entrenadores asignados a Usuario (id)
def mostrar_entrenador(request):
   entrenadores = Entrenador.objects.select_related('usuario').all()
   return render(request, 'app_club/entrenador.html', {'mostrar_entrenador': entrenadores})
   entrenadores = (Entrenador.objects.raw ("SELECT e.id, u.id, e.especialidad, e.salario "
                                           + "FROM app_club_entrenador e "
                                           + "JOIN app_club_usuario u ON e.usuario_id = u.id;"))

# Vista 3: Entrenador según su salario (de mayor a menor)
def mostrar_entrenador_salario(request):
   entrenadores = Entrenador.objects.values('id', 'salario').order_by("-salario")
   return render(request, 'app_club/entrenadorSalario.html', {'mostrar_entrenador_salario': entrenadores})
   entrenadores = (Entrenador.objects.raw ("SELECT e.id, e.salario " 
                                           + "FROM app_club_entrenador e "
                                           + "ORDDER BY e.salario"))