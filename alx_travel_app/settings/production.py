# alx_travel_app/settings/pythonanywhere.py
from .base import *
import os

# Security settings
DEBUG = False
ALLOWED_HOSTS = ['Banta.pythonanywhere.com']  # Replace with your PythonAnywhere domain

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Banta$alx_travel',  # Replace with your MySQL database name
        'USER': 'Banta',  # Your PythonAnywhere username
        'PASSWORD': 'Takemeback@18',  # Your database password
        'HOST': 'Banta.mysql.pythonanywhere-services.com',  # Replace with your MySQL host
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Celery configuration
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'django-db'

# Email configuration (update with your email settings)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'humphreyotieno04@gmail.com'
EMAIL_HOST_PASSWORD = 'zsfp fqks kqwt tzkj'
DEFAULT_FROM_EMAIL = 'humphreyotieno04@gmail.com'

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://Banta.pythonanywhere.com",
    # Add other allowed origins as needed
]
CORS_ALLOW_CREDENTIALS = True

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True