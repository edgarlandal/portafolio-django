from django.urls import path
from .views import project_new, project_list
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", project_list, name="project_list"),
    path("new/", project_new, name="project_new"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
