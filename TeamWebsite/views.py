from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.contrib import messages
from .models import Team, Member
from .forms import TeamForm, MemberForm, ManagerForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


@login_required
def TeamWebsite(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})


@login_required
def home(request):
    teams = Team.objects.all()
    team_members = {}
    for team in teams:
        members = team.member_set.all()
        team_members[team] = members
    return render(request, 'home.html', {'teams': teams, 'team_members': team_members})


@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_members = Member.objects.filter(team=team)
    return render(request, 'team_detail.html', {'team': team, 'team_members': team_members})


@login_required
def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'member_detail.html', {'member': member})


@login_required
def new_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MemberForm()
    return render(request, "new_member.html", {"form": form})


@login_required
def new_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeamForm()
    return render(request, "new_team.html", {"form": form})


# New views for updating and deleting members
@login_required
def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_detail', member_id=member_id)
    else:
        form = MemberForm(instance=member)
    return render(request, 'update_member.html', {'form': form})


@login_required
def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'member': member})


@login_required
def move_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        new_team_id = request.POST.get('new_team')
        new_team = get_object_or_404(Team, id=new_team_id)
        member.team = new_team
        member.save()
        return redirect('team_detail', team_id=new_team_id)
    else:
        # Redirect to some page or handle the situation when request method is not POST
        pass


@login_required
def add_member_to_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    available_members = Member.objects.exclude(team=team)  # Exclude members who are already part of the team
    print("Available Members:", available_members)  # Print out available_members for debugging
    if request.method == 'POST':
        member_id = request.POST.get('member')
        member = get_object_or_404(Member, id=member_id)
        member.team = team
        member.save()
        return redirect('team_detail', team_id=team_id)
    else:
        return render(request, 'team_detail.html', {'team': team, 'team_members': team.member_set.all(), 'available_members': available_members})


@login_required
def create_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save()
            return redirect('home')  # Redirect to the home page
    else:
        form = ManagerForm()
    return render(request, 'create_manager.html', {'form': form})


@login_required
def delete_manager(request, manager_id):
    manager = get_object_or_404(Manager, id=manager_id)
    if request.method == 'POST':
        manager.delete()
        return redirect('home')  # Redirect to the home page
    return render(request, 'confirm_delete_manager.html', {'manager': manager})


@login_required
def confirm_delete_manager(request, manager_id):
    manager = get_object_or_404(Manager, id=manager_id)
    return render(request, 'confirm_delete_manager.html', {'manager': manager})
