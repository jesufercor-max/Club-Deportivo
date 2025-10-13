from django.core.management.base import BaseCommand
from app_club.models import Usuario, Perfil, Entrenador, Equipo, Jugador, Instalacion, Torneo, Evento
from faker import Faker

class Command(BaseCommand):
    help = 'Genera 5 datos aleatorios por modelo usando solo Faker (sin random ni datetime)'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')

        # Crear Usuarios y Perfiles
        usuarios = []
        for _ in range(5):
            u = Usuario.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                email=fake.unique.email(),
                fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=40)
            )
            Perfil.objects.create(
                usuario=u,
                direccion=fake.address(),
                telefono=fake.phone_number()
            )
            usuarios.append(u)

        # Entrenadores
        for i, u in enumerate(usuarios[:3]):
            Entrenador.objects.create(
                usuario=u,
                especialidad=fake.job(),
                experiencia_anios=fake.random_int(min=1, max=15),
                salario=fake.random_int(min=1500, max=3500)
            )

        # Equipos
        equipos = []
        categorias = ["Infantil", "Juvenil", "Senior"]
        for i in range(3):
            eq = Equipo.objects.create(
                nombre=fake.word().capitalize(),
                categoria=categorias[i % 3],
                fecha_creacion=fake.date_this_decade(),
                entrenador=Entrenador.objects.all()[i]
            )
            equipos.append(eq)

        # Jugadores
        posiciones = ["Portero", "Defensa", "Centrocampista", "Delantero"]
        for i, u in enumerate(usuarios):
            Jugador.objects.create(
                usuario=u,
                posicion=posiciones[i % 4],
                numero=fake.random_int(min=1, max=99),
                equipo=equipos[i % 3]
            )

        # Instalaciones
        tipos = ["Campo", "Pista", "Gimnasio"]
        for i in range(3):
            Instalacion.objects.create(
                nombre=fake.company(),
                tipo=tipos[i % 3],
                capacidad=fake.random_int(min=100, max=1000),
                direccion=fake.address()
            )

        # Torneos
        for i in range(2):
            Torneo.objects.create(
                nombre=fake.word().capitalize(),
                fecha_inicio=fake.date_this_year(),
                fecha_fin=fake.date_this_year(after_today=True)
            )

        # Eventos
        for i in range(2):
            Evento.objects.create(
                nombre=fake.catch_phrase(),
                descripcion=fake.text(),
                fecha=fake.date_time_this_year()
            )

        self.stdout.write(self.style.SUCCESS("✅ Se generaron datos simples para todos los modelos usando solo Faker."))
