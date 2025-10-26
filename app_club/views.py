from django.shortcuts import render
from django.db.models import Q
from .models import Usuario, Entrenador, Participacion, Equipo

# Create your views here.

# Vista Urls: index.html
def index(request):
   return render(request, 'index.html')

# Vista 1: Usuario del club
def mostrar_usuario(request):
   usuarios = Usuario.objects.all()
   usuarios = (Usuario.objects.raw("SELECT * FROM app_club_usuario"))
   return render(request, 'app_club/usuario.html', {"mostrar_usuario":usuarios})

# Vista 2: Entrenadores asignados a Usuario (id)
def mostrar_entrenador(request):
   entrenadores = Entrenador.objects.select_related('usuario').all()
   entrenadores = (Entrenador.objects.raw ("SELECT e.id, u.id, e.especialidad, e.salario "
                                           + "FROM app_club_entrenador e "
                                           + "JOIN app_club_usuario u ON e.usuario_id = u.id;"))
   return render(request, 'app_club/entrenador.html', {'mostrar_entrenador': entrenadores})

# Vista 3: Entrenador según su salario (de mayor a menor)
def mostrar_entrenador_salario(request):
   entrenadores = Entrenador.objects.values('id', 'salario').order_by("-salario")
   entrenadores = (Entrenador.objects.raw ("SELECT e.id, e.salario " 
                                           + "FROM app_club_entrenador e "
                                           + "ORDDER BY e.salario"))
   return render(request, 'app_club/entrenadorSalario.html', {'mostrar_entrenador_salario': entrenadores})

# Vista 4: Participación donde los equipos tengan mas de 25 y menos de 30 puntos
def mostrar_participacion(request, puntos_participacion):
   participaciones = Participacion.objects.prefetch_related("torneo" , "equipo")
   # Filtramos participaciones con puntos entre 25 y 30 usando Q
   participaciones = Participacion.objects.filter(Q(puntos__gt=25) & Q(puntos__lt=30)).order_by("-puntos")
   participaciones = (Participacion.objects.raw ("SELECT * FROM app_club_participacion p "
                                                 + "JOIN app_club_torneo t ON p.torneo_id = t.id "
                                                 + "JOIN app_club_equipo e ON p.equipo_id = e.id "
                                                 + "WHERE p.puntos > 25 AND p.puntos < 30 "
                                                 + "ORDER BY p.puntos DESC "))
   return render(request, 'app_club/participaciones.html', {'mostrar_participacion' : participaciones})

# Vista 5: Entrenadores con salario mayor a 2000€ o la experiencia mayor a 5 años
def entrenadores_con_salario(request, salario):
   entrenadores = Entrenador.objects.filter(Q(salario__gt=salario) | Q(experiencia_anios__gt=5))
   entrenadores = (Entrenador.objects.raw("SELECT e.id, e.salario, e.experiencia_anios "
                                           + "FROM app_club_entrenador e "
                                           + "WHERE e.salario > 2000 OR e.experiencia_anios > 5 "))
   return render(request, 'app_club/entrenadoresExperiencia.html', {'entrenadores_con_salario': entrenadores})

# Vista 6: Equipos sin Participaciones
def equipos_sin_participaciones(request):
   equipos = Equipo.objects.filter(participacion=None)
   equipos = (Equipo.objects.raw("SELECT * FROM app_club_equipo e "
                                 + "LEFT JOIN app_club_participacion p ON p.equipo_id = e.id "
                                 + "WHERE p.id IS NULL;"))
   return render(request, 'app_club/equipos_sin_participaciones.html', {'equipos_sin_participaciones': equipos})