from django.contrib import admin
from django.contrib.auth.models import User

from .models import Contest, UserExtraData


class UserExtraDataInLine(admin.StackedInline):
    model = UserExtraData


class UserModelAdmin(admin.ModelAdmin):
    inlines = [UserExtraDataInLine]


admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
admin.site.register(Contest)
