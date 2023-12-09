from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from userSystem.models import CustomUser

class BenchType(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Тип скамейки')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    avatar = models.ImageField(default='default.png', upload_to='bench_type/', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип скамейки'
        verbose_name_plural = 'Тип скамеек'

    def __str__(self):
        return self.name
    

class BenchDistrict(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Район скамейки')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    avatar = models.ImageField(default='default.png', upload_to='bench_district/', blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Район скамейки'
        verbose_name_plural = 'Район скамеек'

    def __str__(self):
        return self.name


class BenchEnvironment(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Окружение скамейки')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    avatar = models.ImageField(default='default.png', upload_to='bench_environment/', blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Окружение скамейки'
        verbose_name_plural = 'Окружение скамеек'

    def __str__(self):
        return self.name


class Bench(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_latitude = models.FloatField(verbose_name="Широта")
    location_longitude = models.FloatField(verbose_name="Долгота")

    avatar = models.ImageField(default='noBenchImage.png', upload_to='bench_avatars/', blank=True, null=True)

    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)

    
    has_backrest = models.BooleanField(default=None, blank=True, null=True)
    has_bin = models.BooleanField(default=None, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    deskription = models.TextField(blank=True)

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор", default=CustomUser, editable=False)

    type = models.ForeignKey(BenchType, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(BenchDistrict, on_delete=models.CASCADE, blank=True, null=True)
    environment = models.ForeignKey(BenchEnvironment, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Скаймейка"
        verbose_name_plural = "Скаймейки"

    def __str__(self):
        return str(self.id)
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        # Здесь вы можете вернуть путь к изображению по умолчанию или другую логику по вашему выбору
        return '/media/default.png'
    
    def get_rating(self):
        rating = int(self.rating)

        return int(rating)
    
    def image_upload_to(instance, filename):
        return f'bench_images/{instance.bench.id}/avatar/{filename}'
    

class BenchImage(models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE, related_name='images')

    def image_upload_to(instance, filename):
        return f'bench_images/{instance.bench.id}/{filename}'
    
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Дополнительное фото', blank=True, null=True)

    def __str__(self):
        return f"{self.bench.id} Image"
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'