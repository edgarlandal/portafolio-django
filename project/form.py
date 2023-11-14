from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "year", "img", "repository", "technologies"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project Name"}),
            "description": forms.Textarea(attrs={"placeholder": "Project Description"}),
            "year": forms.TextInput(attrs={"placeholder": "Year"}),
            "img": forms.ClearableFileInput(
                attrs={"placeholder": "Select an Image"}
            ),
            "respository": forms.TextInput(attrs={"placeholder": "Repository URL"}),
        }
