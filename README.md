# Proyecto Club Deportivo – Rama: errores

## Descripción

Esta rama implementa **páginas de error personalizadas** para los errores HTTP más comunes en Django:

- **400 – Bad Request**  
- **403 – Forbidden**  
- **404 – Not Found**  
- **500 – Internal Server Error**  

El objetivo es proporcionar una **experiencia de usuario más profesional**, mostrando mensajes claros y un enlace al **inicio del sitio**, en lugar de los mensajes genéricos de Django.

---

## Vistas de error

Se han creado vistas en `views.py` que devuelven el template correspondiente y el código HTTP adecuado:

def error_400(request, exception):
    return render(request, 'app_club/errores/400.html', status=400)

def error_403(request, exception):
    return render(request, 'app_club/errores/403.html', status=403)

def error_404(request, exception=None):
    return render(request, 'app_club/errores/404.html', status=404)

def error_500(request):
    return render(request, 'app_club/errores/500.html', status=500)

### Handlers de error ###
handler400 = 'app_club.views.error_400'
handler403 = 'app_club.views.error_403'
handler404 = 'app_club.views.error_404'
handler500 = 'app_club.views.error_500'

### Paht en urls.py ###
path('prueba400/', views.prueba_400, name='prueba_400'),
path('prueba403/', views.prueba_403, name='prueba_403'),
path('prueba404/', views.prueba_404, name='prueba_404'),
path('prueba500/', views.prueba_500, name='prueba_500'),

### Configuración necesaria ###
Para que los errores personalizados funcionen correctamente:

DEBUG debe estar desactivado:

DEBUG = False


ALLOWED_HOSTS debe incluir el host local y cualquier dominio de despliegue:

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.pythonanywhere.com']

### Cómo probar cada error  ###

400 – Bad Request --> Usamos una URL con parámetro inválido	`/prueba_int/no_es_numero/`
403 – Forbidden -->	Lanzamos un PermissionDenied `/prueba403/`
404 – Not Found --> URL inexistente	`/pagina_inexistente/`
500 – Internal Server Error -->	Vista que genera una excepción no manejada	`/prueba500/`
