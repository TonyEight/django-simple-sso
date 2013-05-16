# Django settings for example client project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Amsterdam'

USE_TZ = False

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '*6_p%jz4o0j=&amp;lh%m6*@8=zyb021w0sg+ham2h_mha9a6v_zp%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls_client'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'simple_sso.sso_server',
)

LOGIN_URL = 'simple-sso-login'
SSO_SERVER = 'http://127.0.0.1:8000/authserver/'

SSO_PUBLIC_KEY = 'dxHJmiFWHfXWADYnTm9zBvay3gBkiArNKd9RhLpaH2FVBiUP1g2dVCYlUeHw0VGb'
SSO_PRIVATE_KEY = 's50T5KtTTGtXTNaadOxi4XuISGFh3xw5WTeoAy51mAC40S4RVj4V7bKVBIGxPG5G'