from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class home(TemplateView):
    template_name = 'home/index.html'