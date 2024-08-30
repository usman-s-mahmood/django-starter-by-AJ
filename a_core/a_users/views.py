from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(
            User,
            username=username
        ).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    profile = request.user.profile
    return render(
        request,
        'a_users/profile.html',
        {
            'profile': profile
        }
    )
    
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if form.is_valid():
            form.save();
            return redirect('profile')
    if request.path == reverse('profile-onboarding'):
        onboarding=True
    else:
        onboarding=False
    return render(
        request,
        'a_users/profile_edit.html',
        {
            'form': form,
            'onboarding': onboarding 
        }
    )
    
@login_required
def profile_settings_view(request):
    return render(
        request,
        'a_users/profile_settings.html',
        {
            
        }
    )