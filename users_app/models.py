from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):
        if not email:
            raise ValueError('User must provide email.')
        if not user_name:
            raise ValueError('User must provide user name.')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, user_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            user_name=user_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.is_email_verified = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=30, unique=False, verbose_name='user name')
    first_name = models.CharField(max_length=30, unique=False, verbose_name='first name')
    last_name = models.CharField(max_length=30, unique=False, verbose_name='last name')
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')
    is_email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ['user_name', ]

    objects = MyUserManager()

    def __str__(self):
        return self.email
