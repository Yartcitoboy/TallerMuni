from django.urls import path, include
from .views import index, talleres, registro, login_view, bienvenida
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='index'),
    path('talleres',talleres,name='talleres'),
    path('registro',registro,name='registro'),
    path('bienvenida', bienvenida,name='bienvenida'),
    path('login',login_view,name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page=index), name='logout'),
]
