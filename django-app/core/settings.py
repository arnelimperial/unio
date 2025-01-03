import os
from decouple import config, Csv
from django.conf import settings
from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='secretkey')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1, django-app, host.docker.internal', cast=Csv())

# Application definition & Middlewares
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "django.contrib.sites",
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
]

LOCAL_APPS = [
    'users.apps.UsersConfig',
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Common & Templates
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = "users.User"

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'

# Database & Cache
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='mydatabase'),
        'USER': config('DB_USER', default='myuser'),
        'PASSWORD': config('DB_PASSWORD', default='mypassword'),
        'HOST': config('POSTGRES_HOST', default='localhost'), # Use localhost since Django is running outside Docker
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password & Auth Backends
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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

AUTHENTICATION_BACKENDS = [
    'users.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# CORS
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS = True

CSRF_HEADER_NAME = 'X-CSRFToken'

CSRF_COOKIE_NAME = 'csrftoken'

CORS_EXPOSE_HEADERS = ['Content-Type', 'authorization', 'X-CSRFToken', 'Access-Control-Allow-Origin: *',]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:5173',
    'http://localhost:5173',
    'http://127.0.0.1:8080',
    'http://localhost:8080',

]
CORS_ORIGIN_WHITELIST = (
     'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:5173',
    'http://localhost:5173',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
)

CORS_ALLOW_HEADERS = default_headers + (
    'Access-Control-Allow-Origin',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Origin',
    'cache-control',
    'if-modified-since',
    'keep-alive',
    'X-Mx-ReqToken',
    'XMLHttpRequest',
)

CORS_PREFLIGHT_MAX_AGE = 86400

# GOOGLE CREDENTIALS SOCIAL AUTH
# ------------------------------------------------------------------------------

GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')

GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')

GOOGLE_REDIRECT_URI = 'http://localhost:8080/api/auth/google/callback'

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = config('ADMIN_URL', default='admin/')

# django-rest-framework
# -------------------------------------------------------------------------------

DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + \
        ('rest_framework.renderers.BrowsableAPIRenderer',)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        'rest_framework.permissions.AllowAny'
    ],
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

}

# Simple JWT
# ------------------------------------------------------------------------------

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}


# Security
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = False

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_HTTPONLY = False

if not settings.DEBUG:

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_SSL_REDIRECT = config(
        'SECURE_SSL_REDIRECT', default=True, cast=bool)

    SESSION_COOKIE_SECURE = config(
        'SESSION_COOKIE_SECURE', default=True, cast=bool)

    CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE',
                                default=True, cast=bool)

    SECURE_HSTS_SECONDS = config(
        'SECURE_HSTS_SECONDS', default=18408206, cast=int)  # 60

    SECURE_HSTS_INCLUDE_SUBDOMAINS = config(
        'SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)

    SECURE_HSTS_PRELOAD = config(
        'SECURE_HSTS_PRELOAD', default=True, cast=bool)

    SECURE_CONTENT_TYPE_NOSNIFF = config(
        'SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)

    SECURE_REFERRER_POLICY = config(
        'REFERRER_POLICY', default='no-referrer-when-downgrade')

    CORS_REPLACE_HTTPS_REFERER = True

    CSRF_TRUSTED_ORIGINS = [
        'https://www.arnelimperial.com',
        # 'https://synchro-web.onrender.com',
    ]



