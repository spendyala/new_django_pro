from django.conf.urls import url

from static_html import views

urlpatterns = [
   # /static_html
   url(r'^((?P<file_name>state_details)/(?P<rec_id>[A-Z0-9]{2})|$)', views.index, name='index'),
   url(r'^((?P<file_name>excel)/(?P<obj>(steam_leak|steam_trap|boiler_datacollection|stacked_economizer))/(?P<rec_id>([0-9]+|all))|$)', views.index, name='index'),
   url(r'^((?P<file_name>[a-zA-Z0-9-_]*)/(?P<rec_id>[0-9]*)|$)', views.index, name='index'),
]
