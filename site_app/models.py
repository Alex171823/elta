from django.db import models
from django.contrib.auth.models import User


class UserExtraData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=13)
    date_birth = models.DateField("Дата рождения", null=True)
    rating = models.IntegerField("Рейтинг", blank=True, default=0)

    class Meta:
        verbose_name = 'Дельтовец'
        verbose_name_plural = 'Дельтовцы'
