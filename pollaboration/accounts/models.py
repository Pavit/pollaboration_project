from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, gender, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, gender, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            gender=gender,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    date_of_birth = models.DateField()
    gender = models.CharField()
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender','date_of_birth']
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
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

    def get_full_name(self):
    # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
    # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.email