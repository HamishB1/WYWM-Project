from django.urls import path
from TeamWebsite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('new_member/', views.new_member, name="new_member"),  # Corrected
    path('new_team/', views.new_team, name="new_team"),  # Corrected
    # Add more URL patterns for CRUD operations
]
