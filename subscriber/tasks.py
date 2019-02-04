import celery

from datetime import datetime
from django.core.mail import send_mass_mail
from django.conf import settings

from real_estate.celery import app
from apartments.models import Apartment
from subscriber.models import MailTemplate


@app.task(base=celery.Task)
def generate_subscriber_mail():
    messages = []
    template = MailTemplate.objects.get(mail_type='subscriber')
    for apartment in Apartment.objects.filter(date=datetime.now().date()):
        messages.append((template.title, template.body, settings.EMAIL,
                         [subscriber.email for subscriber in apartment.city.subscribers]))

    send_mass_mail(messages, fail_silently=False)
