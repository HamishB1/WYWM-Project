from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from TeamWebsite.models import Manager, Member

class Command(BaseCommand):
    help = 'Creates users and assigns them to groups'

    def handle(self, *args, **kwargs):
        # Get all managers from the database
        managers = Manager.objects.all()

        # Get all members from the database
        members = Member.objects.all()

        # Get or create groups
        manager_group, _ = Group.objects.get_or_create(name='Team Managers')
        member_group, _ = Group.objects.get_or_create(name='Team Members')

        # Iterate through managers and create users
        for manager in managers:
            # Create user
            user, created = User.objects.get_or_create(username=manager.name)
            if created:
                user.set_password('1111')  # Set a default password
                user.save()

            # Assign user to manager group
            user.groups.add(manager_group)

        # Iterate through members and create users
        for member in members:
            # Create user
            user, created = User.objects.get_or_create(username=member.name)
            if created:
                user.set_password('1111')  # Set a default password
                user.save()

            # Assign user to member group
            user.groups.add(member_group)
