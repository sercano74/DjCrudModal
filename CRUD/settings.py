# ====================  ACCESO =====================
# En CMD entrar al env\scripts\activate.bat
# python manage.py runserver
# usuario : admin
# kw: admin
# ==================================================
# ==================================================
# https://www.youtube.com/watch?v=6E_NeVjxCdE&t=39s
# ==================================================
# ==================================================
# = Tambien esta este que es modal con jS y django =
# https://www.youtube.com/watch?v=BJ5M9RYpdt4&t=665s


from pathlib import Path

## Nuevas cargas
import os


import environ
env = environ.Env()
environ.Env.read_env()

## Generar el archivo requirements.txt en basedir para agregar nuestras dependencias,
## para el caso de usar Render en este se puede utilizar Poetry, ver en el
## https://render.com/docs/deploy-django


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
## SECRET_KEY = 'django-insecure-imbqmbsbmz-__klci&i=o5b#3u!viwr5rmpov-e+$&^9f6#jg8'

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-imbqmbsbmz-__klci&i=o5b#3u!viwr5rmpov-e+$&^9f6#jg8')


# SECURITY WARNING: don't run with debug turned on in production!
## DEBUG = True
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ


ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CRUD',
    'App',

]

# pip install whitenoise[brotli]
# Añadir la nueva dependencia al siguiente listado:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'CRUD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CRUD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

## DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
print('BASE_DIR : ', BASE_DIR)
print('PATH : ', Path)

##   pip install dj-database-url
## luego,
##   import dj_database_url
## finalmente agregar modulo de postgre
##   pip install psycopg2-binary

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'),
    conn_max_age=600,
    conn_health_checks=True,
)
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

## Realizar carga de whitenoise para carga de archivos estáticos: Js, ccs, imágenes y otros, este es el que usa render
##   pip install whitenoise[brotli]
## luego, cargar el Middleware
##   'whitenoise.middleware.WhiteNoiseMiddleware',

# Following settings only make sense on production and may break development environments.
if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

## para generar el archivo staticfiles se hace a traves de generar el build.sh
##   #!/usr/bin/env bash
##   exit on error
##   set -o errexit

##   #poetry install

##   python manage.py collectstatic --no-input
##   python manage.py migrate

## NOTA: Asegurar a través de consola de GIT BASH con
##   chmod a+x build.sh
## listar con el comando "ls" y debe aparecer el build.sh*

## Cargar el gunicorn para ejecutar el proyecto
##   pip install gunicorn





# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
