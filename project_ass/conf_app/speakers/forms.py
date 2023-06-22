from django import fields
from speakers.models import Speakers

class SpeakerForm(forms.ModelForm):
    
    class Meta:
        model = Speakers
        fields = ("__all__")
