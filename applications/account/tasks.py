from django.core.mail import send_mail
from config.celery import app

#
# @app.task
# def send_confirmation_email_celery(email, code):
#     full_link = f'http://localhost:8000/account/activate/{code}'
#     send_mail(
#         'Активация пользователя',
#         full_link,
#         'muratalievaziret4@gamil.com',
#         [email]
#     )