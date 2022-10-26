from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", default='', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='', null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Libros(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    nombreLibro = models.CharField(max_length=60,null=True, blank=True)
    autor = models.CharField(max_length=60,null=True, blank=True)
    capitulos = models.IntegerField()
    genero = models.CharField(max_length=60,null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "libros"
        verbose_name_plural = "libross"
    def __str__(self):
        return f'{self.user.username}: {self.nombreLibro}: {self.genero}'

class Comentar(models.Model):
    comentario = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name='comentarios', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario', null=True)
    imagen = models.ImageField(default='', null=True, blank=True)
    timecoment = models.DateTimeField(default=timezone.now)
    mensaje = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-timecoment']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f'{self.user.username}'
