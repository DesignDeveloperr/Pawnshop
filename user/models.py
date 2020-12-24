from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return self.email
