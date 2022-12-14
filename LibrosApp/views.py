#from typing_extensions import Self
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def inicio(request):
    return render(request, "LibrosApp/inicio.html")

@login_required
def buscarLibros(request):
    return render(request, "LibrosApp/buscar.html")

@login_required
def buscar(request):
    if request.GET["titulo"]:
        buscar = request.GET["titulo"]
        libros = Libros.objects.filter(nombreLibro__icontains=buscar)
        return render(request, "LibrosApp/resultados.html", {"libros":libros, "buscar":buscar})
    else:
        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)

def loginUsuario(request):
    if request.method == "POST":
        ingresar = MyAuthenticationForm(request, data = request.POST)
        if ingresar.is_valid():
            usuario = ingresar.cleaned_data.get("username")
            contra = ingresar.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, "LibrosApp/inicio.html",{"mensaje":f"hola {user}"})
        else:
            return render(request, "LibrosApp/inicio.html",{"mensaje":f"Datos incorrectos"})
    else:
        ingresar = MyAuthenticationForm()
    return render(request, "LibrosApp/login.html",{"ingresar":ingresar})

def register(request):
    if request.method == "POST":
        registrar = RegistroForm(request.POST)
        if registrar.is_valid():
            nombreUsuario = registrar.cleaned_data["username"]
            registrar.save()
            messages.success(request, f'Usuario {nombreUsuario} creado')
            return render(request, "LibrosApp/inicio.html",{"mensaje":f"Usuario {nombreUsuario} creado!!"})
    else:
        registrar = RegistroForm()
    return render(request, "LibrosApp/registro.html",{"registrar":registrar})

@login_required
def editarUsuario(request):
    userConect = request.user
    if request.method == "POST":
        usuarioForm = EditarUsuarioForm(request.POST)
        if usuarioForm.is_valid():
            info = usuarioForm.cleaned_data
            userConect.username = info["username"]
            userConect.email = info["email"]
            userConect.password1 = info["password1"]
            userConect.password2 = info["password2"]
            userConect.save()
            return render(request, "LibrosApp/inicio.html")
    else:
        usuarioForm = EditarUsuarioForm(initial={"email": userConect.email})
    return render(request, "LibrosApp/editarusuario.html", {"userEdit":usuarioForm, "userOn":userConect})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        avatarForm = AvatarFormulario(request.POST, request.FILES)
        if avatarForm.is_valid():
            info = avatarForm.cleaned_data
            avatar = Avatar(user=request.user, imagen=info['imagen'])
            avatar.save()
            return render(request, "LibrosApp/perfil.html")
    else:
        avatarForm = AvatarFormulario()
    return render(request, "LibrosApp/avatar.html",{'avatarForm':avatarForm})

@login_required
def perfil(request):
    return render(request, "LibrosApp/perfil.html")

@login_required
def posts(request):
    posts = Libros.objects.all()
    context = {"posts":posts}
    return render(request, "LibrosApp/libros.html", context)

@login_required
def postear(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        posteo = LibrosForm(request.POST, request.FILES)
        if posteo.is_valid():
            post = posteo.save(commit=False)
            post.user = current_user
            posteo.save()
            messages.success(request, "Publicaci??n enviado con ??xito")
            return render(request, "LibrosApp/padre.html")
    else:
        posteo = LibrosForm()
    return render(request,"LibrosApp/formulario.html",{"posteo":posteo})

@login_required
def editarPost(request, Posteo):
    editar = Libros.objects.get(nombreLibro = Posteo)
    if request.method == "POST":
        postEditar = LibrosForm(request.POST, request.FILES)
        if postEditar.is_valid():
            info = postEditar.cleaned_data
            editar.imagen = info["imagen"]
            editar.nombreLibro = info["nombreLibro"]
            editar.genero = info["genero"]
            editar.anio = info["anio"]
            editar.descripcion = info["descripcion"]
            editar.save()
            messages.success(request, "Publicaci??n editada con ??xito")
            return render(request, "LibrosApp/libros.html")
    else:
        postEditar = LibrosForm(initial={"imagen": editar.imagen, "nombreLibro": editar.nombreLibro, "genero": editar.genero, "anio": editar.anio, "descripcion": editar.descripcion})
    return render(request, "LibrosApp/editarlibros.html", {"editar":postEditar, "nombre":Posteo})

@login_required
def eliminarPost(request, Posteo):
    eliminar = Libros.objects.get(nombreLibro = Posteo)
    eliminar.delete()
    nombreLibros = Libros.objects.all()
    contexto = {"nombreLibros":nombreLibros}
    return render(request, "LibrosApp/inicio.html", contexto)

class detalleLibro(LoginRequiredMixin, DetailView):
    model = Libros
    context_object_name = 'verlibro'
    template_name = 'LibrosApp/detallelibro.html'

