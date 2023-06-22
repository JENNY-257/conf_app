from django.shortcuts import render
from django.http import HttpResponse
from speakers.models import Speakers
from speakers.forms import SpeakerForm

# Create your views here.
def speak(request):
    if request.method=="POST":
        form=SpeakerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=SpeakerForm()
    return HttpResponse('hello there!')
def hello(req):
    return HttpResponse("hellllllo")
return render(request,"index.html"),"form":form