"""
Django settings for access_hack project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)
# print "BASE_DIR: {}".format(BASE_DIR)
# print "REPOSITORY_ROOT: {}".format(REPOSITORY_ROOT)

from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg ="Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6-io+#b4d0=gsm*z3%fjkix0@s^=tpv4ou70$npfgqsyqcsh98'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sass_processor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'access_hack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'planner/templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'access_hack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

'''
IMPORTANT - Replace values for secret key, name, user, password with get_env_variable("[PROJECT]_DB_NAME"), etc
We set those values at the bottom of the venv/bin/activate file (which is not stored in the repo).

export CBE_SECRET_KEY='[the one generated by django-admin]'
export PROJECT_DB_NAME='my_dbname'
export PROJECT_DB_USER='my_dbuser'
export PROJECT_DB_PASSWORD='my_dbpassword'

Then below we use get_env_variable("PROJECT_DB_NAME") etc

Unrelatedly, we also will define which settings file is used in venv/bin/activate as well:

export DJANGO_SETTINGS_MODULE='my_project.settings.local'

'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'access_hack',
        'USER': 'access_user',
        'PASSWORD': 'floweryacht7890&*()',
        'HOST': 'localhost',
        'PORT': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Settings

SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))
print "SETTINGS_PATH: {}".format(SETTINGS_PATH)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR + '/static/',
    BASE_DIR + "/static/js/",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
)

# Where it's going to save the compiled css file. It creates a dir called scss on its own.
SASS_PROCESSOR_ROOT = BASE_DIR + "/static/css/"
LIBSASS_SOURCE_COMMENTS = False

SASS_PROCESSOR_INCLUDE_DIRS = (
    os.path.join(BASE_DIR, 'static/scss'),
)

# LOGIN_URL = '/login/'
