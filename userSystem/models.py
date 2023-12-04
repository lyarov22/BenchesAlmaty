from django.db import models
from django.contrib.auth.models import AbstractUser

# login system
class CustomUser(AbstractUser):
    # Добавьте здесь дополнительные поля, если необходимо
    pass



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='default.png', upload_to='user_avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

