from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def projects(request):
    return render(request, 'portfolio/projects.html')