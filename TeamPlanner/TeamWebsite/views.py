from django.shortcuts import render, get_object_or_404
from .models import Team, Member


def TeamWebsite(request):
    # Fetch all teams from the database
    teams = Team.objects.all()
    # Render the 'home.html' template with the teams data
    return render(request, 'home.html', {'teams': teams})


def home(request):
    # Fetch all teams from the database
    teams = Team.objects.all()
    # Initialize an empty dictionary to store team members
    team_members = {}
    # Add this debugging line to print the contents of team_members
    print(team_members)

    # Iterate over each team
    for team in teams:
        # Access the members of the current team using the related name 'member_set'
        members = team.member_set.all()
        # Add the team and its members to the 'team_members' dictionary
        team_members[team] = members

    # Render the 'home.html' template with the team members data
    return render(request, 'home.html', {'teams': teams, 'team_members': team_members})


def team_detail(request, team_id):
    # Fetch the team with the given ID from the database, or return a 404 error if not found
    team = get_object_or_404(Team, id=team_id)
    # Render the 'team_detail.html' template with the team data
    return render(request, 'team_detail.html', {'team': team})


def member_detail(request, member_id):
    # Fetch the member with the given ID from the database, or return a 404 error if not found
    member = get_object_or_404(Member, id=member_id)
    # Render the 'member_detail.html' template with the member data
    return render(request, 'member_detail.html', {'member': member})

# Add more view functions for CRUD operations
