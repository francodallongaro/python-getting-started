"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
# from boto.s3.connection import OrdinaryCallingFormat
# from storages.backends.s3boto import S3BotoStorage
# import dj_database_url
# from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = Path(__file__).resolve().parent.parent



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "jhsfcnakjaskndsjjsncjanksncjzbchzxblSdvndhrbfsucnxvbhx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    "storages",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "hello",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gettingstarted.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "gettingstarted.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# if DEBUG == True:

#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

# else:

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.postgresql",
        "NAME": "demo_1",
        "USER": "idealdatabase",
        "PASSWORD": "2IdealServicios",
        "HOST": "database-1.c8xhkoscqibi.us-east-2.rds.amazonaws.com",
        "PORT": "5432",
    }
}



# import dj_database_url
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# DATABASES = {
#     'default': dj_database_url.config()
# }

# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'sample123',
#             'USER': 'suresh',
#             'PASSWORD': '',
#             'HOST': 'localhost',
#             'PORT': '',
#         }
# }
# # dj-database-url settings
# # Update database configuration with $DATABASE_URL.
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/




# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG == True:

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    django_heroku.settings(locals())

else:

    AWS_ACCESS_KEY_ID = 'AKIA2AAJQQ3Z4JGGRJXW'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'ideal-bucket'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = 'hello.storage_backends.MediaStorage'

    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'hello.storage_backends.StaticStorage'

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    django_heroku.settings(locals(), staticfiles=False)
