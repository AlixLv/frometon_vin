"""
WSGI config for frometon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frometon.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "frometon.settings"


application = get_wsgi_application()
print("🍉  application: ", application)
# connecting Django app on Vercel.app
app = application 

