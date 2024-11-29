from django import forms
from .models import Usuario

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