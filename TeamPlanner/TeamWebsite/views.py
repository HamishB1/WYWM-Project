from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team, Member
# Create your views here.


def TeamWebsite(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})


def home(request):
    teams = Team.objects.all()
    team_members = {team: Member.objects.filter(team=team) for team in teams}
    return render(request, 'home.html', {'team_members': team_members})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})


def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'member_detail.html', {'member': member})

# Add more view functions for CRUD operations
