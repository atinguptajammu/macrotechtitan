from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y#!hvdueq#n=j(=9hwt%5d*35qs3u!ma6zvzbydo5c@&3k=e^!"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["www.macrotechtitan.com" , "*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CSRF_TRUSTED_ORIGINS = ["https://www.macrotechtitan.com"]

try:
    from .local import *
except ImportError:
    pass
