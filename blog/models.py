from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def approved_comments(self):
        return self.comments.filter(comentario_aprobado=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def aprobar(self):
        self.comentario_aprobado = True
        self.save()

    def __str__(self):
        return self.texto
