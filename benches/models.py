from django.db import models

class Bench(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_latitude = models.FloatField(verbose_name="Широта")
    location_longitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        verbose_name = "Скаймейка"
        verbose_name_plural = "Скаймейки"

    def __str__(self):
        return self.id