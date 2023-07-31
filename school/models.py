from django.db import models

from services.utils import NULLABLE


class Course(models.Model):
    """ Модель курса """
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='school/', verbose_name='Превью(картинка)', **NULLABLE)
    description = models.CharField(max_length=1000, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Признак отображения')

    def __str__(self):
        return f'Объект Course:{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """ Модель урока """
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='school/', verbose_name='Превью(картинка)', **NULLABLE)
    description = models.CharField(max_length=1000, verbose_name='Описание')
    url = models.URLField(max_length=255, verbose_name='Ссылка на видео')
    is_active = models.BooleanField(default=True, verbose_name='Признак отображения')

    def __str__(self):
        return f'Объект Lesson: {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
