
import os
#import posixpath
import django
from django import setup
from pathlib import Path

# Ruta de directorio donde se encuentra la aplicación:
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave de Seguridad:
SECRET_KEY = '3d5680ac-dbe8-4eef-a8f5-d20043dd6414'

# Modo de Debug:
DEBUG = True

ALLOWED_HOSTS = []

# Referencias de la aplicacion:

INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appInventario'
]

# FrameWork:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo de URLS para el proyecto:

ROOT_URLCONF = 'proyectoInventarioCoder.urls'

# Configuración de Templates:

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

WSGI_APPLICATION = 'proyectoInventarioCoder.wsgi.application'

# Base de datos:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Validación de Password:

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

# Definiciones de internacializacion:

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estaticos:

STATIC_URL = "/static/"

# Valor para variables de base de datos, para crecimiento:

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"