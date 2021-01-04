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

class ASBHome(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class LogoView(TemplateView):
    template_name = "logo.html"

class HomeView(TemplateView):
    template_name = "home.html"
