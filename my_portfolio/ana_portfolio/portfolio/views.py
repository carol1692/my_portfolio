from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from datetime import datetime
# Create your views here.


def current_year():
    date = datetime.today()
    year = date.year
    return year

def index(request, data=current_year()):
    return render(request, 'portfolio/index.html', {"id": "home_bt", "year":data})

def skills(request, data=current_year()):
    return render(request, 'portfolio/skills.html' , {"id": "skills_bt","year":data})

def resume(request, data=current_year()):
    return render(request, 'portfolio/resume.html' , {"id": "resume_bt","year":data})

def projects(request, data=current_year()):
    return render(request, 'portfolio/projects.html' , {"id": "projects_bt","year":data})

def download(request, cv):
    path_cv = 'portfolio/static/portfolio/cvs/'
    if cv == 'download_pt':
        response = FileResponse(open( path_cv + 'cv- Ana Lemos - pt-br.pdf', "rb"),as_attachment=True)
    else:
        response = FileResponse(open( path_cv + 'cv- Ana Lemos - en.pdf', "rb"),as_attachment=True)
    return response