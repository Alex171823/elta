# Generated by Django 4.0.1 on 2022-01-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0012_remove_userextradata_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradata',
            name='date_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userextradata',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, verbose_name='Номер телефона'),
        ),
    ]
