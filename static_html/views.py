from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from clients.ISO3166 import ISO3166
from clients.models import Client

from steam_trap.models import SteamTrap, STEAM_TRAP_CHOICES, TRAP_SIZE_CHOICES
from steam_leaks.models import SteamLeak
from boiler_blowdown.models import BoilerBlowdown
from stacked_economizer.models import StackedEconomizer

import datetime
import json


def set_render_object(request, file_name=None, content=None):
	if not content:
		content={}
	content.update({'username': request.user.username})

	return render(request, 'static_html/%s.html' % (file_name, ), content)

# Clients
def client(request, file_name=None, rec_id=None):
	if rec_id:
		return render(request, 'static_html/404.html')
	data = {}
	data['countries_list'] = ISO3166
	return set_render_object(request, file_name=file_name, content=data)

def client_details(request, file_name=None, rec_id=None):
	if not rec_id:
		return render(request, 'static_html/404.html')

	try:
		client_obj = Client.objects.get(id=rec_id)
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
def steam_trap(request, file_name=None, rec_id=None):
	if rec_id:
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


def steam_trap_details(request, file_name=None, rec_id=None):
	if not rec_id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()
		trap_pipe_size_list = TRAP_SIZE_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list,
				'trap_pipe_size_list': trap_pipe_size_list}
		steam_trap_obj = SteamTrap.objects.get(id=rec_id)
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
def steam_leak(request, file_name=None, rec_id=None):
	if rec_id:
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


def steam_leak_details(request, file_name=None, rec_id=None):
	if not rec_id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]
		pressure_in_psig_list = STEAM_TRAP_CHOICES.keys()

		data = {'clients_list': clients_list,
				'pressure_in_psig_list': pressure_in_psig_list}
		steam_leak_obj = SteamLeak.objects.get(id=rec_id)
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


# Boiler Blowdown
def boiler_blowdown(request, file_name=None, rec_id=None):
	if rec_id:
		return render(request, 'static_html/404.html')
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

def boiler_blowdown_details(request, file_name=None, rec_id=None):
	if not rec_id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		boiler_blowdown_obj = BoilerBlowdown.objects.get(id=rec_id)
		data['boiler_blowdown_obj'] = boiler_blowdown_obj
		data['get_existing_blowdown_gallons_per_day'] = boiler_blowdown_obj.get_existing_blowdown_gallons_per_day()
		data['get_existing_annual_quantity_gals'] = boiler_blowdown_obj.get_existing_annual_quantity_gals()
		data['get_existing_annual_quantity_lbs'] = boiler_blowdown_obj.get_existing_annual_quantity_lbs()
		data['get_existing_blowdown_energy_loss_btuh'] = boiler_blowdown_obj.get_existing_blowdown_energy_loss_btuh()
		data['get_existing_energy_loss_therm'] = boiler_blowdown_obj.get_existing_energy_loss_therm()
		data['get_existing_blowdown_energy_loss_therm'] = boiler_blowdown_obj.get_existing_blowdown_energy_loss_therm()
		data['get_existing_overflow_cost'] = boiler_blowdown_obj.get_existing_overflow_cost()
		data['get_existing_makeup_water_quantity'] = boiler_blowdown_obj.get_existing_makeup_water_quantity()
		data['get_existing_makeup_water_cost'] = boiler_blowdown_obj.get_existing_makeup_water_cost()
		data['get_existing_gas_and_water_cost'] = boiler_blowdown_obj.get_existing_gas_and_water_cost()
		data['get_existing_blowdown_energy_recovery_therms'] = boiler_blowdown_obj.get_existing_blowdown_energy_recovery_therms()
		data['get_existing_total'] = boiler_blowdown_obj.get_existing_total()
		data['get_proposed_blowdown_gallons_per_day'] = boiler_blowdown_obj.get_proposed_blowdown_gallons_per_day()
		data['get_proposed_annual_quantity_gals'] = boiler_blowdown_obj.get_proposed_annual_quantity_gals()
		data['get_proposed_annual_quantity_lbs'] = boiler_blowdown_obj.get_proposed_annual_quantity_lbs()
		data['get_proposed_blowdown_energy_loss_btuh'] = boiler_blowdown_obj.get_proposed_blowdown_energy_loss_btuh()
		data['get_proposed_energy_loss_therm'] = boiler_blowdown_obj.get_proposed_energy_loss_therm()
		data['get_proposed_overflow_cost'] = boiler_blowdown_obj.get_proposed_overflow_cost()
		data['get_proposed_makeup_water_quantity'] = boiler_blowdown_obj.get_proposed_makeup_water_quantity()
		data['get_proposed_makeup_water_cost'] = boiler_blowdown_obj.get_proposed_makeup_water_cost()
		data['get_proposed_gas_and_water_cost'] = boiler_blowdown_obj.get_proposed_gas_and_water_cost()
		data['get_proposed_blowdown_energy_loss_therm'] = boiler_blowdown_obj.get_proposed_blowdown_energy_loss_therm()
		data['get_proposed_blowdown_energy_recovery_therms'] = boiler_blowdown_obj.get_proposed_blowdown_energy_recovery_therms()
		data['get_proposed_total'] = boiler_blowdown_obj.get_proposed_total()
		data['get_savings_gas'] = boiler_blowdown_obj.get_savings_gas()
		data['get_savings_water'] = boiler_blowdown_obj.get_savings_water()
		data['get_savings_gas_and_water'] = boiler_blowdown_obj.get_savings_gas_and_water()
		data['get_savings_total'] = boiler_blowdown_obj.get_savings_total()
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Stack Economizer
def stacked_economizer(request, file_name=None, rec_id=None):
	if rec_id:
		return render(request, 'static_html/404.html')
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

def stacked_economizer_details(request, file_name=None, rec_id=None):
	if not rec_id:
		return render(request, 'static_html/404.html')

	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		stacked_economizer_obj = StackedEconomizer.objects.get(id=rec_id)
		data['stacked_economizer_obj'] = stacked_economizer_obj
		data['get_boiler_size_mmbtu_per_hr'] = stacked_economizer_obj.get_boiler_size_mmbtu_per_hr()
		data['get_recoverable_heat_mmbtu_per_hr'] = stacked_economizer_obj.get_recoverable_heat_mmbtu_per_hr()
		data['get_recoverable_heat_therms_per_year'] = stacked_economizer_obj.get_recoverable_heat_therms_per_year()
		data['get_savings'] = stacked_economizer_obj.get_savings()
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Premium Efficiency
def premium_efficiency(request, file_name=None, rec_id=None):
	if rec_id:
		return render(request, 'static_html/404.html')
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')

# Air Compressor
def air_compressors(request, file_name=None, rec_id=None):
	if rec_id:
		return render(request, 'static_html/404.html')
	try:
		clients_obj = Client.objects.all()
		clients_list = [(x.id, x.client_name) for x in clients_obj]

		data = {'clients_list': clients_list}
		return set_render_object(request, file_name=file_name, content=data)
	except Exception as err:
		return render(request, 'static_html/404.html')
# Login and Logout
def login(request, file_name=None, rec_id=None):
	# if rec_id:
	# 	return render(request, 'static_html/login.html')
	data = {}
	return set_render_object(request, file_name=file_name, content=data)

def logout(request, file_name=None, rec_id=None):
	# Logout
	auth.logout(request)
	return set_render_object(request, file_name='login', content={})

def test_html(request, file_name=None, rec_id=None):
	# Logout
	auth.logout(request)
	return set_render_object(request, file_name=file_name, content={})

def authenticate_user(request, path):
	print path
	if path.replace('/', ''):
		return render(request, 'static_html/login.html')
	if request.method == 'POST':
		login_data = json.loads(request.body)
		user = auth.authenticate(username=login_data['username'],
								 password=login_data['password'])
		if user and user.is_authenticated():
			auth.login(request, user)
			content = {}
			content.update(csrf(request))
			return set_render_object(request,
									 file_name='index',
									 content=content)
	return set_render_object(request, file_name='index')


# Add every new Page, This is there to avoid hacking
VIEW_METHODS = { #'authenticate_user': authenticate_user,
				'client': client,
				'client_details': client_details,
				'login': login,
				'logout': logout,
				'boiler_blowdown': boiler_blowdown,
				'boiler_blowdown_details': boiler_blowdown_details,
				'steam_trap': steam_trap,
				'steam_trap_details': steam_trap_details,
				'steam_leak': steam_leak,
				'steam_leak_details': steam_leak_details,
				'stacked_economizer': stacked_economizer,
				'stacked_economizer_details': stacked_economizer_details,
				'premium_efficiency': premium_efficiency,
				'air_compressors': air_compressors,
				'test_html': test_html}

# Create your views here.
def index(request, file_name=None, rec_id=None):
	if not request.user.is_authenticated():
		# return HttpResponseRedirect('/login/')
		return login(request, file_name='login')
	if not file_name:
		content = {}
		content.update(csrf(request))
		return set_render_object(request, file_name='index', content=content)
	else:
		method_obj = VIEW_METHODS.get(file_name)
		if method_obj:
			return method_obj(request, file_name, rec_id)
		else:
			# return HttpResponse(json.dumps({'Error': 'Page Not found 404'}))
			return render(request, 'static_html/404.html')
