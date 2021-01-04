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

from .models import Hub, Link 
class DatavaultHome(LoginRequiredMixin, TemplateView):
    template_name = 'vault/datavault_index.html'

class HubsView(ListView): 
    model = Hub
    template_name = 'vault/hub/hub_list.html'
    context_object_name = 'hubs'

class LinksView(ListView): 
    template_name = 'vault/link_list.html'
    model = Link 
    context_object_name = 'links'
