from django.db import models

from user.models import Users


class Products(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    number = models.IntegerField(verbose_name='Номер')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

    def __str__(self):
        return self.user.email


class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
