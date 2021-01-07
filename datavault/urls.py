"""datavault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

""" import from the overal project web site """
from .views import ASBHome, LogoView, HomeView

""" imports from the diffent apps """
from glossary.views import GlossaryHome, TermenRapport, TermDetails

from glossary.admin import glossary_admin 
from vault.admin import datavault_admin

app_name = "project"
urlpatterns = [
    path("",ASBHome.as_view(),name="asb_home")
    , path('home',HomeView.as_view())
    , path('glossary/', include('glossary.urls'))
    , path('datavault/',include('vault.urls'))
    , path('gl_admin', glossary_admin.urls)
    , path('dv_admin', datavault_admin.urls)
] + static(settings.STATIC_ROOT, document_root=settings.BASE_DIR)
