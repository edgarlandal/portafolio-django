from django.shortcuts import render, redirect
from .form import ExperienceForm
from .models import Experience

# Create your views here.
def experience_list(req):
    experiences = Experience.objects.all()
    context = {'experiences': experiences}
    return render(req, 'experience/experience_list.html', context)

def experience_new(req):
    if req.method == 'POST':
        form = ExperienceForm(req.POST)
        if form.is_valid():
            experience = form.save()
            return redirect("experience_list")
    else:
        form = ExperienceForm()   

    return render(req, "experience/experience_new.html", {'form': form})

