from django.db import models
from django.utils import timezone
import arrow
import datetime
import ISO3166

ISO3166_CHOICES = ISO3166.ISO3166


class Client(models.Model):
	client_name = models.CharField('Client', max_length=256)
	country = models.CharField(max_length=2, choices=ISO3166_CHOICES)
	start_date = models.DateTimeField('Registered Date')
	customer_site = models.CharField('Customer Site', max_length=256, default='')
	state = model.CharField('State', max_length=128, default='')
	gas_rate = model.FloatField('Gas Rate', default=0)
	water_rate = model.FloatField('Water Rate', default=0)
	owner = models.ForeignKey('auth.User', related_name='client')

	def was_recent(self):
		return self.start_date >= timezone.now() - datetime.timedelta(days=1)
	was_recent.admin_order_field = 'start_date'
	was_recent.boolean = True
	was_recent.short_description = 'Recently Joined?'

	def __str__(self):
		return self.client_name

	def save(self, *args, **kwargs):
		# TODO: add owner
		self.start_date = datetime.datetime.utcnow()
		super(Client, self).save(*args, **kwargs)

	class Meta:
		ordering = ('client_name',)

# class Comments(models.Model):
# 	comment = models.TextField('Comments', max_length=500)
