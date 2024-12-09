# leaderboard/tasks.py
from celery import shared_task
from .models import User, Winner
from django.db.models import Max
from datetime import timedelta

@shared_task
def check_and_declare_winner():
    # Get the user with the maximum points
    max_points = User.objects.aggregate(Max('points'))['points__max']

    # Get all users with the maximum points
    top_users = User.objects.filter(points=max_points)

    # If there's more than one user with the max points, no winner is declared
    if top_users.count() == 1:
        top_user = top_users.first()
        winner = Winner.objects.create(
            user=top_user,
            points=top_user.points,
        )
        return f"Winner declared: {top_user.name} with {top_user.points} points."
    else:
        return "No winner declared due to a tie."
