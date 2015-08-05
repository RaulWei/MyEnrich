"""
Django settings for myenrich project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# sae need
# import os.path
# import sae.const
# from os import environ
#
# MYSQL_DB = sae.const.MYSQL_DB
# MYSQL_USER = sae.const.MYSQL_USER
# MYSQL_PASS = sae.const.MYSQL_PASS
# MYSQL_HOST_M = sae.const.MYSQL_HOST
# MYSQL_HOST_S = sae.const.MYSQL_HOST_S
# MYSQL_PORT = sae.const.MYSQL_PORT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^8i63c0=z07b5_0zni21aw@u(4(xa+b(na^3di^35)2%65hkj%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'enrich',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myenrich.urls'

WSGI_APPLICATION = 'myenrich.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # local mysql
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'myenrich',
        #'USER': 'root',
        #'PASSWORD': '',
        #'HOST': '',
        #'PORT': '3306',

        # sae mysql
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': MYSQL_DB,
        # 'USER': MYSQL_USER,
        # 'PASSWORD': MYSQL_PASS,
        # 'HOST': MYSQL_HOST_M,
        # 'PORT': MYSQL_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("javascript", os.path.join(STATIC_ROOT, 'javascript')),
    ("img", os.path.join(STATIC_ROOT, 'img')),
)
