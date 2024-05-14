from django import forms
from .models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'  # This will include all fields from the Team model in the form
