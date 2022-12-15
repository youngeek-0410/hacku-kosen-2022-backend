import os

from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django_psdb_engine",
        "NAME": os.getenv("DB_NAME"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "OPTIONS": {
            "ssl": {"ca": os.getenv("MYSQL_ATTR_SSL_CA")},
            "charset": "utf8mb4",
        },
    }
}

#############################
# AWS S3
#############################
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", default="")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", default="")

# storage
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", default="")

# cloudfront
AWS_S3_CUSTOM_DOMAIN = os.getenv("CLOUD_FRONT_DOMAIN_NAME")

# media
DEFAULT_FILE_STORAGE = "config.backends.MediaStorage"

# static
AWS_LOCATION = "static"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
