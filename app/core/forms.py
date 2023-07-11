from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields, Form
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import *


# Definición de una clase de formulario personalizado para la autenticación de usuario
class MyAuthForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']  # Campos del formulario: nombre de usuario y contraseña

    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        # Personalización de los campos de nombre de usuario y contraseña del formulario
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'})
        self.fields['password'].label = False

# Definición de un formulario de registro de usuario
class UsuarioRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'type': 'password', 'name': 'password', 'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'type': 'password', 'name': 'password', 'placeholder': 'Password'}), label='',
        error_messages={
            'error_messages': 'padada',
            'invalid': 'fields format is not valid',
            'max_length': 'max_length is 30 chars',
            'min_length': 'password should be at least 8 Chars',
            'password_mismatch': 'The twdada.',
        })

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rut']  # Campos del formulario: nombre de usuario, correo electrónico, contraseñas y rut
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'rut': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
        error_messages_email = {
            'required': 'Ingrese un dato',
            'invalid': 'Formato invalido',
            'max_length': 'max length is 40 chars',
        }
        error_messages = {
            'required': 'please Fill-out this field',
            'invalid': 'fields format is not valid',
            'max_length': 'max_length is 30 chars',
            'min_length': 'password should be at least 8 Chars',
            'password_mismatch': ("The twoadadadada."),
        }

# Definición de un formulario para el modelo Producto
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id', 'nomprod', 'precio', 'imagen']  # Campos del formulario: ID, nombre, precio e imagen
