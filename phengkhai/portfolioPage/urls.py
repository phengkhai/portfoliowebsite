from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProjectsList.as_view(), name='home'),
    path('projects/<slug>/', views.ProjectsDetail.as_view(), name='projects_detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)