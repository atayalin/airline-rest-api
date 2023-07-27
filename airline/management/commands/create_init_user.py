from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'To create initial user.'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='user').exists():
            User.objects.create_user(username='user', password='1234')
            self.stdout.write(self.style.SUCCESS('Initial user "user" created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Initial user "user" already exists.'))
