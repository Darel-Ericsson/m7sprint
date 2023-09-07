from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password1', 'password2'
        ]
        labels = {
            'username' : 'Usuario',
            'first_name' : 'Nombres',
            'last_name' : 'Apellidos',
            'password' : 'Contraseña',
            'password2' : 'Repetir Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ej: JuanPedro1718'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ej: Juan Pedro'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ej: Pérez Machuca'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'})
        }

        help_texts = {
            'username' : 'Debe contener letras, números y @.',
            'password1': 'Ingrese su contraseña.',
            'password2': 'Vuelva a ingresar su contraseña.',
        }
