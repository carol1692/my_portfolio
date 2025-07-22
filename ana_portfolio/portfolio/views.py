from django.shortcuts import render
from dotenv import load_dotenv
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, FileResponse
from datetime import datetime
from .forms.contact_form import ContactPortfolio
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

load_dotenv()
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
        response = FileResponse(open( path_cv + 'cv- Ana Lemos - dev-en.pdf', "rb"),as_attachment=True)
    return response

def contact(request, data=current_year):
    if request.method == 'POST':
        formulario = ContactPortfolio(request.POST)
        if formulario.is_valid():
            user_name = formulario.cleaned_data['user_name']
            user_email = formulario.cleaned_data['user_mail']
            user_message = formulario.cleaned_data['message']
            html_content = render_to_string('portfolio/contact_mail.html', {"username": user_name, "mail": user_email, "message": user_message} )
            text_content = strip_tags(html_content)

            send_email = EmailMultiAlternatives(subject=f'Contact from {user_name} via my portfolio', body=text_content, from_email=settings.EMAIL_HOST_USER, to=["carol1692@hotmail.com"])
            send_email.attach_alternative(html_content, 'text/html')
            send_email.send()
            return HttpResponseRedirect("/portfolio/thanks_msg")
    else:
        formulario = ContactPortfolio()
    
    return render(request, "portfolio/contact.html", {"id": "contact_bt","year":data, "formulario":formulario})

def thanks_msg(request, data=current_year()):
    return render(request, 'portfolio/thanks_msg.html' , {"id": "contact_bt","year":data})