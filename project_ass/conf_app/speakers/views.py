from django.shortcuts import render
from django.http import HttpResponse
from speakers.models import Speakers
from .forms import SpeakerForm

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
    return render(request,'index.html',{'form':form})
def show(request):
    speakers=Speakers.objects.all() 
    return render(request,'show.html',{'speakers':speakers})
def edit(request, id):
    speakers=Speakers.objects.get(id=id)
    return render(request, 'edit.html', {'speakers':speakers})
def update(request,id):
    speakers=Speakers.objects.get(id=id)
    form=SpeakerForm(request.POST,instance=speakers)
    if form.is_Valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'speakers':speakers})
def destroy(request,id):
    speakers=Speakers.objects.get(id=id)
    speakers.delete()
    return redirect("/show")

    