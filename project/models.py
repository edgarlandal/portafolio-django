from django.db import models

types = [
    ("Leguage", "Leguage"),
    ("Frameworks", "Frameworks"),
    ("Tools", "Tools"),
    ("Other", "Other"),
]


# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to="tech_images/", blank=True, null=True)
    type = models.CharField(max_length= 50,choices=types, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to="projects_images/")
    repository = models.URLField()
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.name} - ({self.year})"
