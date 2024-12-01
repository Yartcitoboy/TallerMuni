from django import forms
from .models import Usuario, Inscripcion, Taller

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginForm(forms.Form):
    # Cambié 'rut' a 'email'
    email = forms.EmailField(max_length=255, label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingrese su email'
    }))
    
    # El campo password no cambia, ya que aún pedimos la contraseña
    password = forms.CharField(max_length=5, label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Ingrese su contraseña'
    }))
    
class InscripcionForm(forms.ModelForm):
    taller = forms.ModelChoiceField(queryset=Taller.objects.all(), widget=forms.HiddenInput())
    nombre_participante = forms.CharField(max_length=100)
    rut_participante = forms.CharField(max_length=12)
    dia_seleccionado = forms.CharField(max_length=100)

    class Meta:
        model = Inscripcion
        fields = ['nombre_participante', 'rut_participante', 'taller', 'dia_seleccionado', 'confirmacion']