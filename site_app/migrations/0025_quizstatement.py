# Generated by Django 4.0.3 on 2022-03-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0024_alter_picturecontestrating_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_statement', models.CharField(max_length=255)),
                ('wrong_statement', models.CharField(max_length=255)),
                ('explanation', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
