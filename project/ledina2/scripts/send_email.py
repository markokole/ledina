from django.core.mail import send_mail


def run():
    send_mail(
        'Gimnazija Ledina',
        'Testiranje posiljanja mejla',
        'posiljatelj@yahoo.com',
        ['posiljatelj@yahoo.com', 'prejemnik@gmail.com'],
        fail_silently=False,
    )

