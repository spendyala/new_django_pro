from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client

COMPRESSOR_TYPE = [('REC', 'Reciprocating'),
                   ('ROS', 'Rotary Screw'),
                   ('ROC', 'Rotary Centrifugal')]

VFD_CONTROL_TYPE = [(1, 'YES'),
                    (2, 'NO')]

class AirCompressor(models.Model):
    start_date = models.DateTimeField('Registered Date')
    client = models.ForeignKey(Client)
    air_compressor = models.CharField('Air Compressor',
                                      default='',
                                      max_length=128)
    customer_name = models.CharField('Customer Name',
                                     default='',
                                     max_length=128)
    customer_site = models.CharField('Customer Site',
                                     default='',
                                     max_length=128)
    project_name = models.CharField('Project Name',
                                    default='',
                                    max_length=128)
    # electric_utility_rate = models.FloatField(
    #     'Electric Utility Rate (per kWh)',
    #     default=0)
    compressor_name = models.CharField('Compressor Name',
                                       default='',
                                       max_length=128)
    manufacturer = models.CharField('Manufacturer',
                                    default='',
                                    max_length=128)
    model_info = models.CharField('Model #',
                                  default='',
                                  max_length=128)
    serial_info = models.CharField('Serial #',
                                   default='',
                                   max_length=128)
    compressor_type = models.CharField('Compressor Type',
                                       choices=COMPRESSOR_TYPE,
                                       max_length=256,
                                       default='REC')
    vfd_speed_control = models.IntegerField('VFD Speed Control',
                                            choices=VFD_CONTROL_TYPE,
                                            default=1)
    vfd_90_t_fitting = models.IntegerField('90Degree T-fitting',
                                           choices=VFD_CONTROL_TYPE,
                                           default=1)
    # Inputs
    nameplate_horsepower = models.FloatField('Nameplate Horsepower (HP)',
                                             default=0)
    nameplate_max_flow = models.FloatField('Nameplate Maximum Flow (CFM)',
                                           default=0)
    measured_actual_flow = models.FloatField('Measured Actual Flow (GPM)',
                                             default=0)
    measured_line_pressure = models.FloatField('Measured Line Pressure (PSI)',
                                               default=0)
    annual_hours_of_operation = models.FloatField(
        'Annual Hours of Operation (Hours)',
        default=0)
    reduce_line_pressure_to = models.FloatField(
        'Reduced Line Pressure: To (PSI)',
        default=0)
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='air_compressor')

    def get_hourly_kwh_consumed(self):
        return round((self.nameplate_horsepower * 0.746)/0.9, 3)

    def get_hourly_cost_of_operation(self):
        return round(self.get_hourly_kwh_consumed() *
                     self.client.electric_rate, 2)

    def get_annual_cost_of_operation(self):
        return round(
            self.get_hourly_cost_of_operation() *
            self.annual_hours_of_operation, 2)

    def get_reduced_line_pressure_from(self):
        return self.measured_line_pressure

    def get_proposed_pressure_decrease(self):
        return round(self.get_reduced_line_pressure_from() -
                     self.reduce_line_pressure_to, 2)

    def get_estimated_ann_savings_per_2_psi_reduction(self):
        return round(self.get_annual_cost_of_operation() * 0.01, 2)

    def get_annual_cost_before_psi_setback(self):
        return self.get_annual_cost_of_operation()

    def get_annual_cost_after_psi_setback(self):
        return round(self.get_annual_cost_of_operation() -
                     ((self.get_proposed_pressure_decrease() / 2.0) *
                      self.get_estimated_ann_savings_per_2_psi_reduction()))

    def get_annual_savings_after_psi_setback(self):
        return round(self.get_annual_cost_before_psi_setback() -
                     self.get_annual_cost_after_psi_setback())

    def get_estimated_air_leak_25_percent_of_costs(self):
        return round(self.get_annual_cost_of_operation() * 0.25)

    def get_estimated_air_leak_40_percent_of_costs(self):
        return round(self.get_annual_cost_of_operation() * 0.4)

    def was_recent(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)
    was_recent.admin_order_field = 'start_date'
    was_recent.boolean = True
    was_recent.short_description = 'Recently Joined?'

    def __str__(self):
        return self.air_compressor

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(AirCompressor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('compressor_name',)
