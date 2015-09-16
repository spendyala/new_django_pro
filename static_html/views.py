from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from clients.ISO3166 import ISO3166
from clients.models import Client
import datetime
import json


def set_render_object(request, file_name=None, content=None):
	return render(request, 'static_html/%s.html' % (file_name, ), content)

# Clients
def client(request, file_name=None, id=None):
	if id:
		return render(request, 'static_html/404.html')
	data = {}
	data['countries_list'] = ISO3166
	return set_render_object(request, file_name=file_name, content=data)

def client_details(request, file_name=None, id=None):
	if not id:
		return render(request, 'static_html/404.html')

	try:
		client_obj = Client.objects.get(id=id)
		data = {'client_id': client_obj.id,
				'client_name': client_obj.client_name,
				'country_id': client_obj.country,
				'start_date': client_obj.start_date,
				'customer_site': client_obj.customer_site}
		data['countries_list'] = ISO3166
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Steam Trap
def steam_trap(request, file_name=None, id=None):
	if id:
		return render(request, 'static_html/404.html')
	data = {}
	return set_render_object(request, file_name=file_name, content=data)


def steam_trap_details(request, file_name=None, id=None):
	if not id:
		return render(request, 'static_html/404.html')

	try:
		client_obj = Client.objects.get(id=id)
		data = {'client_id': client_obj.id,
				'client_name': client_obj.client_name,
				'country_id': client_obj.country,
				'start_date': client_obj.start_date,
				'customer_site': client_obj.customer_site}
		data['countries_list'] = ISO3166
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Add every new Page, This is there to avoid hacking
VIEW_METHODS = {'client': client,
				'client_details': client_details,
				'steam_trap': steam_trap}

# Create your views here.
def index(request, file_name=None, id=None):
	if not file_name:
		return render(request, 'static_html/index.html')
	else:
		print file_name
		method_obj = VIEW_METHODS.get(file_name)
		if method_obj:
			return method_obj(request, file_name, id)
		else:
			# return HttpResponse(json.dumps({'Error': 'Page Not found 404'}))
			return render(request, 'static_html/404.html')
