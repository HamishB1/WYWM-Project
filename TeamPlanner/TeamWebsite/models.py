from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)

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