# Generated by Django 4.0.1 on 2022-02-02 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0021_alter_contest_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.contest'),
        ),
    ]
