"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api_client/', include('clients.urls')),
    url(r'^api_steam_trap/', include('steam_trap.urls')),
    url(r'^api_steam_leak/', include('steam_leaks.urls')),
    url(r'^api_boiler_blowdown/', include('boiler_blowdown.urls')),
    url(r'^api_stacked_economizer/', include('stacked_economizer.urls')),
    url(r'^api_air_compressors/', include('air_compressors.urls')),
    url(r'^api_air_leak/', include('air_leak.urls')),
    url(r'^api_premium_efficiency/', include('premium_efficiency.urls')),
    url(r'^api_vfd/', include('vfd.urls')),
    url(r'^api_valve_insulation/', include('valve_insulation.urls')),
    url(r'^api_pipe_insulation/', include('pipe_insulation.urls')),
    url(r'^api_boiler_datacollection/',
        include('boiler_datacollection.urls')),
    url(r'^authenticate_user(|/)$', 'static_html.views.authenticate_user'),
    # url(r'^login(|/)$', 'main_app.views.login'),
    url(r'^(|/)', include('static_html.urls', namespace='static_html')),
]
