# Generated by Django 4.0.1 on 2022-01-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0010_alter_userextradata_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradata',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='pictures/avatars', verbose_name='Аватарка'),
        ),
    ]
