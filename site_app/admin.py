from django.contrib import admin
from django.contrib.auth.models import User

from .models import Contest, UserExtraData, UserImages, Votes, PictureContestRating


class UserExtraDataInLine(admin.TabularInline):
    model = UserExtraData


class UserModelAdmin(admin.ModelAdmin):
    inlines = [UserExtraDataInLine]
    fields = ['username', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login', 'date_joined']
    list_display = fields
    search_fields = fields


class UserExtraDataModelAdmin(admin.ModelAdmin):
    fields = ['user', 'phone_number', 'date_birth', 'rating']
    list_display = fields


class UserImagesModelAdmin(admin.ModelAdmin):
    fields = ['user', 'picture', 'date_uploaded']
    list_display = fields


class ContestModelAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'date_started', 'date_finished', 'active']
    list_display = fields


class PictureContestRatingModelAdmin(admin.ModelAdmin):
    fields = ['contest', 'picture', 'rating']
    list_display = fields


admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
admin.site.register(Contest, ContestModelAdmin)
admin.site.register(UserExtraData, UserExtraDataModelAdmin)
admin.site.register(UserImages, UserImagesModelAdmin)
admin.site.register(Votes)
admin.site.register(PictureContestRating, PictureContestRatingModelAdmin)
