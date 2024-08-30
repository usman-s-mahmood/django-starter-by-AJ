# created manually!
from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(
                attrs={
                    'placeholder': 'Add a display name'
                }
            ),
            'info': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Add Information'
                }
            )
        }