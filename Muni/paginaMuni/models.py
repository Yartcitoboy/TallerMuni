from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, rut, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        usuario = self.model(email=email, rut=rut, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, rut, password, **extra_fields)

class Usuario(AbstractBaseUser):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    nacimiento = models.DateField()
    email = models.EmailField(max_length=120, unique=True)
    telefono = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre']

    objects = UsuarioManager()

    def __str__(self):
        return self.email
    
class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    usuario_nombre = models.CharField(max_length=100)
    usuario_rut = models.CharField(max_length=20)
    dias_seleccionado = models.CharField(max_length=255)  # Puedes usar un campo de texto para almacenar los días seleccionados
    confirmacion = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario_nombre} - {self.taller.nombre}"