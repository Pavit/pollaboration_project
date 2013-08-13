# Django settings for pollaboration project.
from os.path import abspath, basename, dirname, join, normpath
from sys import path
import os


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
ROOT_PATH = os.path.dirname(__file__)
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import dj_database_url
if not os.environ.get("HEROKU_DEV", False):  ### DB SETTINGS (LOCAL AND LOCAL W/ HEROKU) AND LOCAL FACEBOOK INFO
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'pollaboration',
    #         'USER': 'django_login',
    #         'PASSWORD': 'django',
    #         'HOST': '',
    #         'PORT': '', 
    #     }   
    # }
    # Below are the connections settings for using the heroku DB when working locally
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddai7at32sf8tc',
        'HOST': 'ec2-107-20-201-165.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'bfhsmrupkooooh',
        'PASSWORD': 'oJ3qQPaL6K0m0rbc8cvev-2aNH'
        }
    }
    FACEBOOK_APP_ID = '343120432448964'
    FACEBOOK_API_SECRET  = 'f43073165e02ef728f31a315cd9fa6de'
else:
    # HEROKU DATABASE SETTINGS / FACEBOOK INFO
    DATABASES = {'default': dj_database_url.config()}
    FACEBOOK_APP_ID = '167104050141535'
    FACEBOOK_API_SECRET  = '289643c70a9e00dafa68505e848244ea'
    
FACEBOOK_SCOPE = 'email,user_birthday,user_hometown,user_location,user_questions,user_relationships,user_religion_politics'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'pollaboration/static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$hvl&!2(w+n&7u6ez#_m0_j&cul^x0_x!(g%yb8ox3z4i+i@7z'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pollaboration.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pollaboration.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,"pollaboration/templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'accounts',
    'questions',
    'south',
    'facepy',
)
AUTH_USER_MODEL = 'accounts.MyUser'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
LOGOUT_URL = '/accounts/logout/'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
