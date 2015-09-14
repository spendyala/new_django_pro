from django.shortcuts import render, redirect

from clients.ISO3166 import ISO3166
import datetime


def set_render_object(request, file_name=None, content=None):
	return render(request, 'static_html/%s.html' % (file_name, ), content)

def client(request, file_name=None):
	# import pdb; pdb.set_trace()
	data = {}
	data['countries_list'] = ISO3166
	return set_render_object(request, file_name=file_name, content=data)


VIEW_METHODS = {'client': client}

# Create your views here.
def index(request, file_name=None):
	if not file_name:
		return render(request, 'static_html/index.html')
	else:
		return VIEW_METHODS[file_name](request, file_name)
