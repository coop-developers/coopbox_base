"""
Django settings for coopbox_base project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a+lpjdgr#p=ep9hs0^%02)%e-%-ty50m3ijt=*(e8x++*ixgl$'

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

# XXX: make the following automatically load from db or settings file
    'coopbox_base',
    
    'filer',
    'mptt',
    'easy_thumbnails',
    'calendarium',

# XXX: end above
)

MIGRATION_MODULES = {
    'filer': 'filer.migrations_django',
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'coopbox_base.urls'

WSGI_APPLICATION = 'coopbox_base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Django-jinja settings
TEMPLATE_LOADERS = (
    'coopbox_base.util.template_loader.AppLoader',
    'coopbox_base.util.template_loader.FileSystemLoader',
)

INSTALLED_APPS += ('django_jinja',)
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'coopbox_base.util.context_processors.coopbox_parameters',
)

# Configurations
# GOOGLE_ANALYTICS_ID = 'UA-XXXXX-X'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic_format': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic_format',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # XXX: debug settings below to get rid of the annoying django db debug logs
        'coopbox_base': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
