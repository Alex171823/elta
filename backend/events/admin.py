from django.contrib import admin

from events.models import Event, UserEventNotificationSettings

admin.site.register(UserEventNotificationSettings)
admin.site.register(Event)
