"""
Django settings for enade project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
#!/usr/bin/python
# -*- coding: ascii -*-d
import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^n!x*g2efn(5r+(j1)m1tuqhw)5fcy$mqe4l3n#(-)b8e37f$7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['54.233.173.29','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'multiupload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'enade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [   ],
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

WSGI_APPLICATION = 'enade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'correcao_gabarito'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', '@vncs@'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 3600 

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

JET_THEMES = [
                {
                    'theme': 'default',
                    # theme folder name
                    'color': '#47bac1',
                    # color of the theme's button in user menu
                    'title': 'Default'
                    # theme title
                },
                {
                    'theme': 'green',
                    'color': '#44b78b',
                    'title': 'Green'
                },
                {
                    'theme': 'light-green',
                    'color': '#2faa60',
                    'title': 'Light Green'
                },
                {
                    'theme': 'light-violet',
                    'color': '#a464c4',
                    'title': 'Light Violet'
                },
                {
                    'theme': 'light-blue',
                    'color': '#5EADDE',
                    'title': 'Light Blue'
                },
                { 
                    'theme': 'light-gray',
                    'color': '#222',
                    'title': 'Light Gray'
                }
]
JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS =True
JET_SIDE_MENU_ITEMS = [
# A list of application or custom item dicts
{'label': 'Enade', 'app_label': 'core', 'items': [
{'label':'Academico','name': 'core.aluno'},
{'label':'Curso','name': 'core.curso'},
{'label':'Gabarito','name': 'core.gabarito'},
{'label':'Periodo Avaliativo','name': 'core.periodoavaliativo'},
{'label':'Upload Gabarito','name': 'core.imagem',},
# {'label':'Analytics', 'url': 'core/imagem/multiupload/', 'url_blank': False},
]},
{'label': u'Autenticacao e Autorizacao ', 'items': [
{'label':'Usuario','name': 'auth.user'},
{'name': 'auth.group'},
]},
{'label': 'Relatorios', 'app_label': 'Relatorio', 'items': [
{'label':'Desempenho Simulado','name': 'core.relatorioacademicos'},
# {'name': 'bannertype'},
]},
]