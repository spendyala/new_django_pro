from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from clients.ISO3166 import ISO3166
import datetime
import json


def set_render_object(request, file_name=None, content=None):
	return render(request, 'static_html/%s.html' % (file_name, ), content)

def client(request, file_name=None):
	# import pdb; pdb.set_trace()
	data = {}
	data['countries_list'] = ISO3166
	return set_render_object(request, file_name=file_name, content=data)

def steam_trap(request, file_name=None):
	data = {}
	return set_render_object(request, file_name=file_name, content=data)

# Add every new Page, This is there to avoid hacking
VIEW_METHODS = {'client': client,
				'steam_trap': steam_trap}

# Create your views here.
def index(request, file_name=None):
	if not file_name:
		return render(request, 'static_html/index.html')
	else:
		method_obj = VIEW_METHODS.get(file_name)
		if method_obj:
			return method_obj(request, file_name)
		else:
			# return HttpResponse(json.dumps({'Error': 'Page Not found 404'}))
			return render(request, 'static_html/404.html')
