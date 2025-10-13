# Backups - Gestor de Club Deportivo

Esta rama está dedicada a la **gestión, backup y generación de datos automáticos** para pruebas o restauraciones en la aplicación, siguiendo las siguientes tareas principales:

---

## Rellenar tablas con seeders

Para poblar las tablas automáticamente se emplean **seeders** personalizados, que permiten insertar datos de prueba coherentes en todos los modelos definidos previamente. Se recomienda ejecutar los seeders en entornos de prueba o desarrollo para garantizar la integridad de los datos reales.

---

## Comando para generar datos aleatorios con Faker

Se ha implementado un comando propio de Django que utiliza la librería **Faker** para crear 10 datos aleatorios por cada modelo de la aplicación.

- El comando garantiza variedad y verosimilitud en todos los campos, incluyendo relaciones entre modelos (ForeignKey, ManyToMany, etc.).
- Cada vez que se ejecuta, crea nuevos registros usando información simulada, útil para pruebas y tests de rendimiento.

### Ejemplo de uso

python manage.py poblar_base

Este comando generará 10 registros falsos en cada una de las siguientes tablas:

- Usuario
- Perfil
- Entrenador
- Equipo
- Jugador
- Partido
- Resultado
- Instalacion
- Reserva
- Torneo
- Participacion
- Evento

---

## Crear y restaurar un backup con fixtures

Para preservar la información, la rama contiene _fixtures_ exportados desde la base de datos mediante los comandos de Django.

- Los fixtures pueden cargarse en cualquier entorno compatible con el mismo esquema de modelos.
- Cada fixture es el backup de una tabla/modelo.

### Comandos relevantes

#### Crear backup

python manage.py dumpdata app.Modelo --indent 4 > nombre_fixture.json

#### Restaurar backup

python manage.py loaddata nombre_fixture.json

---

## Script auxiliar: `fix_fixture.py`

Esta utilidad se desarrolló para solucionar un problema específico de codificación en Windows, permitiendo la carga correcta de algunos fixtures.

- Solo es necesario emplearlo si se detectan errores de codificación en sistemas Windows.
- No forma parte del workflow didáctico visto en clase; se añadió como apoyo técnico para compatibilidad transversal.

### Uso del script

python fix_fixture.py fixture_original.json fixture_corregido.json

Esto creará una versión compatible del fixture para su utilización en Windows.

---

## Estructura de backup

Los archivos de backup y los comandos de generación están organizados según los modelos principales definidos en la rama _modelos_. Así se asegura que relaciones y dependencias no se pierdan al restaurar datos.
