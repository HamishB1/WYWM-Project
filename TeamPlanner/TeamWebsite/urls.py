from django.urls import path
from TeamWebsite import views


urlpatterns = [
    path('', views.TeamWebsite, name='home'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    # Add more URL patterns for CRUD operations
]
