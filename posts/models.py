from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    comentario = models.TextField(blank=True)
    foto = models.ImageField(upload_to='posts/', blank=True, null=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post de {self.autor.username}'

