# Generated by Django 4.2 on 2023-12-07 12:46

import benches.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benches', '0007_alter_bench_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=benches.models.BenchImage.image_upload_to, verbose_name='Дополнительное фото'),
        ),
    ]