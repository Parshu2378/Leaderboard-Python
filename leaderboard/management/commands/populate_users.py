# leaderboard/management/commands/populate_users.py
from django.core.management.base import BaseCommand
from faker import Faker
from leaderboard.models import User
import random

class Command(BaseCommand):
    help = 'Populates the database with random users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--num_users',
            type=int,
            help='Indicates the number of users to create',
            default=10,  # Default to 10 if not specified
        )

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = kwargs['num_users']

        for _ in range(num_users):
            name = fake.name()
            age = random.randint(18, 60)  # Random age between 18 and 60
            points = random.randint(0, 100)  # Random points between 0 and 100
            address = fake.address()

            # Create and save a new user
            User.objects.create(
                name=name,
                age=age,
                points=points,
                address=address
            )

        self.stdout.write(self.style.SUCCESS(f'{num_users} users created successfully!'))
