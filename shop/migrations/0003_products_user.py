# Generated by Django 3.1.4 on 2020-12-24 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('shop', '0002_auto_20201223_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.users', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
