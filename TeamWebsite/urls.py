from django.urls import path
from TeamWebsite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('new_member/', views.new_member, name="new_member"),  # Corrected
    path('new_team/', views.new_team, name="new_team"),  # Corrected
    # New URL patterns for updating and deleting members
    path('member/<int:member_id>/update/', views.update_member, name='update_member'),
    path('member/<int:member_id>/delete/', views.delete_member, name='delete_member'),
    # Add more URL patterns for CRUD operations
    # Add more URL patterns for CRUD operations
]
