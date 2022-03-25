import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class UserExtraData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField("Номер телефона", max_length=13, blank=True)
    date_birth = models.DateField("Дата рождения", null=True, blank=True)
    rating = models.IntegerField("Рейтинг", blank=True, default=0)

    class Meta:
        verbose_name = 'Дельтовец'
        verbose_name_plural = 'Дельтовцы'

    def __str__(self):
        return f"{self.user} {self.phone_number} {self.date_birth} {self.rating}"


# OVERWRITE DELETE METHOD
class UserImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures')
    date_uploaded = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Пользовательское изображение'
        verbose_name_plural = 'Изображения пользователей'

    def __str__(self):
        return f"{self.user} {self.picture} {self.date_uploaded}"


@receiver(models.signals.post_delete, sender=UserImages)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UserImages` object is deleted.
    """
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


class Contest(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, blank=True)
    description = models.CharField(max_length=255)
    pictures = models.ManyToManyField(UserImages, blank=True)
    date_started = models.DateField(auto_now=True)
    date_finished = models.DateField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'

    def __str__(self):
        return f"{self.name} {self.users} {self.description} {self.pictures}"


class Votes(models.Model):
    # Changed to fk
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    votes_left = models.IntegerField(default=3)

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return f"{self.user} {self.contest} {self.votes_left}"


class PictureContestRating(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    picture = models.ForeignKey(UserImages, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f"{self.contest} {self.picture} {self.rating}"


class QuizStatement(models.Model):
    correct_statement = models.CharField(max_length=255, blank=False)
    wrong_statement = models.CharField(max_length=255, blank=False)
    explanation = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f"{self.correct_statement} {self.wrong_statement} {self.explanation}"
