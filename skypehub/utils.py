try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        from django.utils import simplejson as json

import Skype4Py
from Skype4Py.errors import SkypeError

SKYPE_HOOK_OPTIONS = {
    'Transport': 'x11',
}

def get_skype(**kwargs):
    options = kwargs or {}
    return Skype4Py.Skype(**options)
