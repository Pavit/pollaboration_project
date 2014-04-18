from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from facepy import GraphAPI
from datetime import date, datetime


class MyUserManager(BaseUserManager):
    def create_user(self, email, gender, date_of_birth=None, password=None, fb_id=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
            date_of_birth=date_of_birth,
        )
        if fb_id is None:
            user.set_password(password)
        else:
            user.set_password(self.make_random_password(length=10))
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
    REQUIRED_FIELDS = ['gender']
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
    fb_access_token = models.CharField(max_length=500, blank=True)
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

    def populate_graph_info(self):
        graphinfo = GraphAPI(self.fb_access_token).get('me/')
        print graphinfo
        if "id" in graphinfo: self.fb_id = graphinfo["id"]
        if "username" in graphinfo: self.fb_username = graphinfo["username"]
        if "name" in graphinfo: self.name = graphinfo["name"]
        if "first_name" in graphinfo: self.first_name = graphinfo["first_name"]
        if "last_name" in graphinfo: self.last_name = graphinfo["last_name"]
        if "gender" in graphinfo: self.gender = graphinfo["gender"]
        if "email" in graphinfo: self.email = graphinfo["email"]
        if "birthday" in graphinfo:
            self.date_of_birth = datetime.strptime(graphinfo["birthday"], "%m/%d/%Y")
            today = date.today()
            self.age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or today.month == self.date_of_birth.month and today.day < self.date_of_birth.day:
                self.age -= 1
            self.agegroup = ">56"
            if self.age<56:  self.agegroup="46-55"
            if self.age<46:  self.agegroup="36-45"
            if self.age<36:  self.agegroup="26-35"
            if self.age<26:  self.agegroup="16-25"
            if self.age<16:  self.agegroup="<15"
        if "timezone" in graphinfo: self.timezone = graphinfo["timezone"]
        if "hometown" in graphinfo: self.hometown = graphinfo["hometown"]
        if "location" in graphinfo: self.location = graphinfo["location"]
        if "locale" in graphinfo: self.locale = graphinfo["locale"]
        if "relationship_status" in graphinfo: self.relationship_status = graphinfo["relationship_status"]
        if "religion" in graphinfo: self.religion = graphinfo["religion"]
        if "political" in graphinfo: self.political = graphinfo["political"]
        self.save()
        return self

    def check_friends(self):
        frienddict = GraphAPI(self.fb_access_token).get('me/friends')["data"]
        #check if user's friends are already members of the site
        user_fb_ids = MyUser.objects.values_list('fb_id', flat=True).order_by('fb_id')
        friend_fb_ids = []
        for friend in frienddict:
            friend_fb_ids.append(friend["id"])
            matches = MyUser.objects.filter(fb_id__in=friend_fb_ids)
        if matches.exists():
            for match in matches:
                if self.friends.filter(fb_id=match).exists():
                    pass
                else:
                    self.friends.add(match)
        self.save()
        return self