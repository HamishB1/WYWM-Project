from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class User(AbstractUser):
    pass


class TeamManager(models.Manager):
    pass


class Team(models.Model):
    name = models.CharField(max_length=100)

    # Define a default manager
    objects = TeamManager()

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_manage_team", "Can manage team"),
        ]


class Manager(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_manage_member", "Can manage member"),
        ]

    # Define a default manager
    objects = models.Manager()
