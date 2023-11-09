from django.db import models

class Offers( models.Model):
    name = models.CharField('Имя', max_length=100)
    number = models.CharField('Телефон', max_length=12)
    mail = models.CharField('Почта', max_length=100)
    social_nets = models.CharField("Соц.Сети", max_length=127)
    description = models.TextField("Описание")
    files = models.FileField("Файлы", upload_to='uploads/')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name="Предложение"
        verbose_name_plural="Предложения"