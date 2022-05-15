import os

from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from events.models import UserEventNotificationSettings

from site_app.models import UserExtraData, UserImages


# Creates UserExtraData, UserEventNotificationSettings tables for new user
@receiver(post_save, sender=User)
def auto_create_related_tables(sender, instance, created, **kwargs):
    if created:
        new_user_extra_data = UserExtraData(user=instance)
        new_user_extra_data.save()

        new_user_event_notifications_settings = UserEventNotificationSettings(user=instance)
        new_user_event_notifications_settings.save()


# Deletes file from filesystem when corresponding `UserImages` object is deleted.
@receiver(post_delete, sender=UserImages)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)
