from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Avatar, Libros

class RegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Ingrese un correo"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"eform","placeholder":"Ingrese una contraseña"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"eform","placeholder":"Repita la contraseña"}), label="")
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["username"].widget.attrs.update({"class":"eform","placeholder":"Nombre"})
        self.fields["username"].help_text = None

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Ingrese un correo"}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"eform","placeholder":"Ingrese una contraseña"}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"eform","placeholder":"Repita la contraseña"}), label="")
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields['username'].widget = forms.widgets.TextInput(attrs={"class":"eform",'placeholder': 'Nombre'})
        self.fields['username'].help_text = None

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["imagen"].label = ""
        self.fields["imagen"].help_text = None

class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields['username'].widget = forms.widgets.TextInput(attrs={"class":"eform",'placeholder': 'Nombre'})
        self.fields["password"].label = ""
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={"class":"eform",'placeholder': 'Contraseña'})

class LibrosForm(forms.ModelForm):
    nombreLibro = forms.CharField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Título"}), label="")
    genero = forms.CharField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Genero"}), label="")
    anio = forms.CharField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Año de creacion"}), label="")
    autor = forms.CharField(widget=forms.TextInput(attrs={"class":"eform","placeholder":"Autor"}), label="")
    capitulos = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"eform","placeholder":"Capitulos"}), label="")
    descripcion = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":2, "class":"eform","placeholder":"Escribe aquí una descripción o escritura"}), required=True)
    imagen = forms.URLField(widget=forms.URLInput(attrs={"class":"eform","placeholder":"URL de tu imagen"}), label="")

    class Meta:
        model = Libros
        fields = ["nombreLibro", "autor","genero", "capitulos", "anio", "descripcion", "imagen"]

