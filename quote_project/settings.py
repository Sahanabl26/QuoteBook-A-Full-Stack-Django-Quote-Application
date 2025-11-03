"""
Django settings for quote_project project.
(MODIFIED FOR DEPLOYMENT)
"""

from pathlib import Path
import os  # <-- ADDED FOR DEPLOYMENT
import dj_database_url  # <-- ADDED FOR DEPLOYMENT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECRET_KEY is read from an environment variable on the server
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-!8u*k-h*(=_+o4^&is_0@!pu(^mv^)#at_f_5kg!cc&74koa))')

# DEBUG is False in production, but True if you set DEBUG='True' in env
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow Render's hostname
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quotes'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- ADDED FOR DEPLOYMENT
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quote_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quote_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# --- MODIFIED FOR DEPLOYMENT ---
# Uses Render's Postgres DB in production, but your local sqlite3 in development
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # ... (your validators are fine, no changes needed) ...
]


# Internationalization
# ... (no changes needed) ...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I1N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

# This is your existing setting, which is correct
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# --- ADDED FOR DEPLOYMENT ---
# This is where 'collectstatic' will put all files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# This tells Django to use Whitenoise to serve files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# --- END OF DEPLOYMENT ADDITIONS ---


# Default primary key field type
# ... (no changes needed) ...

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'