from celery import shared_task, Celery
from django.conf import settings
from django.core.mail import send_mail

app = Celery()


@shared_task
def self_email(form_title, message, subject=None):
    if subject is None:
        subject = f'Отправлено с формы {form_title}'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_TO],
        fail_silently=False,
    )
