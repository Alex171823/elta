from django.db import models
from django.contrib.auth.models import User


class UserExtraData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=13)
    date_birth = models.DateField(null=True)
    datetime_registered = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = 'Дельтовец'
        verbose_name_plural = 'Дельтовцы'
