from django.shortcuts import render
from django.views.generic import TemplateView



def home(request):
    return render(request, 'info/index.html')  # Renders the main page



# Class-based views for legal pages
class DatenschutzView(TemplateView):
    template_name = 'info/Datenschutz.html'

class AGBView(TemplateView):
    template_name = 'info/AGB.html'


class ImpressumView(TemplateView):
    template_name = 'info/Impressum.html'