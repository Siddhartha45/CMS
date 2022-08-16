from celery import shared_task
from django.core.mail import send_mail

@shared_task
def nuke():
    send_mail(
        'Test',
        'Test Message',
        'from@example.com',
        ['to@example.com'],
    )
    return True