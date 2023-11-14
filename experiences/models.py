from django.db import models
from project.models import Tech

# Create your models here.

class Experience(models.Model):
    entity = models.CharField(max_length=256)
    title = models.CharField(max_length=50)
    description = models.TextField()
    period = models.CharField(max_length=70)
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.entity} - ({self.title})"

