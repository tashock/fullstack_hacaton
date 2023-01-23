from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'User activation',
        full_link,
        'muratalievaziret4@gamil.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Password recovery',
        code,
        'muratalievaziret4@gamil.com',
        [email]
    )
