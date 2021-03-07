import os

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MarkDown(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        markdowntext = open(os.path.join(os.path.dirname(__file__), '../README.MD')).read()

        context = super().get_context_data(**kwargs)
        context['markdowntext'] = markdowntext

        return context


# def home(request):
#     return render(request, 'home/home.html')
