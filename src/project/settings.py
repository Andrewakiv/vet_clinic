"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import logging
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
 '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vet_clinic.apps.VetClinicConfig',
    'accounts.apps.AccountsConfig',
    'phonenumber_field',
    'pet_care_scheduler.apps.PetCareSchedulerConfig',
    'actions.apps.ActionsConfig',
    'blog.apps.BlogConfig',
    'debug_toolbar'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'main_formatter': {
            'format': "{asctime} - {levelname} - {module} - {message}",
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter'
        },
        'vet_clinic_file': {
            'class': 'logging.FileHandler',
            'filename': 'vet_clinic_info.log',
            'formatter': 'main_formatter'
        },
        'accounts_file': {
            'class': 'logging.FileHandler',
            'filename': 'accounts_info.log',
            'formatter': 'main_formatter'
        },
        'pet_care_scheduler_file': {
            'class': 'logging.FileHandler',
            'filename': 'pet_care_scheduler_info.log',
            'formatter': 'main_formatter'
        },
        'blog_file': {
            'class': 'logging.FileHandler',
            'filename': 'blog_info.log',
            'formatter': 'main_formatter'
        }
    },
    'loggers': {
        'vet_clinic': {
            'handlers': ['console', 'vet_clinic_file'],
            'propagate': True,
            'level': 'INFO'
        },
        'accounts': {
            'handlers': ['console', 'accounts_file'],
            'propagate': True,
            'level': 'INFO'
        },
        'pet_care_scheduler': {
            'handlers': ['console', 'pet_care_scheduler_file'],
            'propagate': True,
            'level': 'INFO'
        },
        'blog': {
            'handlers': ['console', 'blog_file'],
            'propagate': True,
            'level': 'INFO'
        }
    }
}


ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'vet_clinic.context_processors.get_mainmenu',
                'vet_clinic.context_processors.get_footer_nav',
                'vet_clinic.context_processors.get_footer_quick_links',
                'vet_clinic.context_processors.get_support',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("POSTGRES_DB"),
        'USER': config("POSTGRES_USER"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'PORT': config("POSTGRES_PORT"),
        'HOST': config("POSTGRES_HOST"),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'auth.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_USER_IMAGE = MEDIA_URL+'services/default_service.png'
DEFAULT_PROFILE_IMAGE = MEDIA_URL+'accounts/default_profile.jpg'

LOGIN_REDIRECT_URL = 'vet_clinic:home'
LOGIN_URL = 'accounts:login'  # must create LoginUserView(LoginView) to use it or use accounts/registration/login.html
# LOGOUT_REDIRECT_URL = 'accounts:logout'
LOGOUT_URL = 'accounts:logout'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
]

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_DB = config('REDIS_DB')

# try:
#     from .local_settings import *
# except ImportError:
#     pass
