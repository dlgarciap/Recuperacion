from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    departamento = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Agregar related_name único para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuario_personalizado_set',  # ← NOMBRE ÚNICO
        related_query_name='usuario_personalizado',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuario_personalizado_set',  # ← NOMBRE ÚNICO
        related_query_name='usuario_personalizado',
    )

    def __str__(self):
        return f"{self.username} - {self.email}"