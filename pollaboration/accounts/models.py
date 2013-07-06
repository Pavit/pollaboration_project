from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    date_of_birth = models.DateTimeField()
    gender = models.CharField()
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    #stuff from facebook
    fb_username = models.CharField(max_length=128, unique=False, blank=True)
    name = models.CharField(max_length=128, unique=False, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    locale = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    hometown = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    timezone = models.CharField(max_length=200, blank=True)
    relationship_status = models.CharField(max_length=200, blank=True)
    religion = models.CharField(max_length=200, blank=True)
    political = models.CharField(max_length=200, blank=True)
    fb_id = models.CharField(max_length=200, blank=True)
    fb_access_token = models.CharField(max_length=200, blank=True)
    friends = models.ManyToManyField('self')
    ####
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    agegroup = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=True)