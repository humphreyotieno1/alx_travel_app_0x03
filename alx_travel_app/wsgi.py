# wsgi.py
import os
import sys

path = '/home/Banta/alx_travel_app'  # Update with your PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'alx_travel_app.settings.production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()