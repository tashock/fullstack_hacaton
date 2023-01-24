<<<<<<< HEAD
import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
app = Celery('config')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
=======
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','fullstack_hacaton.settings')
app = Celery('fullstack_hacaton')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# from celery import Celery

# app = Celery('alerts', broker='redis://localhost:6379/0')

# @app.task
# def send_alert(alert_message):
#     # Код для отправки оповещения
#     print(f'отправка оповещения: {alert_message}')

# # работа каждый час
# app.conf.beat_schedule = {
#     'send-alert': {
#         'task': 'send_alert',
#         'schedule': 3600.0,
#         'args': ('проверка системы ',)
#     },
# }
>>>>>>> 2e694d188e4558f0c7eea30242844e424ef14f4f
