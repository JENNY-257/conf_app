from django.forms import ModelForm
from django import forms
from speakers.models import Speakers

class SpeakerForm(forms.ModelForm):
    
    class Meta:
        model = Speakers
        fields = ["sp_id","sp_name","sp_email","sp_contact"]
        
