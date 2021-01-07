from django.urls import include, path

from .views import DatavaultHome, HubsView, HubDetailsView, LinksView, LinkDetailsView, SatelliteView, SatelliteDetailsView
from .admin import datavault_admin

app_name = "datavault"
urlpatterns = [
    path('', DatavaultHome.as_view(), name="datavault_home") 
    , path('hubs', HubsView.as_view(), name="hub_list")
    , path('<int:pk>/hub_details', HubDetailsView.as_view(), name="hub_details")
    , path('links',LinksView.as_view(), name="link_list")
    , path('<int:pk>/link_details', LinkDetailsView.as_view, name="link_details")
    , path('satellites', SatelliteView.as_view, name="satellite_list")
    , path('<int:pk>/satellite_details',SatelliteView.as_view, name="satellite_details")
    , path('admin/',datavault_admin.urls) 
    # , path('datavault/admin',admin.site.urls)     
] 