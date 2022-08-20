from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class CustomRegisterSerializer(RegisterSerializer): # noqa
    username = None
    user_name = serializers.CharField(max_length=30, allow_blank=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.user_name = self.data.get('user_name')
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.is_active = True
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer): # noqa
    username = None
