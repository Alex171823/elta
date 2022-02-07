from datetime import timedelta

from django.utils.datetime_safe import datetime

from site_app.models import Contest, UserImages

# delete al pics older than 30 days
UserImages.objects.filter(date_uploaded=datetime.today()-timedelta(days=30)).delete()

# make certain contests inactive
contests = (Contest.objects.filter(date_finished=datetime.today()))
for contest in contests:
    contest.active = False
    contest.save()

# delete contests older than 30 days
Contest.objects.filter(date_finished=datetime.today()-timedelta(days=30)).delete()
