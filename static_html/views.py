from django.shortcuts import render, redirect
import datetime

# Create your views here.
def index(request, file_name=None):
	if not file_name:
		return render(request, 'static_html/index.html')
	else:
		return render(request, 'static_html/%s.html' % (file_name, ))
