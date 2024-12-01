from django.shortcuts import render, redirect
from .models import Usuario, Taller, Inscripcion
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .form import InscripcionForm

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
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            # Guardamos la inscripción con los datos del usuario logueado
            inscripcion = form.save(commit=False)
            inscripcion.usuario_nombre = request.user.get_full_name()  # O cualquier campo que desees mostrar
            inscripcion.usuario_rut = request.user.username  # Si tu 'RUT' es el nombre de usuario, o personalízalo
            inscripcion.save()
            return redirect('inscripcion_exitosa')  # Redirige a una página de confirmación
    else:
        form = InscripcionForm()

    return render(request, 'web/talleres/taller.html', {'form': form, 'usuario': request.user})

@login_required
def taller_inscripcion(request):
    # Consultamos todos los talleres disponibles
    talleres = Taller.objects.all()

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            # Guardar la inscripción
            form.save()
            return redirect('inscripcion_exito')  # Redirigir a una página de éxito
    else:
        form = InscripcionForm()

    return render(request, 'web/talleres/taller_inscripcion.html', {'form': form, 'talleres': talleres})

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
            usuario.save()

            # Enviar correo al usuario
            send_mail(
                subject="Bienvenido a la plataforma",
                message=f"Hola {nombre}, tu contraseña inicial es: {contraseña_inicial}.",
                from_email="no-reply@tu-sitio.com",
                recipient_list=[email],
            )
            messages.success(request, "Registro exitoso. Revisa tu correo para la contraseña.")
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

def exit(request):
    logout(request)
    return redirect('index')