"""
Django settings for AICI_WEB project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.core.exceptions import ImproperlyConfigured # for importing error
import os, json # for importing secret key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

## Import secret key from secrets.json
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open (secret_file) as f:
    secrets = json.load(f)

##  Get secret key or return error msg    
def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
SECRET_KEY = "django-insecure-*(coa&dad3uc@c9bl18==z5jpa0*0wbzd4e!g$k=ixk((af&o-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '52.78.234.62'] ## localhost and server IP


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users", ## USER
    "board",
    "construction",
    "voc",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "AICI_WEB.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [f'{BASE_DIR}/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "AICI_WEB.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

## connect with AWS RDS (MySQL)

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'OPTIONS': {
             'sql_mode': 'STRICT_TRANS_TABLES',
         },
         'NAME': get_secret("DB_NAME"),
         'USER': get_secret("DB_USER"),
         'PASSWORD': get_secret("DB_PWD"),
         'HOST': get_secret("DB_HOST"),
         'PORT': '3306', 
     }
}

## Custom User Backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

## Custom User class
AUTH_USER_MODEL = "users.EngineerTB"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr" ## Korean in admin page

TIME_ZONE = "Asia/Seoul" ## KST

USE_I18N = True

USE_TZ = False ## False to set KST in DB


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

## Set Static, Media URL/Root for nginx

# STATIC_URL = '/static/'
# STATIC_ROOT=os.path.join(BASE_DIR, 'static/')

STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR,'static'),

MEDIA_URL = 'media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


## Login / Logout redirect URL 
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/login/'

## Maintain Session in 1 hour
ACCOUNT_SESSION_REMEMBER = True
SESSION_COOKIE_AGE = 3600