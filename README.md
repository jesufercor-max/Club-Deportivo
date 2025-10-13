# Proyecto Web - Gestor de Club Deportivo

Este repositorio contiene el proyecto completo de la página web para la gestión de un club deportivo. A continuación, se describe la estructura del proyecto, los modelos, comandos y herramientas desarrolladas para cubrir los requisitos del trabajo.

---

## Descripción general del proyecto

La página web está diseñada para gestionar los diferentes aspectos de un club deportivo, incluyendo usuarios, equipos, entrenadores, partidos, instalaciones, reservas, torneos, eventos y resultados. La aplicación permite administrar datos, generar backups, y facilitar pruebas mediante generación automática de datos.

---

## Estructura del repositorio y ramas

Se han creado tres ramas principales para organizar el trabajo de forma clara:

- **Configuracion_inicial:** Preparación del proyecto Django y su aplicación base.
- **Modelos:** Definición de los modelos que representan las entidades del club deportivo.
- **Backups:** Gestión de los datos mediante fixtures, seeders y comandos de generación aleatoria con Faker.

---

## Preparación del proyecto Django

Se creó el proyecto Django y la aplicación principal, configurando todo lo necesario para conectar con la base de datos, gestionar migraciones y ejecutar comandos personalizados.

---

## Modelos y sus requisitos

Se definieron 10 modelos principales que cumplen los requisitos exigidos:

- Cumplen al menos 3 relaciones OneToOne, 3 relaciones ManyToOne y 3 relaciones ManyToMany.
- Al menos una relación ManyToMany incluye una tabla intermedia con atributos extra.
- Cada modelo tiene al menos 4 campos individuales.
- Se utilizan 10 atributos distintos de Django (sin contar las relaciones).
- Se emplean más de 10 parámetros diferentes en total en los campos (por ejemplo, max_length, unique, auto_now_add, null, blank, max_digits, decimal_places, related_name, etc.).

---

## Modelos principales y sus atributos

Se detallan los modelos, atributos y parámetros en el archivo `README_Modelos.md` para mantener el README principal limpio y ordenado. Allí se explica en qué consiste cada modelo, cada atributo y cada parámetro usado.

---

## Diagrama Entidad-Relación

Se diseñó el modelo entidad-relación que describe todas las entidades y sus relaciones según lo solicitado. Este diagrama se encuentra en el archivo `ER_diagrama.png` dentro del repositorio.

---

## Relleno de tablas con seeders

Para poblar la base de datos de prueba, se implementaron seeders personalizados que cargan datos básicos iniciales y garantizan consistencia.

---

## Generación de datos aleatorios con Faker

Se creó un comando personalizado de Django:

python manage.py poblar_base

Este comando genera 10 registros aleatorios para cada modelo, creando datos verosímiles para probar la aplicación.

---

## Backup y restauración con fixtures

Se utilizan fixtures en formato JSON para exportar e importar los datos de la base de datos. Los comandos básicos para la gestión son:

- Crear backup:

python manage.py dumpdata app.Modelo --indent 4 > nombre_fixture.json

- Restaurar backup:

python manage.py loaddata nombre_fixture.json

Se incluye un script auxiliar `fix_fixture.py` para solucionar problemas de codificación en Windows cuando se cargan los fixtures.

---

## Gestión de archivos en Git

Se configuró el archivo `.gitignore` para evitar subir archivos innecesarios, como migraciones temporales, archivos de base de datos locales, entornos virtuales, archivos compilados, etc.

---

## Código no visto en clase

Se explica en detalle todo código externo al temario visto en clase, como:

- El uso y funcionamiento del script `fix_fixture.py`.
- El comando personalizado que genera datos con Faker.
- El uso del campo `DecimalField` y sus parámetros (por ejemplo en el modelo Entrenador para el salario).
- Otros parámetros avanzados empleados en los modelos.

---
