import os
from datetime import timedelta
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

AUTH_USER_MODEL = 'auth_app.User'

IMDB_API_URL = 'https://api.collectapi.com/imdb'
IMDB_API_SEARCH_BY_NAME_URL = IMDB_API_URL + '/imdbSearchByName'
IMDB_API_SEARCH_BY_IMDB_ID_URL = IMDB_API_URL + '/imdbSearchById'
IMDB_API_KEY = env('IMDB_API_KEY', default='imdb_api_key')
OMDB_API_URL = 'http://www.omdbapi.com'
OMDB_API_KEY = env('OMDB_API_KEY', default='omdb_api_key')
YOUTUBE_API_KEY = env('YOUTUBE_API_KEY', default='')
TMDB_API_KEY = env('TMDB_API_KEY', default='')
# Movie search: 'omdb' = OMDb ?s= search, 'imdb' = CollectAPI imdbSearchByName. On provider error we fall back to DB search.
MOVIE_SEARCH_PROVIDER = env('MOVIE_SEARCH_PROVIDER', default='omdb')

OPENAI_API_KEY = env('OPENAI_API_KEY', default='')
# AI search (find movie by description): gpt-5 for better adherence to date constraints
OPENAI_AI_SEARCH_MODEL = env('OPENAI_AI_SEARCH_MODEL', default='gpt-5-mini')
# Top movies and recommendations: gpt-5-mini (cheaper, sufficient for simple JSON output)
OPENAI_AI_MODEL = env('OPENAI_AI_MODEL', default='gpt-5-mini')
MAX_PROMPT_TOKENS_LENGTH = 1000

SECRET_KEY = env('DJANGO_KEY', default='fallback_secret')

DEBUG = env.bool('DEBUG', False)
METRICS_ENABLED = env.bool('METRICS_ENABLED', default=True)

DEFAULT_ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'web',  # Docker Compose service name for Prometheus scrape
    'movie-finder-70zg.onrender.com',
    'api.moviefinder.cc',
    'moviefinder.cc',
    'www.moviefinder.cc',
]
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=DEFAULT_ALLOWED_HOSTS)
if 'web' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS = list(ALLOWED_HOSTS) + ['web']
DEFAULT_CSRF_TRUSTED_ORIGINS = ['https://api.moviefinder.cc', 'https://moviefinder.cc', 'https://www.moviefinder.cc']

# Cloudflare reverse proxy configuration
# Trust X-Forwarded-Proto header from Cloudflare/Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework.authtoken',
    'drf_spectacular',
    'movie',
    'collection',
    'auth_app',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]
if METRICS_ENABLED:
    MIDDLEWARE.insert(0, 'movie_finder_django.metrics.PrometheusMiddleware')

ROOT_URLCONF = 'movie_finder_django.urls'

DEFAULT_CORS_ALLOWED_ORIGINS = [
    'https://moviefinder.cc',
    'https://www.moviefinder.cc',
    'https://api.moviefinder.cc',
]
_cors_raw = env.list('CORS_ALLOWED_ORIGINS', default=DEFAULT_CORS_ALLOWED_ORIGINS)
CORS_ALLOWED_ORIGINS = [o.strip() for o in _cors_raw if isinstance(o, str) and o.strip()]
if not CORS_ALLOWED_ORIGINS:
    CORS_ALLOWED_ORIGINS = list(DEFAULT_CORS_ALLOWED_ORIGINS)

# Next.js local dev (and optional alt port). Enable with DEBUG or INCLUDE_LOCAL_FRONTEND_CORS in .env.
LOCAL_FRONTEND_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3001',
]
INCLUDE_LOCAL_FRONTEND_CORS = env.bool('INCLUDE_LOCAL_FRONTEND_CORS', default=False)
if DEBUG or INCLUDE_LOCAL_FRONTEND_CORS:
    CORS_ALLOWED_ORIGINS = list(dict.fromkeys(CORS_ALLOWED_ORIGINS + LOCAL_FRONTEND_ORIGINS))
    if '*' not in ALLOWED_HOSTS:
        ALLOWED_HOSTS = list(dict.fromkeys([*ALLOWED_HOSTS, '*']))

CORS_ALLOW_ALL_ORIGINS = env.bool('CORS_ALLOW_ALL_ORIGINS', default=True)
CORS_ALLOW_CREDENTIALS = True

_csrf_raw = env.list('CSRF_TRUSTED_ORIGINS', default=DEFAULT_CSRF_TRUSTED_ORIGINS)
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf_raw if isinstance(o, str) and o.strip()]
if not CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS = list(DEFAULT_CSRF_TRUSTED_ORIGINS)
if DEBUG or INCLUDE_LOCAL_FRONTEND_CORS:
    CSRF_TRUSTED_ORIGINS = list(dict.fromkeys(CSRF_TRUSTED_ORIGINS + LOCAL_FRONTEND_ORIGINS))

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

WSGI_APPLICATION = 'movie_finder_django.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='postgres'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASSWORD', default='postgres'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env.int('DB_PORT', default=5433),
        'TEST': {
            'NAME': env('DB_TEST_NAME', default='test_postgres'),
        },
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        # access_type=online only; no prompt=consent/select_account so Google reuses prior approval.
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    }
}

# Skip unstyled allauth "Continue" page; redirect straight to Google on GET.
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

SITE_ID = 1
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='email_host_user')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='email_host_password')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Local dev (DEBUG or INCLUDE_LOCAL_FRONTEND_CORS): admin CSS without collectstatic.
_serve_static_from_apps = DEBUG or INCLUDE_LOCAL_FRONTEND_CORS
if _serve_static_from_apps:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    WHITENOISE_USE_FINDERS = True
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

_default_frontend_url = 'http://localhost:3000' if INCLUDE_LOCAL_FRONTEND_CORS else 'https://moviefinder.cc'
FRONTEND_URL = env('FRONTEND_URL', default=_default_frontend_url).rstrip('/')
LOGIN_PAGE_URL = f'{FRONTEND_URL}/'
LOGIN_REDIRECT_URL = f'{FRONTEND_URL}/home/'
LOGOUT_REDIRECT_URL = LOGIN_PAGE_URL
ACCOUNT_ADAPTER = 'auth_app.adapters.MovieFinderAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'auth_app.adapters.MovieFinderSocialAccountAdapter'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'ERROR',
    },
    'loggers': {
        'django.request': {'level': 'ERROR'},
        'django.security': {'level': 'ERROR'},
        'movie': {'level': 'INFO', 'handlers': ['console'], 'propagate': False},
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
}
