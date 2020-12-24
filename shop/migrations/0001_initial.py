# Generated by Django 3.1.4 on 2020-12-23 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзыв',
            },
        ),
    ]
