# Generated by Django 4.2.7 on 2023-11-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_offers_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='files',
            field=models.FileField(upload_to='media/', verbose_name='Файлы'),
        ),
    ]
