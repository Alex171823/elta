# Generated by Django 4.0.1 on 2022-01-28 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_app', '0014_alter_contest_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
