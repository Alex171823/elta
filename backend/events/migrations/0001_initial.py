# Generated by Django 4.0.3 on 2022-05-14 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('date_time_start', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала')),
                ('date_time_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время окончания')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='UserEventNotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_in_tg', models.BooleanField(default=True, verbose_name='Напоминать в Telegram')),
                ('notify_by_email', models.BooleanField(default=True, verbose_name='Напоминать по email')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Настройка оповещений о новых мероприятиях',
                'verbose_name_plural': 'Настройки оповещений о новых мероприятиях',
            },
        ),
    ]
