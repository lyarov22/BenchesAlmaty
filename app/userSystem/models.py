from django.db import models
from django.contrib.auth.models import AbstractUser

# login system
class CustomUser(AbstractUser):
    # Добавьте здесь дополнительные поля, если необходимо
    email = models.EmailField(unique=True)
    # ваша дополнительная информация
    # ...
    
    USERNAME_FIELD = 'username'  # или любое другое поле, которое вы хотите использовать для входа
    pass



class Profile(models.Model):
    LEVEL_CHOICES = [
        (0, 'Пользователь'),
        (1, 'Активный пользователь'),
        (2, 'Эксперт'),
        (3, 'Лидер'),
        (4, 'Администрация⭐'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    surname = models.CharField(max_length=50, blank=True, default='')

    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='default.png', upload_to='user_avatars/', blank=True, null=True)

    level = models.IntegerField(default=0, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.user.username
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        # Здесь вы можете вернуть путь к изображению по умолчанию или другую логику по вашему выбору
        return '/media/default.png'
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.username
        super(Profile, self).save(*args, **kwargs)

