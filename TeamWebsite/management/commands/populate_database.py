from datetime import datetime
from django.core.management.base import BaseCommand
from TeamWebsite.models import Manager, Member, Team

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        self.clear_database()
        self.populate_database()

    def clear_database(self):
        Manager.objects.all().delete()
        Member.objects.all().delete()
        Team.objects.all().delete()

    def populate_database(self):
        # Create teams
        power_plant = Team.objects.create(name='Power Plant')
        administration = Team.objects.create(name='Administration')
        store_pass = Team.objects.create(name='Store Pass')

        # Add managers
        Manager.objects.create(name='Joe Bloggs', team=power_plant, start_date=datetime(2014, 1, 7))
        Manager.objects.create(name='John Smith', team=administration, start_date=datetime(2017, 11, 13))
        Manager.objects.create(name='Jennie Tu', team=store_pass, start_date=datetime(2021, 8, 17))

        # Add members
        Member.objects.create(name='Quinn Blackburn', role='Member', team=power_plant, start_date=datetime(2006, 1, 13))
        Member.objects.create(name='Beverley York', role='Member', team=power_plant, start_date=datetime(2019, 2, 22))
        Member.objects.create(name='Bertie Brennan', role='Member', team=administration, start_date=datetime(2021, 6, 18))
        Member.objects.create(name='Darrin Juarez', role='Member', team=administration, start_date=datetime(2022, 4, 22))
        Member.objects.create(name='Catalina Knight', role='Member', team=store_pass, start_date=datetime(2022, 4, 11))
        Member.objects.create(name='Faye Johnson', role='Member', team=store_pass, start_date=datetime(2018, 9, 10))
        Member.objects.create(name='Sylvester Villa', role='Member', team=store_pass, start_date=datetime(2022, 10, 28))

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
