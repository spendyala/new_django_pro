from django.db import models
from django.utils import timezone
import datetime
import ISO3166


class Client(models.Model):
	client_name = models.CharField('Client', max_length=256)
	country = models.CharField(max_length=2, choices=ISO3166.ISO3166)
	start_date = models.DateTimeField('Registered Date')
	customer_site = models.CharField('Customer Site', max_length=256, default='')

	def was_recent(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=1)
	was_recent.admin_order_field = 'start_date'
	was_recent.boolean = True
	was_recent.short_description = 'Recently Joined?'

	def __str__(self):
		return self.client_name

# class Comments(models.Model):
# 	comment = models.TextField('Comments', max_length=500)
