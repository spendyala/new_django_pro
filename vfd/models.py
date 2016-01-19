from django.db import models
from django.utils import timezone
import datetime
from clients.models import Client

MONTHS = [('JAN', 'January'),
          ('FEB', 'February'),
          ('MAR', 'March'),
          ('APR', 'April'),
          ('MAY', 'May'),
          ('JUN', 'June'),
          ('JUL', 'July'),
          ('AUG', 'August'),
          ('SEP', 'September'),
          ('OCT', 'October'),
          ('NOV', 'November'),
          ('DEC', 'December')]


class VfdMotor(models.Model):
    client = models.ForeignKey(Client)
    vfd_name = models.CharField('Client VFD Name', max_length=256)
    # client.electric_rate = models.FloatField('Cost (per kWh)', default=0.00)
    motor_horse_pwr = models.FloatField('Motor HP', default=0.00)
    existing_motor_efficiency = models.FloatField('Existing Motor Eff. %',
                                                  default=0)
    proposed_vfd_efficiency = models.FloatField('Proposed VFD Eff. %',
                                                default=0.0)
    motor_load = models.FloatField('Motor Load %', default=0)

    start_date = models.DateTimeField('Registered Date')
    notes = models.TextField('Notes', default='')
    owner = models.ForeignKey('auth.User', related_name='vfd_motor')

    def __str__(self):
        return self.vfd_name

    def save(self, *args, **kwargs):
        self.start_date = datetime.datetime.utcnow()
        super(VfdMotor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('vfd_name',)


class VfdMotorDataPerMonth(models.Model):
    client_vfd = models.ForeignKey(VfdMotor)
    month = models.CharField('Month', max_length=3, choices=MONTHS)
    hours_of_operation = models.FloatField('Hours of operation', default=0)

    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User',
                              related_name='vfd_motor_data_per_month')

    def get_existing_kwh(self):
        try:
            val = float(1.0/self.client_vfd.existing_motor_efficiency)
            kwh = self.client_vfd.motor_horse_pwr * val
            kwh *= self.client_vfd.motor_load
            kwh *= 0.746
            kwh *= self.hours_of_operation
            kwh = round(kwh, 2)
        except Exception as exception:
            kwh = 0
        return kwh

    def get_existing_cost_of_operation(self):
        return round(self.get_existing_kwh() *
                     self.client_vfd.client.electric_rate, 2)

    def get_ui_name(self):
        return '%s' % (self.month.lower())

    def __str__(self):
        return '%s-%s' % (self.client_vfd.id, self.month)

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(VfdMotorDataPerMonth, self).save(*args, **kwargs)

    class Meta:
        ordering = ('client_vfd',)


class VfdMotorSetpointSelections(models.Model):
    client_vfd = models.ForeignKey(VfdMotor)
    speed_percent = models.FloatField('VFD Speed %', default=0)
    percent_of_time = models.FloatField('Percent Of Time (%)', default=0)

    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User', related_name='vfd_motor_setpoint_selections')

    def get_proposed_kwh(self):
        try:
            val = float(1.0/self.client_vfd.proposed_vfd_efficiency)
            # proposed_vfd_kwh = data['total_hours']
            proposed_kwh = self.percent_of_time
            proposed_kwh = round(proposed_kwh/100.0, 3)
            proposed_kwh *= self.speed_percent
            proposed_kwh = round(proposed_kwh/100.0, 3)
            proposed_kwh *= self.speed_percent
            proposed_kwh = round(proposed_kwh/100.0, 3)
            proposed_kwh *= self.speed_percent
            proposed_kwh *= self.client_vfd.motor_horse_pwr
            proposed_kwh *= val * 0.746
            proposed_kwh *= self.client_vfd.motor_load
            proposed_kwh = round(proposed_kwh/100.0, 3)
        except Exception as exception:
            proposed_kwh = 0
        return proposed_kwh

    def get_proposed_cost_of_operation(self):
        return self.get_proposed_kwh() * self.client_vfd.client.electric_rate

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(VfdMotorSetpointSelections, self).save(*args, **kwargs)

    class Meta:
        ordering = ('speed_percent',)


class MaterialsVFDMotor(models.Model):
    client_vfd = models.ForeignKey(VfdMotor)
    item = models.CharField('Item', max_length=160)
    supplier = models.CharField('Supplier', max_length=160)
    description = models.CharField('Description', max_length=500)
    ges_cost_each = models.FloatField('GES Cost Each', default=0.0)
    ges_markup = models.FloatField('GES Markup', default=0.0)
    quantity = models.FloatField('Quantity', default=0)

    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User', related_name='materials_vfd_motor')

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(MaterialsVFDMotor, self).save(*args, **kwargs)

    def get_ges_each_cost(self):
        try:
            each_material_price = round(self.ges_cost_each/self.ges_markup, 2)
        except Exception:
            each_material_price = 0
        return each_material_price

    def get_extended_cost(self):
        return self.quantity * self.get_ges_each_cost()

    class Meta:
        ordering = ('client_vfd',)


class LaborVFDMotor(models.Model):
    client_vfd = models.ForeignKey(VfdMotor)
    item = models.CharField('Item', max_length=160)
    vendor = models.CharField('Vendor', max_length=160)
    hourly_rate = models.FloatField('Hourly Rate', default=0)
    fixed_cost = models.FloatField('Fixed Cost', default=0)
    ges_cost = models.FloatField('GES Cost', default=0.0)
    ges_markup = models.FloatField('GES Markup', default=0.0)
    quantity = models.FloatField('Quantity', default=0)
    fixed_flag = models.BooleanField('Fixed Labor Flag', default=True)

    start_date = models.DateTimeField('Registered Date')
    owner = models.ForeignKey('auth.User', related_name='labor_vfd_motor')

    def save(self, *args, **kwargs):
        # TODO: add owner
        if not self.fixed_cost:
            self.fixed_flag = False
        self.start_date = datetime.datetime.utcnow()
        super(LaborVFDMotor, self).save(*args, **kwargs)

    def get_customer_price(self):
        try:
            labor_customer_price = int(round(self.ges_cost/self.ges_markup))
        except Exception as error:
            labor_customer_price = 0
        return labor_customer_price

    class Meta:
        ordering = ('client_vfd',)
