from django import forms
from .models import Team, Member


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'  # This will include all fields from the Team model in the form


class MemberForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Member
        fields = ['name', 'role', 'team', 'start_date']
