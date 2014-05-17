import sys
import os

PROJECT_PATH         = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
STATIC_ROOT         = 'staticfiles'
STATIC_URL          = '/static/'
TEMPLATE_DIRS       = os.path.join(PROJECT_PATH, 'templates')
MEDIA_ROOT          = os.path.join(PROJECT_PATH, 'media')

# ===================
# = Global Settings =
# ===================

DEBUG               = True
TEMPLATE_DEBUG      = DEBUG
ADMIN_MEDIA_PREFIX  = '/media/'
MEDIA_URL           = '/media/'
STATIC_URL          = '/static/'
TIME_ZONE           = 'Pacific/Auckland'
LANGUAGE_CODE       = 'en-us'
SITE_ID             = 1
USE_I18N            = True

# ===========================
# = Django-specific Modules =
# ===========================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debate.middleware.DebateMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.csrf",
    "debate.context_processors.debate_context",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'debate',
    'south',
    'emoji',
    'debug_toolbar', # disable for production
)

LOGIN_REDIRECT_URL = '/'

# ==================
# = Configurations =
# ==================

from local_settings import *