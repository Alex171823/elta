# Generated by Django 4.0.1 on 2022-01-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0006_contest_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
