from django.db import models

# Modelo 1: Usuario del club
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

# Modelo 2: Perfil de usuario (OneToOne con Usuario)
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now_add=True)

# Modelo 3: Entrenador
class Entrenador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50)
    experiencia_anios = models.IntegerField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)

# Modelo 4: Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    fecha_creacion = models.DateField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)  # ManyToOne

# Modelo 5: Jugador
class Jugador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    posicion = models.CharField(max_length=20)
    numero = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)  # ManyToOne

# Modelo 6: Partido
class Partido(models.Model):
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=50)
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_locales')  # ManyToOne
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitantes')  # ManyToOne

# Modelo 7: Resultado
class Resultado(models.Model):
    partido = models.OneToOneField(Partido, on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    observaciones = models.TextField()

# Modelo 8: Instalacion
class Instalacion(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    capacidad = models.IntegerField()
    direccion = models.CharField(max_length=100)

# Modelo intermedio ManyToMany con atributos extras: Reserva de Instalacion
class Reserva(models.Model):
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    duracion_horas = models.IntegerField()

# Modelo 9: Torneo
class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    equipos = models.ManyToManyField(Equipo, through='Participacion')  # ManyToMany con tabla intermedia

# Tabla intermedia para la relación Torneo <-> Equipo
class Participacion(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    posicion_final = models.IntegerField()
    puntos = models.IntegerField()

# Modelo 10: Evento del club
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    asistentes = models.ManyToManyField(Usuario)  # ManyToMany simple
