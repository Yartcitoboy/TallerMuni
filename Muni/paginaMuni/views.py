from django.shortcuts import render, redirect
from .models import Usuario, Taller, Inscripcion
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .form import InscripcionForm
# Esto es ahora
from django.contrib.auth.decorators import login_required

# Create your views here.
# Muni/paginaMuni/views.py
def index(request):
    # Verificar si el usuario está logueado (si hay un usuario en la sesión)
    usuario_nombre = request.user.nombre if request.user.is_authenticated else None  # Cambiado para obtener el nombre del usuario autenticado

    # Mostrar el mensaje de bienvenida si existe
    if messages.get_messages(request):
        return render(request, 'web/index.html', {'messages': messages.get_messages(request), 'usuario_nombre': usuario_nombre})

    return render(request, 'web/index.html', {'usuario_nombre': usuario_nombre})

@login_required
def taller(request):
    talleres = Taller.objects.all()
    print("Vista 'taller' cargada")  # Log para saber que la vista fue llamada correctamente.

    if request.method == 'POST':
        print("Método POST recibido")  # Verificar que se está recibiendo un POST.
        print("Datos recibidos:", request.POST)  # Log de los datos enviados por el formulario.

        form = InscripcionForm(request.POST)
        if form.is_valid():
            print("Formulario válido")  # Verificar si el formulario pasa las validaciones.
            inscripcion = form.save(commit=False)
            inscripcion.usuario_nombre = f"{request.user.nombre} {request.user.apellido1} {request.user.apellido2}"  # Nombre del usuario logueado.
            inscripcion.usuario_rut = request.user.rut  # Usar el RUT como username.
            inscripcion.dias = request.POST.get('dias')
            inscripcion.save()
            print("Inscripción guardada con éxito")  # Log para confirmar que se guardó la inscripción.
            return redirect('inscripcion_exitosa')
        else:
            print("Formulario no válido")  # Log para ver qué falla si el formulario no es válido.
            print("Errores del formulario:", form.errors)  # Log de errores del formulario.
    else:
        print("Método GET recibido")  # Saber si se está cargando el formulario inicialmente.
        form = InscripcionForm()

    return render(request, 'web/talleres/taller.html', {
        'form': form,
        'talleres': talleres,
        'usuario': request.user,
    })



def taller_inscripcion(request):
    talleres = Taller.objects.all()  # Obtener todos los talleres disponibles

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)  # No guardar aún en la base de datos
            inscripcion.usuario_nombre = f"{request.user.nombre} {request.user.apellido1} {request.user.apellido2}"  # Concatenar el nombre manualmente
            inscripcion.save()                    # Guarda la inscripción
            return redirect('inscripcion_exito')  # Redirige a una página de éxito
    else:
        form = InscripcionForm()
        
    usuario_logueado = Usuario.objects.get(id=request.user.id)

    return render(request, 'web/talleres/taller_inscripcion.html', {
        'form': form,
        'talleres': talleres,
        'usuario': request.user,  # Pasar el usuario logueado
    })

def inscripcion_exitosa(request):
    return render(request, 'web/talleres/inscripcion_exitosa.html')


def registro(request):
    if request.method == "POST":
        # Capturar datos
        rut = request.POST.get("rut")
        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        apellido1 = request.POST.get("apellido1")
        apellido2 = request.POST.get("apellido2")
        nacimiento = request.POST.get("nacimiento")
        telefono = request.POST.get("telefono")

        if Usuario.objects.filter(rut=rut).exists():
            messages.error(request, f"El RUT {rut} ya está registrado.")
        else:
            contraseña_inicial = rut[:5]
            usuario = Usuario(
                rut=rut,
                email=email,
                nombre=nombre,
                apellido1=apellido1,
                apellido2=apellido2,
                nacimiento=nacimiento,
                telefono=telefono,
                password=make_password(contraseña_inicial),
            )
            usuario.save()                  # Guarda la inscripción
            return redirect('bienvenida')

            messages.error(request, "Hubo un problema al autenticar al usuario.")
            return redirect('login')

    return render(request, 'web/Acceso/registro.html')

# Muni/paginaMuni/views.py
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Intentando autenticar: {email}")  # Mensaje de depuración
        usuario = authenticate(request, email=email, password=password)
        
        if usuario is not None:
            login(request, usuario)
            messages.success(request, f"¡Bienvenido, {usuario.nombre}!")
            return redirect('index')
        else:
            messages.error(request, "Email o contraseña incorrectos.")
            print("Autenticación fallida.")  # Mensaje de depuración

    return render(request, 'registration/login.html')


def mi_vista(request):
    # Código de la vista...
    return redirect(reverse('logout'))

def bienvenida(request):
    return render(request, 'web/bienvenida.html')

def perfil(request):
    return render(request, 'web/perfil.html')

def exit(request):
    logout(request)
    return redirect('index')