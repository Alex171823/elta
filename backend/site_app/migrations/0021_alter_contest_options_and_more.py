# Generated by Django 4.0.1 on 2022-02-02 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0020_alter_votes_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contest',
            options={'verbose_name': 'Конкурс', 'verbose_name_plural': 'Конкурсы'},
        ),
        migrations.AlterModelOptions(
            name='picturecontestrating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterModelOptions(
            name='userimages',
            options={'verbose_name': 'Пользовательское изображение', 'verbose_name_plural': 'Изображения пользователей'},
        ),
        migrations.AlterModelOptions(
            name='votes',
            options={'verbose_name': 'Голосование', 'verbose_name_plural': 'Голосования'},
        ),
    ]