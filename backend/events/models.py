from django.contrib.auth.models import User
from django.db import models


class UserEventNotificationSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_in_tg = models.BooleanField('Напоминать в Telegram', default=True, null=False)
    notify_by_email = models.BooleanField('Напоминать по email', default=True, null=False)

    class Meta:
        verbose_name = 'Настройка оповещений о новых мероприятиях'
        verbose_name_plural = 'Настройки оповещений о новых мероприятиях'

    def __str__(self):
        return f"{self.notify_in_tg} {self.notify_by_email}"


class Event(models.Model):
    description = models.CharField('Описание', max_length=255, null=False, blank=False)
    date_time_start = models.DateTimeField('Дата и время начала', null=True, blank=True)
    date_time_end = models.DateTimeField('Дата и время окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f"{self.description} {self.date_time_start} {self.date_time_end}"
