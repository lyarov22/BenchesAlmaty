# Generated by Django 4.2 on 2023-12-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benches', '0002_alter_benchimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchimage',
            name='image',
            field=models.ImageField(upload_to='bench/%Y/%m/%d/', verbose_name='Дополнительное фото'),
        ),
    ]
