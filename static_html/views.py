from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from clients.ISO3166 import ISO3166
from clients.models import Client

from steam_trap.models import SteamTrap, STEAM_TRAP_CHOICES, TRAP_SIZE_CHOICES
from steam_leaks.models import SteamLeak

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
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()
		trap_pipe_size_list = TRAP_SIZE_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list,
				'trap_pipe_size_list': trap_pipe_size_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')


def steam_trap_details(request, file_name=None, id=None):
	if not id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()
		trap_pipe_size_list = TRAP_SIZE_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list,
				'trap_pipe_size_list': trap_pipe_size_list}
		steam_trap_obj = SteamTrap.objects.get(id=id)
		data['steam_trap_obj'] = steam_trap_obj
		data['get_steam_energy_btu_per_lb'] = steam_trap_obj.get_steam_energy_btu_per_lb()
		data['get_steam_loss_pph'] = steam_trap_obj.get_steam_loss_pph()
		data['get_gas_usage_therms_per_hour'] = steam_trap_obj.get_gas_usage_therms_per_hour()
		data['absolute_pressure_psia'] = steam_trap_obj.absolute_pressure_psia()
		data['size_trap_orifice'] = steam_trap_obj.size_trap_orifice()
		data['get_cost_per_hour'] = steam_trap_obj.get_cost_per_hour()
		data['get_cost_per_year'] = steam_trap_obj.get_cost_per_year()
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Steam Leak
def steam_leak(request, file_name=None, id=None):
	if id:
		return render(request, 'static_html/404.html')
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()
		# trap_pipe_size_list = TRAP_SIZE_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')


def steam_leak_details(request, file_name=None, id=None):
	if not id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list}
		steam_leak_obj = SteamLeak.objects.get(id=id)
		data['steam_leak_obj'] = steam_leak_obj
		data['get_steam_energy_btu_per_lb'] = steam_leak_obj.get_steam_energy_btu_per_lb()
		data['get_steam_loss_pph'] = steam_leak_obj.get_steam_loss_pph()
		data['get_gas_usage_therms_per_hour'] = steam_leak_obj.get_gas_usage_therms_per_hour()
		data['absolute_pressure_psia'] = steam_leak_obj.absolute_pressure_psia()
		data['get_cost_per_hour'] = steam_leak_obj.get_cost_per_hour()
		data['get_cost_per_year'] = steam_leak_obj.get_cost_per_year()
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')


# Login
def login(request, file_name=None, id=None):
	if id:
		return render(request, 'static_html/login.html')
	data = {}
	return set_render_object(request, file_name=file_name, content=data)

# Add every new Page, This is there to avoid hacking
VIEW_METHODS = {'client': client,
				'client_details': client_details,
				'login': login,
				'steam_trap': steam_trap,
				'steam_trap_details': steam_trap_details,
				'steam_leak': steam_leak,
				'steam_leak_details': steam_leak_details}

# Create your views here.
def index(request, file_name=None, id=None):
	if not file_name:
		return render(request, 'static_html/index.html')
	else:
		method_obj = VIEW_METHODS.get(file_name)
		if method_obj:
			return method_obj(request, file_name, id)
		else:
			# return HttpResponse(json.dumps({'Error': 'Page Not found 404'}))
			return render(request, 'static_html/404.html')
