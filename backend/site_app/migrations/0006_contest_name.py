# Generated by Django 4.0.1 on 2022-01-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0005_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
