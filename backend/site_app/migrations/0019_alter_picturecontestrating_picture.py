# Generated by Django 4.0.1 on 2022-01-28 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0018_rename_date_time_uploaded_userimages_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturecontestrating',
            name='picture',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='site_app.userimages'),
        ),
    ]