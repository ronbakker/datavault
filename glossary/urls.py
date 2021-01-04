from django.urls import include, path

from .views import GlossaryHome, TermenRapport,TermDetails
from .admin import glossary_admin

app_name = "glossary"
urlpatterns = [
    path('',GlossaryHome.as_view(), name='glossary_home')
    # , path('admin/',glossary_admin.urls)
    , path('termen',TermenRapport.as_view(),name='termen')
    , path('<int:pk>/term_detail',TermDetails.as_view(),name='term_detail')        
]
