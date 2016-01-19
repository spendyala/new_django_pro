from django.db import models

# Create your models here.
from django.utils import timezone
import arrow
import datetime

from clients.models import Client


class BoilerBlowdown(models.Model):
    client = models.ForeignKey(Client)
    boiler_blowdown_name = models.CharField('Boiler Blowdown Reduction and Recovery',
                                            max_length=128,
                                            default='Boiler_')
    # client.gas_rate = models.FloatField('Gas Rate', default=0)
    # client.water_rate = models.FloatField('Water Rate', default=0)
    makeup_water_temperature = models.FloatField('Makeup Water Temperature',
                                                 default=0)
    # Reduce Blowdown Flow Rate
    existing_blowdown_frequency_per_day = models.FloatField('Existing Blowdown Frequency (Per Day)',
                                                            default=0)
    existing_blowdown_rate_gpm = models.FloatField('Existing Blowdown Rate (GPM)',
                                                   default=0)
    existing_blowdown_duration_mins = models.FloatField('Existing Blowdown Duration (minutes)',
                                                        default=0)
    existing_days_of_operation = models.FloatField('Existing Days of Operation',
                                                   default=0)
    existing_discharge_temp_in_f = models.FloatField('Existing Discharge Temp (F)',
                                                     default=0)

    proposed_blowdown_frequency_per_day = models.FloatField('Proposed Blowdown Frequency (Per Day)',
                                                            default=0)
    proposed_blowdown_rate_gpm = models.FloatField('Proposed Blowdown Rate (GPM)',
                                                   default=0)
    proposed_blowdown_duration_mins = models.FloatField('Proposed Blowdown Duration (minutes)',
                                                        default=0)
    proposed_days_of_operation = models.FloatField('Proposed Days of Operation',
                                                   default=0)
    proposed_discharge_temp_in_f = models.FloatField('Proposed Discharge Temp (F)',
                                                     default=0)
    # Provided Blowdown Heat Recovery
    existing_heat_recovery_efficiency_perc = models.FloatField('Existing Heat Recovery Efficiency',
                                                               default=0)

    proposed_heat_recovery_efficiency_perc = models.FloatField('Proposed Heat Recovery Efficiency',
                                                               default=0)

    start_date = models.DateTimeField('Registered Date')
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='boiler_blowdown')

    # Methods
    # Existing
    def get_existing_blowdown_gallons_per_day(self):
        return round(self.existing_blowdown_rate_gpm *
                     self.existing_blowdown_frequency_per_day *
                     self.existing_blowdown_duration_mins, 2)

    def get_existing_annual_quantity_gals(self):
        return round(self.existing_days_of_operation *
                     self.get_existing_blowdown_gallons_per_day(), 2)

    def get_existing_annual_quantity_lbs(self):
        return round(self.get_existing_annual_quantity_gals() * 8.33, 2)

    def get_existing_blowdown_energy_loss_btuh(self):
        return round(self.get_existing_annual_quantity_lbs() *
                     (self.existing_discharge_temp_in_f -
                      self.makeup_water_temperature), 2)

    def get_existing_energy_loss_therm(self):
        return round(self.get_existing_blowdown_energy_loss_btuh()/100000.0, 2)

    def get_existing_blowdown_energy_loss_therm(self):
        return self.get_existing_energy_loss_therm()

    def get_existing_overflow_cost(self):
        return round(self.get_existing_blowdown_energy_loss_therm() *
                     self.client.gas_rate, 2)

    def get_existing_makeup_water_quantity(self):
        return self.get_existing_annual_quantity_gals()

    def get_existing_makeup_water_cost(self):
        return round(self.get_existing_makeup_water_quantity() *
                     self.client.water_rate, 2)

    def get_existing_gas_and_water_cost(self):
        return round(self.get_existing_overflow_cost() +
                     self.get_existing_makeup_water_cost(), 2)

    def get_existing_blowdown_energy_recovery_therms(self):
        return round(self.get_existing_blowdown_energy_loss_therm() *
                     (self.existing_heat_recovery_efficiency_perc/100), 2)

    def get_existing_total(self):
        return round(self.get_existing_blowdown_energy_recovery_therms() *
                     self.client.gas_rate, 2)

    # Proposed
    def get_proposed_blowdown_gallons_per_day(self):
        return round(self.proposed_blowdown_rate_gpm *
                     self.proposed_blowdown_frequency_per_day *
                     self.proposed_blowdown_duration_mins, 2)

    def get_proposed_annual_quantity_gals(self):
        return round(self.proposed_days_of_operation *
                     self.get_proposed_blowdown_gallons_per_day(), 2)

    def get_proposed_annual_quantity_lbs(self):
        return round(self.get_proposed_annual_quantity_gals() * 8.33, 2)

    def get_proposed_blowdown_energy_loss_btuh(self):
        return round(self.get_proposed_annual_quantity_lbs() *
                     (self.proposed_discharge_temp_in_f -
                      self.makeup_water_temperature), 2)

    def get_proposed_energy_loss_therm(self):
        return round(self.get_proposed_blowdown_energy_loss_btuh()/100000.0, 2)

    def get_proposed_overflow_cost(self):
        return round(self.get_proposed_blowdown_energy_loss_therm() *
                     self.client.gas_rate, 2)

    def get_proposed_makeup_water_quantity(self):
        return self.get_proposed_annual_quantity_gals()

    def get_proposed_makeup_water_cost(self):
        return round(self.get_proposed_makeup_water_quantity() *
                     self.client.water_rate, 2)

    def get_proposed_gas_and_water_cost(self):
        return round(self.get_proposed_overflow_cost() +
                     self.get_proposed_makeup_water_cost(), 2)

    def get_proposed_blowdown_energy_loss_therm(self):
        return self.get_proposed_energy_loss_therm()

    def get_proposed_blowdown_energy_recovery_therms(self):
        return round(self.get_proposed_blowdown_energy_loss_therm() *
                     (self.proposed_heat_recovery_efficiency_perc/100), 2)

    def get_proposed_total(self):
        return round(self.get_proposed_blowdown_energy_recovery_therms() *
                     self.client.gas_rate, 2)

    def get_savings_gas(self):
        return round(self.get_existing_overflow_cost() -
                     self.get_proposed_overflow_cost(), 2)

    def get_savings_water(self):
        return round(self.get_existing_makeup_water_cost() -
                     self.get_proposed_makeup_water_cost(), 2)

    def get_savings_gas_and_water(self):
        return round(self.get_existing_gas_and_water_cost() -
                     self.get_proposed_gas_and_water_cost(), 2)

    def get_savings_total(self):
        return round(self.get_existing_total() -
                     self.get_proposed_total(), 2)

    def was_recent(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)
    was_recent.admin_order_field = 'start_date'
    was_recent.boolean = True
    was_recent.short_description = 'Recently Joined?'

    def __str__(self):
        return self.boiler_blowdown_name

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(BoilerBlowdown, self).save(*args, **kwargs)

    class Meta:
        ordering = ('boiler_blowdown_name',)
