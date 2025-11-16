from django import forms
from django.forms import ModelForm

from .models import user_details
from .models import AudioFile
from .models import AudioFile

class useridForm(forms.Form):
    idval=forms.IntegerField()
    audio_file=forms.FileField(required=False)

class user_form(forms.ModelForm):
    class Meta:
        model = user_details
        fields = ['first_name','last_name','email','audio_file']
