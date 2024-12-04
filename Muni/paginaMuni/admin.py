from django.contrib import admin
from .models import Usuario, Taller, Inscripcion
# Register your models here.
admin.site.register(Taller)
admin.site.register(Inscripcion)
admin.site.register(Usuario)