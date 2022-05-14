from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.datetime_safe import datetime

from site_app.models import Contest, UserImages


class Command(BaseCommand):
    help = 'Delete all pics, contests (and related data) older than 30 days'    # noqa A003

    def handle(self, *args, **options):
        # delete al pics older than 30 days
        UserImages.objects.filter(date_uploaded=datetime.today()-timedelta(days=30)).delete()

        # make certain contests inactive
        contests = (Contest.objects.filter(date_finished=datetime.today()))
        for contest in contests:
            contest.active = False
            contest.save()

        # delete contests older than 30 days
        Contest.objects.filter(date_finished=datetime.today()-timedelta(days=30)).delete()
