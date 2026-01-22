"""
Django settings for twitter_clone project.
"""

import os
from pathlib import Path
from datetime import timedelta

# ==============================================================
# 📌 BASE DIR
# ==============================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================
# 🔐 SECURITY
# ==============================================================
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default-key")

DEBUG = False  # PRODUÇÃO SEMPRE FALSE

ALLOWED_HOSTS = [
    "*",  # mais simples e evita erro 400 no Render
]

# ==============================================================
# 📦 APPS
# ==============================================================
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceiros
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "django_extensions",

    # Apps
    "users",
    "tweets",
]

# ==============================================================
# ⚙️ MIDDLEWARE
# ==============================================================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # PRIMEIRO
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==============================================================
# 🌐 CORS / CSRF
# ==============================================================
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "https://twitter-theta-henna.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    "authorization",
    "content-type",
    "x-csrftoken",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CSRF_TRUSTED_ORIGINS = [
    "https://twitter-theta-henna.vercel.app",
]

# ==============================================================
# 🔗 URL / TEMPLATES / WSGI
# ==============================================================
ROOT_URLCONF = "twitter_clone.urls"

AUTH_USER_MODEL = "users.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "twitter_clone" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "twitter_clone.wsgi.application"

# ==============================================================
# 🗄️ DATABASE
# ==============================================================
DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "SQL_ENGINE",
            "django.db.backends.sqlite3"
        ),
        "NAME": os.environ.get(
            "SQL_DATABASE",
            BASE_DIR / "db.sqlite3"
        ),
        "USER": os.environ.get("SQL_USER", ""),
        "PASSWORD": os.environ.get("SQL_PASSWORD", ""),
        "HOST": os.environ.get("SQL_HOST", ""),
        "PORT": os.environ.get("SQL_PORT", ""),
    }
}

# ==============================================================
# 🔐 PASSWORD VALIDATORS
# ==============================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==============================================================
# 🌍 I18N
# ==============================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==============================================================
# 📁 STATIC / MEDIA
# ==============================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==============================================================
# ⚙️ REST FRAMEWORK / JWT
# ==============================================================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ==============================================================
# 🧠 EXTRAS
# ==============================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
