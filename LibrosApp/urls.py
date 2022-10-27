from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name = "inicio"),
    path("buscar/", buscarLibros, name = "buscar"),
    path("resultados/", buscar, name = "Resultado"),
    path("login/", loginUsuario, name = "login"),
    path("register/", register, name = "register"),
    path("logout", LogoutView.as_view(template_name="LibrosApp/inicio.html"), name = "salir"),
    path("editarUsuario/", editarUsuario, name = "editUser"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar/"),
    path("perfil/", perfil, name = "perfill"),
    path('detallePost/<int:pk>/', detallePost.as_view(), name='detallePost'),
    path('detallePost/<int:pk>/comentar/', ComentarioPagina.as_view(), name='comentario'),
    
    #CRUD
    path("libros/", posts, name = "libros"),
    path("librosposts/", postear, name = "librosposts"),
    path("editarlibro/<Posteo>", editarPost, name = "editarlibro"),
    path("eliminarlibro/<Posteo>", eliminarPost, name = "eliminarlibro"),
]