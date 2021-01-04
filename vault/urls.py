from django.urls import include, path

from .views import DatavaultHome, HubsView, LinksView
from .admin import datavault_admin

app_name = "datavault"
urlpatterns = [
    path('', DatavaultHome.as_view(), name="datavault_home") 
    , path('hubs',HubsView.as_view(), name="hubs")
    , path('links',LinksView.as_view(), name="links")
    , path('admin/',datavault_admin.urls) 
    # , path('datavault/admin',admin.site.urls)     
] 