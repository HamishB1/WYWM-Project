from django.contrib import admin
from .models import Team, Manager, Member

# Register your models here.
admin.site.register(Team)
admin.site.register(Manager)
admin.site.register(Member)