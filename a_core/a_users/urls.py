# created manually!
from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('onboarding/', profile_edit_view, name='profile-onboarding'),
    path('@<username>/', profile_view, name='profile'),
    path('settings/', profile_settings_view, name='profile-settings'),
]