# Modelos - Gestor de Club Deportivo

Esta rama contiene los modelos de la aplicación.

## Modelos y sus atributos

### Usuario

- `nombre` (CharField, max_length=50)
- `apellido` (CharField, max_length=50)
- `email` (EmailField, unique=True)
- `fecha_nacimiento` (DateField)

### Perfil

- `usuario` (OneToOneField con Usuario)
- `direccion` (CharField, max_length=100)
- `telefono` (CharField, max_length=15)
- `fecha_registro` (DateTimeField, auto_now_add=True)

### Entrenador

- `usuario` (OneToOneField con Usuario)
- `especialidad` (CharField, max_length=50)
- `experiencia_anios` (IntegerField)
- `salario` (DecimalField, max_digits=8, decimal_places=2)

### Equipo

- `nombre` (CharField, max_length=50)
- `categoria` (CharField, max_length=30)
- `fecha_creacion` (DateField)
- `entrenador` (ForeignKey con Entrenador, on_delete=models.SET_NULL, null=True)

### Jugador

- `usuario` (OneToOneField con Usuario)
- `posicion` (CharField, max_length=20)
- `numero` (IntegerField)
- `equipo` (ForeignKey con Equipo, on_delete=models.CASCADE)

### Partido

- `fecha` (DateTimeField)
- `lugar` (CharField, max_length=50)
- `equipo_local` (ForeignKey con Equipo, related_name='partidos_locales')
- `equipo_visitante` (ForeignKey con Equipo, related_name='partidos_visitantes')

### Resultado

- `partido` (OneToOneField con Partido)
- `goles_local` (IntegerField)
- `goles_visitante` (IntegerField)
- `observaciones` (TextField)

### Instalacion

- `nombre` (CharField, max_length=50)
- `tipo` (CharField, max_length=30)
- `capacidad` (IntegerField)
- `direccion` (CharField, max_length=100)

### Reserva

- `instalacion` (ForeignKey con Instalacion)
- `equipo` (ForeignKey con Equipo)
- `fecha` (DateTimeField)
- `duracion_horas` (IntegerField)

### Torneo

- `nombre` (CharField, max_length=50)
- `fecha_inicio` (DateField)
- `fecha_fin` (DateField)
- `equipos` (ManyToManyField con Equipo, through='Participacion')

### Participacion

- `torneo` (ForeignKey con Torneo)
- `equipo` (ForeignKey con Equipo)
- `posicion_final` (IntegerField)
- `puntos` (IntegerField)

### Evento

- `nombre` (CharField, max_length=50)
- `descripcion` (TextField)
- `fecha` (DateTimeField)
- `asistentes` (ManyToManyField con Usuario)

## Relaciones

- 3 OneToOne: Usuario–Perfil, Usuario–Entrenador, Partido–Resultado
- 3 ManyToOne: Jugador–Equipo, Equipo–Entrenador, Reserva–Instalacion/Equipo
- 3 ManyToMany: Torneo–Equipo (con tabla intermedia Participacion), Evento–Usuario, cualquier otra según necesidad
