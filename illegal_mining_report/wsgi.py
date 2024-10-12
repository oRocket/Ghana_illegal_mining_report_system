"""
WSGI config for illegal_mining_report project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'illegal_mining_report.settings')

application = get_wsgi_application()
# added this vercel variable
app = application