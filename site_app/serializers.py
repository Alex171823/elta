from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserExtraData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = ('password', )
        # fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'user_permissions',
        #           'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'extra_data')
