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

from .models import Hub, Link, Satellite
class DatavaultHome(LoginRequiredMixin, TemplateView):
    template_name = 'vault/datavault_index.html'

class HubsView(ListView): 
    model = Hub
    template_name = 'vault/hub/hub_list.html'
    # context_object_name = 'hubs'

class HubDetailsView(DetailView): 
    model = Hub 
    template_name = 'vault/hub/hub_details.html'
    # context_object_name = 'hub'

class LinksView(ListView): 
    template_name = 'vault/link/link_list.html'
    model = Link 
    # context_object_name = 'links'
class LinkDetailsView(DetailView): 
    model = Link
    template_name = "vault/link/link_details.html"
    # context_object_name = "link"

class SatelliteView(ListView): 
    template_name = "vault/satellite/satellite-list.html"
    model = Satellite
    #context_object_name = "satellites"

class SatelliteDetailsView(DetailView): 
    template_name = "vault/satellite/satellite_details.html"
    model = Satellite 
    # context_object_name = "satellite"
