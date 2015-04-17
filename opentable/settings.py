"""
Django settings for opentable project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fxkasrl7@_$o4p+*@5iz491!+f*d8&%fw-j(ryr-o1&gm-uv8*'

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
    'taggit',
    'crispy_forms',
    'characters',
    'writeups',
    'tinymce',
    'highcharts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'opentable.context_processors.add_sidebar_data',
)

ROOT_URLCONF = 'opentable.urls'

WSGI_APPLICATION = 'opentable.wsgi.application'

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = ''

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    STATIC_PATH,
)


# template files
TEMPLATE_URL = '/templates/'

TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')

TEMPLATE_DIRS = [
    TEMPLATE_PATH,
]

# media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_PATH = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    MEDIA_PATH
]

#redirect if not logged in
LOGIN_URL = '/'

#Tagging settings
FORCE_LOWERCASE_TAGS = True

#crispy-forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#tiny MCE stuff
TINYMCE_JS_URL = os.path.join(STATIC_PATH, "js/tiny_mce/tiny_mce.js")

# TODO: get all writeups and summaries from email threads and write scripts to insert into database.

# Do this absolutely last! Will not port from sqllite to production db