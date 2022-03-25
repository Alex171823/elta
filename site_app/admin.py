from django.contrib import admin

from .models import Contest, PictureContestRating, UserExtraData, UserImages, Votes, QuizStatement


class UserExtraDataInLine(admin.TabularInline):
    model = UserExtraData


class UserExtraDataModelAdmin(admin.ModelAdmin):
    fields = ['user', 'phone_number', 'date_birth', 'rating']
    list_display = fields


class UserImagesModelAdmin(admin.ModelAdmin):
    fields = ['user', 'picture']
    search_fields = ['picture', 'user__username']
    list_display = fields


class ContestModelAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'active']
    list_display = fields


class PictureContestRatingModelAdmin(admin.ModelAdmin):
    fields = ['contest', 'picture', 'rating']
    list_display = fields


admin.site.register(Contest)
admin.site.register(UserExtraData, UserExtraDataModelAdmin)
admin.site.register(UserImages, UserImagesModelAdmin)
admin.site.register(Votes)
admin.site.register(PictureContestRating, PictureContestRatingModelAdmin)
admin.site.register(QuizStatement)