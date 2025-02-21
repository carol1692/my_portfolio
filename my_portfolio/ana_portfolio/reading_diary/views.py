from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "reading_diary/index.html"

    def get_context_data(self, **kwargs):
        template_data = super().get_context_data(**kwargs)
        template_data["rows_range"] = range(2)
        template_data["cols_range"] = range(3)
        return template_data
