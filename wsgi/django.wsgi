#!/usr/bin/python
import os
import sys

sys.path.append('/vagrant_shared/cyp_django_site')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cyp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
