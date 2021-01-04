from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.core.files.storage import FileSystemStorage
from django.db import models
#from django.db.models import Q
#from django.forms import Form
from django.http import (FileResponse, HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView, TemplateView
from reportlab.pdfgen import canvas

from glossary.models import Term
class GlossaryHome(LoginRequiredMixin, TemplateView):
    template_name = 'glossary/glossary_index.html'

class TermenRapport(ListView): 
    model = Term
    template_name = 'glossary/term/term_list.html'
    context_object_name = 'termen'

class TermDetails(DetailView): 
    model = Term
    template_name = 'glossary/term/term_detail.html'
    context_object_name = 'term'
