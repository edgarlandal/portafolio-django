from django.urls import path
from .views import experience_list, experience_new

urlpatterns = [
    path("", experience_list, name="experience_list"),
    path("new/", experience_new, name="experience_new"),
]
