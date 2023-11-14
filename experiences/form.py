from django import forms
from .models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["entity", "title", "description", "period", "technologies"]
        widgets = {
            "entity": forms.TextInput(attrs={"placeholder": "Institution"}),
            "title": forms.TextInput(attrs={"placeholder": "Position or certificate"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "period": forms.TextInput(attrs={"placeholder": "Period"}),
        }
