from proroot.settings.base import *
from proroot.settings.credantials import *

SECRET_KEY = secret_key

INSTALLED_APPS += [
    'apps.core.apps.CoreConfig',
]
