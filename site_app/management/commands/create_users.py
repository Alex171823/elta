from random import randint

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

from site_app.models import UserExtraData

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fill database with 500 fake users
    def handle(self, *args, **kwargs):
        # clear database
        # User.objects.all().delete()
        # UserExtraData.objects.all().delete()

        # create 500 users
        self.stdout.write('Creating users')
        users = []
        for i in range(1, 500):
            name = fake.name()
            username = name.split(' ')[0].lower() + '_' + str(randint(0, 5000))
            users.append(User(username=username,
                              first_name=name.split(' ')[0],
                              last_name=name.split(' ')[1],
                              email=username + '@mail.org',
                              password=make_password(fake.password()),
                              is_staff=0,
                              is_active=randint(0, 1),
                              is_superuser=0))
            self.stdout.write(f'user {i} created')
        self.stdout.write('adding users to db...')
        User.objects.bulk_create(users)

        # create up to 10 posts for each user
        self.stdout.write('Creating extra data')
        extra_data = []
        for user in User.objects.all():
            extra_data.append(UserExtraData(user=user,
                                            avatar=f'./{user.username}',
                                            phone_number=f'+3806855555{randint(10, 100)}',
                                            rating=randint(0, 11)))
        UserExtraData.objects.bulk_create(extra_data)
        self.stdout.write('data added')
