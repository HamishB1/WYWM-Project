from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Team, Member

# Create your views here.
def home(request):
    teams = Team.objects.all()
    members = Member.objects.all()
    return render(request, 'templates/home.html', {'teams': teams, 'members': members})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'teamplates/team_detail.html', {'team': team})

def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'templates/member_detail.html', {'member': member})

# Add more view functions for CRUD operations
