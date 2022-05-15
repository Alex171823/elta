# Generated by Django 4.0.1 on 2022-01-31 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_app', '0019_alter_picturecontestrating_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]