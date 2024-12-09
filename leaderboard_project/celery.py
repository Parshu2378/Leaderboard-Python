# myproject/celery.py (update with periodic task schedule)
from celery import Celery
from celery.schedules import crontab

app = Celery('myproject')

app.conf.beat_schedule = {
    'check-winner-every-5-minutes': {
        'task': 'leaderboard.tasks.check_and_declare_winner',
        'schedule': crontab(minute='*/5'),  # Run every 5 minutes
    },
}

# Using a string here means the worker doesn’t have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
