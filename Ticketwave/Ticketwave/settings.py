"""
Django settings for Ticketwave project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n=a2yox(rubsowm)xnqv^9!q-jut2krq*s9p)j%2hdg(4^7kcf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'categories',
    'discounts',
    'orders',
    'events',
    'pricing',
    'ticket_classes',
    'ticket_groups',
    'users',
    'venues',
=======
    
    
    #authentication/autheriazation
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'Authentication_Autherization',
>>>>>>> 816aa52 (settings + auth folder)
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

ROOT_URLCONF = 'Ticketwave.urls'

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

WSGI_APPLICATION = 'Ticketwave.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "ticketwave",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#authentication_autheriazation


OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
PASSWORD_HASHERS = ['django.contrib.auth.hashers.BCryptSHA256PasswordHasher']

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'  
LOGIN_URL = 'http://localhost:8000/auth/login'
ACCOUNT_AUTHENTICATION_METHOD = 'username'


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =  'ticketwave001@gmail.com' #os.environ.get('EMAIL_ID') 
EMAIL_HOST_PASSWORD =  'zxuhoelupwlvobem' #os.environ.get('EMAIL_PW')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'ticketwave001@gmail.com'
VERIFICATION_SUCCESS_TEMPLATE = None
LOGIN_URL = 'localhost' + '/auth/login' #os.environ.get('DOMAIN')



ACCOUNT_ADAPTER = 'authentication_autheriazation.adapter.CustomAccountAdapter'
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'authentication_autheriazation.serializers.CustomRegisterSerializer',
}

ACCOUNT_LOGOUT_ON_GET = True

REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

from datetime import timedelta

REST_AUTH = {
    
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_HTTPONLY':False,
    
    
}
SIMPLE_JWT ={
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


SOCIALACCOUNT_LOGIN_ON_GET=True
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend'
    ]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
