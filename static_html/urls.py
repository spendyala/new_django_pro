from django.conf.urls import url

from static_html import views

urlpatterns = [
   # /static_html
   url(r'^((?P<file_name>state_details)/(?P<rec_id>[A-Z0-9]{2})|$)', views.index, name='index'),
   url(r'^((?P<file_name>excel)/(?P<obj>(air_compressors|air_leak|steam_leak|steam_trap|boiler_blowdown|boiler_datacollection|stacked_economizer|valve_insulation|pipe_insulation|premium_efficiency))/(?P<rec_id>([0-9]+|all))|$)', views.index, name='index'),
   url(r'^((?P<file_name>[a-zA-Z0-9-_]*)/(?P<rec_id>[0-9]*)|$)', views.index, name='index'),
]
