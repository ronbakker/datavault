from django.urls import include, path

from .views import GlossaryHome, TermenRapport,TermDetails
from .admin import glossary_admin

urlpatterns = [
    path('',glossary_admin.urls)
]
