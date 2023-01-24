<<<<<<< HEAD
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

=======
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
>>>>>>> 2e694d188e4558f0c7eea30242844e424ef14f4f
__all__ = ('celery_app',)