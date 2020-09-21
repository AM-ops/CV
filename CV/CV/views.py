from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'

class SuccessPage(TemplateView):
    """docstring for HomePage."""
    template_name = 'success.html'

def handler404(request, exception):
       return render(request, '404.html')
