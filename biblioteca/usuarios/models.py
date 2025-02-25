from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    LEITOR = 'leitor'
    WRITER = 'writer'

    TIPOS_USUARIO = [
        (LEITOR, 'Leitor'),
        (WRITER, 'Writer'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPOS_USUARIO, default=LEITOR)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios_set",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_set",
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.tipo})"
