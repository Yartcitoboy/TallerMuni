from django.core.management.base import BaseCommand
from paginaMuni.models import Taller, PAGINAMUNI_TALLER  # Reemplaza `app_name` con el nombre de tu aplicación

class Command(BaseCommand):
    help = "Transferir datos de Taller a PAGINAMUNI_TALLER"

    def handle(self, *args, **kwargs):
        for taller in Taller.objects.all():
            PAGINAMUNI_TALLER.objects.create(
                nombre=taller.nombre,
                descripcion=taller.descripcion,
                duracion=taller.duracion,
                instructor=taller.instructor
            )
        self.stdout.write(self.style.SUCCESS("Datos transferidos exitosamente."))
