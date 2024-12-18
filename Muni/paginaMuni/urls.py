from django.urls import path, include
from .views import index, taller, perfil, taller_inscripcion, registro, login_view, bienvenida, exit, inscripcion_exitosa, crearTaller, tallerCreado
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='index'),
    path('taller',taller,name='taller'),
    path('inscripcion',taller_inscripcion, name='taller_inscripcion'),
    path('crearTaller', crearTaller, name='crearTaller'),
    path('tallerCreado', tallerCreado, name='tallerCreado'),
    path('perfil', perfil, name='perfil'),
    path('registro',registro,name='registro'),
    path('bienvenida', bienvenida,name='bienvenida'),
    path('inscripcion-exitosa', inscripcion_exitosa, name='inscripcion_exitosa'),
    path('login/',login_view,name='login'),
    path('logout/', exit, name='exit'),
]
