from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from PIL import Image

# login system
class CustomUser(AbstractUser):
    # Добавьте здесь дополнительные поля, если необходимо
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
    )


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='user_avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

