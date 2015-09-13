from django.conf.urls import url

from static_html import views

urlpatterns = [
   # /static_html
   url(r'^((?P<file_name>[a-zA-Z0-9-_]*)/|$)', views.index, name='index'),
]
