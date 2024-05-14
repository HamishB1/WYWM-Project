from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Team, Member
from .forms import TeamForm


def TeamWebsite(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})


def home(request):
    teams = Team.objects.all()
    team_members = {}
    for team in teams:
        members = team.member_set.all()
        team_members[team] = members
    return render(request, 'home.html', {'teams': teams, 'team_members': team_members})


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_members = Member.objects.filter(team=team)
    return render(request, 'team_detail.html', {'team': team, 'team_members': team_members})


def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'member_detail.html', {'member': member})


MemberForm = modelform_factory(Member, exclude=[])


def new_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MemberForm()
    return render(request, "new_member.html", {"form": form})


def new_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeamForm()
    return render(request, "new_team.html", {"form": form})
