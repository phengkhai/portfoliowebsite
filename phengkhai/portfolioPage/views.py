from django.views import generic
from .models import Projects
from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404

class ProjectsList(generic.ListView):
    queryset = Projects.objects.order_by('-created_on')
    template_name = 'index.html'

class ProjectsDetail(generic.DetailView):
    model = Projects
    template_name = 'project_detail.html'
    def projects_detail(request, slug):
        projects = get_object_or_404(Projects, slug=slug)
        return render(request, 'project_detail.html', {'projects': projects})
