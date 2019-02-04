from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'generate-subscriber-mail': {
        'task': 'subscriber.tasks.generate_subscriber_mail',
        'schedule': crontab(minute=0, hour=0)
    }
}
