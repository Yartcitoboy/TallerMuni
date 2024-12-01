from django.urls import path, include
from .views import index, taller, taller_inscripcion, registro, login_view, bienvenida, exit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='index'),
    path('taller',taller,name='taller'),
    path('inscripcion',taller_inscripcion, name='taller_inscripcion'),
    path('registro',registro,name='registro'),
    path('bienvenida', bienvenida,name='bienvenida'),
    path('login/',login_view,name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page=index), name='logout'),
    path('logout/', exit, name='exit'),
]
