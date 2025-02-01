from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from datetime import datetime
from .forms.contact_form import ContactPortfolio
import smtplib, os
from replace_accents import replace_accents_characters
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

def contact(request, data=current_year):
    if request.method == 'POST':
        formulario = ContactPortfolio(request.POST)
        my_email = os.getenv("E_MAIL")
        mail_pwd = os.getenv("E_MAIL_PASSWD")
        if formulario.is_valid():
            user_name = formulario.cleaned_data['user_name']
            user_email = formulario.cleaned_data['user_mail']
            user_message = formulario.cleaned_data['message']

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=mail_pwd)
                connection.sendmail(from_addr=my_email, to_addrs="carol1692@hotmail.com", msg=f"subject: Contact from {user_name} via my portfolio\n\n Nome do remetente: {user_name}\n\n  Reply to e-mail: {user_email}\n\n Message:{replace_accents_characters(user_message)}")
            return HttpResponseRedirect("/portfolio/thanks_msg")
    else:
        formulario = ContactPortfolio()
    return render(request, "portfolio/contact.html", {"id": "contact_bt","year":data, "formulario":formulario})
    
def thanks_msg(request, data=current_year()):
    return render(request, 'portfolio/thanks_msg.html' , {"id": "contact_bt","year":data})