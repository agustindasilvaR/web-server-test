from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Cambia related_name para evitar colisiones
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='user',
    )


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Cambia related_name para evitar colisiones
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='user',
    )
    
class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    fileName = models.CharField(max_length=255)
    fileType = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.fileName