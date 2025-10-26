from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Sum
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

# Vista 7: Participaciones de un torneo específico
def participaciones_por_torneo(request, torneo_id):
   participaciones = Participacion.objects.select_related('torneo', 'equipo')
   participaciones = Participacion.objects.filter(torneo_id=torneo_id)
   participaciones = (Participacion.objects.raw("SELECT  p.id, p.puntos, p.equipo_id, p.torneo_id" 
                                               + "FROM app_club_participacion p "
                                               + "JOIN app_club_equipo e ON p.equipo_id = e.id "
                                               + "JOIN app_club_torneo t ON p.torneo_id = t.id "
                                               + "WHERE t.id = {torneo_id};"))
   return render(request, 'app_club/participaciones_por_torneo.html', {'participaciones_por_torneo': participaciones})

# Vista 8: Buscar usuario por nombre
def usuario_por_nombre(request, nombre):
   usuarios = Usuario.objects.filter(nombre__icontains=nombre)
   usuarios = (Usuario.objects.raw("SELECT * FROM app_club_usuario u "
                                    + f"WHERE u.nombre LIKE '%{nombre}%';"))
   return render(request, 'app_club/usuario_por_nombre.html', {'usuario_por_nombre': usuarios })

# Vista 9: Total de puntos por torneo
def total_puntos_por_torneo(request):
   torneos = Participacion.objects.values('torneo__nombre').annotate(total_puntos=Sum('puntos'))
   torneos = (Participacion.objects.raw("SELECT t.id, t.nombre AS torneo_nombre, SUM(p.puntos) AS total_puntos "
                                        + "FROM app_club_participacion p "
                                        + "JOIN app_club_torneo t ON p.torneo_id = t.id "
                                        + "GROUP BY t.id, t.nombre;"))

   return render(request, 'app_club/total_puntos_por_torneo.html', {'total_puntos_por_torneo': torneos})

# Errores
def error_400(request, exception):
   return render(request, 'app_club/errores/400.html', status=400)

def error_403(request, exception):
   return render(request, 'app_club/errores/403.html', status=403)

def error_404(request, exception=None):
   return render(request, 'app_club/errores/404.html', status=404)

def error_500(request):
   return render(request, 'app_club/errores/500.html', status=500)

# Error 400 – Bad Request
def prueba_400(request):
   # Forzamos un error 400 lanzando ValueError
   raise ValueError("Forzando error 400")

# Error 403 – Forbidden
def prueba_403(request):
   raise PermissionDenied

# Error 404 – Not Found
def prueba_404(request):
   # Simplemente redirige a una URL que no existe
   return redirect('/pagina_inexistente/')

# Error 500 – Internal Server Error
def prueba_500(request):
   # Forzamos un error de división por cero
   1 / 0
