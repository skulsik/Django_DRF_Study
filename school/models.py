import datetime

from django.db import models

from config import settings
from services.utils import NULLABLE


class Course(models.Model):
    """ Модель курса """
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='school/', verbose_name='Превью(картинка)', **NULLABLE)
    description = models.CharField(max_length=1000, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Признак отображения')

    def __str__(self):
        return f'Объект Lesson: {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    """ Модель платежа """
    user = models.CharField(max_length=100, verbose_name='Пользователь')
    date_pay = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата платежа')

    name_of_payment_list: list = [
        ('course', 'Курс'),
        ('lesson', 'Урок'),
    ]
    name_of_payment = models.CharField(
        max_length=6,
        choices=name_of_payment_list,
        default='lesson',
        verbose_name='Оплаченный курс или урок'
    )

    payment_amount = models.PositiveIntegerField(default=0, verbose_name='Сумма оплаты')

    payment_method_list: list = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(
        max_length=8,
        choices=payment_method_list,
        default='transfer',
        verbose_name='Способ оплаты'
    )
    is_active = models.BooleanField(default=True, verbose_name='Признак отображения')

    def __str__(self):
        return f'Объект Payments: {self.user}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
