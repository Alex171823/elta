from django.contrib import admin
from .models import UserExtraData
from django.contrib.auth.models import User

admin.site.unregister(User)


class UserExtraDataInLine(admin.StackedInline):
    model = UserExtraData


class UserModelAdmin(admin.ModelAdmin):
    inlines = [UserExtraDataInLine]


admin.site.register(User, UserModelAdmin)
