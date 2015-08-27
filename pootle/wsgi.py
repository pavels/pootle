import os
import site
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pootle.settings'

from django.core.wsgi import get_wsgi_application
from django.core.cache import cache

cache.clear()
application = get_wsgi_application()
