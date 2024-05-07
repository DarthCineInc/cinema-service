from split_settings.tools import include
from django.core.exceptions import ImproperlyConfigured
from os import environ


ENV_TYPE = environ.get('DJANGO_ENV', None)
ENV_TYPE = 'local' # Development only
print("DJANGO ENV was not set. 'local' will be set by default.")

if not ENV_TYPE:
    raise ImproperlyConfigured("DJANGO_ENV environment variable must be set before running.")

base_settings = [
    'components/common.py',
    'components/database.py',
    f'environments/{ENV_TYPE}.py'
]

include(*base_settings)