from django.shortcuts import render, redirect
from .form import ProjectForm
from .models import Project

# Create your views here.
def project_list(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'projects/projects_list.html', context)

def project_new(req):
    if req.method == 'POST':
        form = ProjectForm(req.POST, req.FILES)
        if form.is_valid():
            project = form.save()
            return redirect("projects_list")
    else:
        form = ProjectForm()   

    return render(req, "projects/project_new.html", {'form': form})
