from .base import *
import os
import dj_database_url


DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(', ')

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}


INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
] + CUSTOM_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_SSL_REDIRECT = True