from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class PremiumEfficiency(models.Model):
    client = models.ForeignKey(Client)
    start_date = models.DateTimeField('Registered Date')

    motor_name = models.CharField('Motor Name', max_length=160)
    annual_operating_hours = models.FloatField(
        'Annual Operating Hours', default=0)
    # client.electric_rate = models.FloatField('Energy Cost', default=0)
    motor_nameplate_hp = models.FloatField('Motor Nameplate Hp', default=0)
    existing_full_load_eff = models.FloatField(
        'Existing Full Load Efficiency', default=0)
    existing_three_fourth_load_eff = models.FloatField(
        'Existing 3/4 Load Efficiency', default=0)
    existing_half_load_eff = models.FloatField(
        'Existing 1/2 Load Efficiency', default=0)
    existing_motor_purchase_price = models.FloatField(
        'Existing Motor Purchase Price', default=0)
    proposed_full_load_eff = models.FloatField(
        'Proposed Full Load Efficiency', default=0)
    proposed_three_fourth_load_eff = models.FloatField(
        'Proposed 3/4 Load Efficiency', default=0)
    proposed_half_load_eff = models.FloatField(
        'Proposed 1/2 Load Efficiency', default=0)
    proposed_motor_purchase_price = models.FloatField(
        'Proposed Motor Purchase Price', default=0)
    motor_nameplate_rpm = models.FloatField('Motor Nameplate RPMs', default=0)
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='premium_efficiency')

    def load_energy_cost(self, load_efficiency, load_val=1):
        try:
            val = (self.motor_nameplate_hp * 0.746 *
                   self.annual_operating_hours *
                   self.client.electric_rate * load_val * 100)
            val = round(val/load_efficiency)
            return val
        except Exception as exception:
            return 0

    def get_existing_energy_cost_full_load(self):
        return self.load_energy_cost(self.existing_full_load_eff)

    def get_proposed_energy_cost_full_load(self):
        return self.load_energy_cost(self.proposed_full_load_eff)

    def get_existing_energy_cost_three_fourth_load(self):
        return self.load_energy_cost(self.existing_three_fourth_load_eff,
                                     load_val=0.75)

    def get_proposed_energy_cost_three_fourth_load(self):
        return self.load_energy_cost(self.proposed_three_fourth_load_eff,
                                     load_val=0.75)

    def get_existing_energy_cost_half_load(self):
        return self.load_energy_cost(self.existing_half_load_eff,
                                     load_val=0.5)

    def get_proposed_energy_cost_half_load(self):
        return self.load_energy_cost(self.proposed_half_load_eff,
                                     load_val=0.5)

    def get_purchase_price_diff(self):
        return round(self.proposed_motor_purchase_price -
                     self.existing_motor_purchase_price)

    def get_energy_cost_full_load_diff(self):
        return round(self.get_existing_energy_cost_full_load() -
                     self.get_proposed_energy_cost_full_load())

    def get_energy_cost_three_fourth_load_diff(self):
        return round(self.get_existing_energy_cost_three_fourth_load() -
                     self.get_proposed_energy_cost_three_fourth_load())

    def get_energy_cost_half_load_diff(self):
        return round(self.get_existing_energy_cost_half_load() -
                     self.get_proposed_energy_cost_half_load())

    def was_recent(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)
    was_recent.admin_order_field = 'start_date'
    was_recent.boolean = True
    was_recent.short_description = 'Recently Joined?'

    def __str__(self):
        return self.motor_name

    def save(self, *args, **kwargs):
        self.start_date = datetime.datetime.utcnow()
        super(PremiumEfficiency, self).save(*args, **kwargs)

    class Meta:
        ordering = ('motor_name',)
