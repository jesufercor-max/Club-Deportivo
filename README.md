# 🏋️‍♂️ Proyecto Club Deportivo

Este proyecto en **Django** gestiona la información de un club deportivo, incluyendo usuarios, entrenadores, equipos, torneos, participaciones y manejo de errores personalizados.  

El desarrollo se organiza en distintas ramas (**URLs_1** a **URLs_9** y **Errores**), donde cada una implementa una funcionalidad concreta dentro de la aplicación `app_club`.

---

## 🚀 URLs_1
### ✳️ Descripción
Ruta añadida:
ruta('usuario/', vistas.mostrar_usuario, nombre='mostrar_usuario')

texto

### 👁️ Vista
Permite visualizar todos los usuarios en la plantilla `usuario.html`.

**Con ORM:**
usuarios = Usuario.objetos.todos()

texto

**Con SQL cruda:**
usuarios = Usuario.objects.raw("SELECT * FROM app_club_usuario")

texto

**Renderizado:**
return render(solicitud, 'app_club/usuario.html', {"mostrar_usuario": usuarios})

texto

---

## 🧑‍🏫 URLs_2
### ✳️ Descripción
Ruta:
ruta('entrenador/', vistas.mostrar_entrenador, nombre='mostrar_entrenador')

texto

### 👁️ Vista
Muestra el **ID**, **especialidad**, **salario** del entrenador y su **usuario asociado**.

**Con ORM:**
entrenadores = Entrenador.objects.select_ related('usuario').all()

texto

**Con SQL:**
entrenadores = Entrenador.objects.raw("""
SELECCIONE e.id, u.id, e.especialidad, e.salario
FROM app_club_entrenador e
JOIN app_club_usuario u ON e.usuario_id = u.id;
""")

texto

**Renderizado:**
return render(solicitud, 'app_club/entrenador.html', {'mostrar_entrenador': entrenadores})

texto

---

## 💰 URLs_3
### ✳️ Descripción
Ruta:
ruta('entrenadorSalario/', vistas.mostrar_entrenador_salario, nombre='mostrar_entrenador_salario')

texto

### 👁️ Vista
Visualiza el **ID** y el **salario** de los entrenadores ordenado de mayor a menor.

**Con ORM:**
entrenadores = Entrenador.objects.values('id', 'salario').order_by('-salario')

texto

**Con SQL:**
entrenadores = Entrenador.objects.raw("""
SELECT e.id, e.salario
FROM app_club_entrenador y
ORDER BY e.salario DESC;
""")

texto

---

## 🏆 URLs_4
### ✳️ Descripción
Ruta:
ruta('participaciones/ int:puntos_participacion /', vistas.mostrar_participacion, nombre='mostrar_participacion')

texto

### 👁️ Vista
Filtra y muestra las participaciones con **puntos entre 26 y 29**.

**Con ORM (Q objects):**
participaciones = Participacion.objects.filter(Q(puntos__gt=25) & Q(puntos__lt=30)).order_by('-puntos')

texto

**Con SQL:**
participaciones = Participacion.objects.raw("""
SELECCIONAR *
FROM app_club_participacion p
ÚNETE a app_club_torneo t ON p.torneo_id = t.id
ÚNETE a app_club_equipo e ON p.equipo_id = e.id
DONDE p.puntos > 25 Y p.puntos < 30
ORDENAR POR p.puntos DESC;
""")

texto

---

## 👨‍🏫 URLs_5
### ✳️ Descripción
Ruta con `re_path`:
re_path(r'^entrnadoresExperiencia/(?P <salario> [0-9]+)$', vistas.entrenadores_con_salario, name='entrenadores_con_salario')

texto

### 👁️ Vista
Muestra entrenadores según **salario > 2000** o **experiencia > 5 años**.

**Con ORM:**
entrenadores = Entrenador.objects.filter(Q(salario__gt=salario) | Q(experiencia_anios__gt=5))

texto

**Con SQL:**
entrenadores = Entrenador.objects.raw("""
SELECCIONE e.id, e.salario, e.experiencia_anios
FROM app_club_entrenador e
DONDE e.salario > 2000 OR e.experiencia_anios > 5;
""")

texto

---

## ⚽ URLs_6
### ✳️ Descripción
Ruta:
ruta('equipos_sin_participaciones/', vistas.equipos_sin_participaciones, nombre='equipos_sin_participaciones')

texto

### 👁️ Vista
Muestra los equipos **sin participaciones**.

**Con ORM:**
equipos = Equipo.objects.filter(participacion=Ninguno)

texto

**Con SQL:**
equipos = Equipo.objects.raw("""
SELECT *
FROM app_club_equipo e
LEFT JOIN app_club_participacion p ON p.equipo_id = e.id
WHERE p.id IS NULL;
""")

texto

---

## 🏟️ URLs_7
### ✳️ Descripción
Ruta:
ruta('participaciones/torneo/ int:torneo_id /', vistas.participaciones_por_torneo, nombre='participaciones_por_torneo')

texto

### 👁️ Vista
Muestra las participaciones por torneo (nombre del torneo, equipo, puntos, id).

**Con ORM:**
participaciones = Participacion.objects.select_ related('torneo', 'equipo').filter(torneo_id=torneo_id)

texto

**Con SQL:**
participaciones = Participacion.objects.raw(f"""
SELECCIONAR p.id, p.puntos, p.equipo_id, p.torneo_id
FROM app_club_participacion p
ÚNETE a app_club_equipo e ON p.equipo_id = e.id ÚNETE
a app_club_torneo t ON p.torneo_id = t.id
DONDE t.id = {torneo_id};
""")

texto

---

## 👤 URLs_8
### ✳️ Descripción
Ruta con `re_path`:
re_path(r'^usuario_por_nombre/(?P <nombre> [a-zA-Z]+)$', views.usuario_por_nombre, name='usuario_por_nombre')

texto

### 👁️ Vista
Filtra por nombre de usuario (por ejemplo, “Juan”).

**Con ORM:**
usuarios = Usuario.objects.filter(nombre__icontains=nombre)

texto

**Con SQL:**
usuarios = Usuario.objects.raw(f"""
SELECT * FROM app_club_usuario u
WHERE u.nombre LIKE '%{nombre}%';
""")

texto

---

## 🧮 URLs_9
### ✳️ Descripción
Ruta:
ruta('total_puntos_por_torneo/', vistas.total_puntos_por_torneo, nombre='total_puntos_por_torneo')

texto

### 👁️ Vista
Muestra la **suma total de puntos por torneo**.

**Con ORM:**
torneos = Participacion.objects.values('torneo__nombre').annotate(total_puntos=Sum('puntos'))

texto

**Con SQL:**
torneos = Participacion.objects.raw("""
SELECCIONAR t.id, t.nombre AS torneo_nombre, SUM(p.puntos) AS total_puntos
FROM app_club_participacion p
ÚNETE a app_club_torneo t ON p.torneo_id = t.id
GROUP BY t.id, t.nombre;
""")

texto

---

## ⚠️ Rama: ERRORES
### ✳️ Descripción
Implementa **páginas personalizadas** para los errores HTTP comunes:

| Código | Error | Descripción |
|--------|--------|-------------|
| 400 | Bad Request | Solicitud incorrecta |
| 403 | Forbidden | Prohibido |
| 404 | Not Found | Página no encontrada |
| 500 | Internal Server Error | Error interno del servidor |

### 👁️ Vistas
def error_400(solicitud, excepción): return render(solicitud, 'app_club/errores/400.html', estado=400)
def error_403(solicitud, excepción): return render(solicitud, 'app_club/errores/403.html', estado=403)
def error_404(solicitud, excepción=Ninguna): return render(solicitud, 'app_club/errores/404.html', estado=404)
def error_500(solicitud): return render(solicitud, 'app_club/errores/500.html', estado=500)

texto

### ⚙️ Configuración
DEBUG = Falso
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.pythonanywhere.com']

texto

### 🔗 Handlers
handler400 = 'app_club.views.error_400'
handler403 = 'app_club.views.error_403'
handler404 = 'app_club.views.error_404'
handler500 = 'app_club.views.error_500'