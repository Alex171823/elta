# Generated by Django 4.0.1 on 2022-01-19 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_app', '0002_remove_userextradata_datetime_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextradata',
            name='date_birth',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userextradata',
            name='phone_number',
            field=models.CharField(max_length=13, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='userextradata',
            name='rating',
            field=models.IntegerField(blank=True, default=0, verbose_name='Рейтинг'),
        ),
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='pictures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
