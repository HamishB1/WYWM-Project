from django.db import models


class TeamManager(models.Manager):
    pass


class Team(models.Model):
    name = models.CharField(max_length=100)

    # Define a default manager
    objects = TeamManager()

    def __str__(self):
        return self.name


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

    # Define a default manager
    objects = models.Manager()
