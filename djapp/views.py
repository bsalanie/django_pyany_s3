from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    print("got called!")
    template_name = "index.html"
