from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_portfolio"),
    path("skills", views.skills, name="skills_portfolio"),
    path("resume", views.resume, name="resume_portfolio"),
    path("projects", views.projects, name="projects_portfolio"),
    path("download:<str:cv>", views.download, name="download_cv"),
    path("contact", views.contact, name="contact"),
    path("thanks_msg", views.thanks_msg, name="thanks_msg")
]

