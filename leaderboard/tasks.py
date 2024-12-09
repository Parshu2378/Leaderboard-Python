# leaderboard/tasks.py
from celery import shared_task
from .models import User, Winner

@shared_task
def identify_winner():
    users = User.objects.order_by('-points')[:2]
    if len(users) < 2 or users[0].points > users[1].points:
        Winner.objects.create(user=users[0], points=users[0].points)
