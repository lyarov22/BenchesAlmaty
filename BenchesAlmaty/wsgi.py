import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from BenchesAlmaty import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BenchesAlmaty.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join('staticfiles'))
application.add_files(os.path.join('media'), prefix='media/')  # Если у вас есть медиа файлы

# Enable insecure serving of static files when DEBUG is True
if settings.DEBUG:
    # from django.contrib.staticfiles.handlers import StaticFilesHandler
    # application = StaticFilesHandler(application)

    STATIC_ROOT = os.path.join(settings.BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'