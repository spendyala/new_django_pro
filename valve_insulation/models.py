from django.db import models

from django.utils import timezone
import arrow
import datetime

from clients.models import Client


NPS_PIPE_SIZES = [(0.5, 0.5),
                  (0.75, 0.75),
                  (1.0, 1.0),
                  (1.25, 1.25),
                  (1.5, 1.5),
                  (2.0, 2.0),
                  (2.5, 2.5),
                  (3.0, 3.0),
                  (3.5, 3.5),
                  (4.0, 4.0),
                  (4.5, 4.5),
                  (5.0, 5.0),
                  (6.0, 6.0),
                  (7.0, 7.0),
                  (8.0, 8.0),
                  (9.0, 9.0),
                  (10.0, 10.0),
                  (12.0, 12.0),
                  (14.0, 14.0),
                  (16.0, 16.0),
                  (18.0, 18.0),
                  (20.0, 20.0),
                  (24.0, 24.0),
                  (30.0, 30.0),
                  (36.0, 36.0),
                  (48.0, 48.0)]

WORKING_FLUID = [('Steam', 'Steam'),
                 ('Condensate', 'Condensate'),
                 ('Heating Hot Water', 'Heating Hot Water'),
                 ('Domestic Hot Water', 'Domestic Hot Water')]

LOCATION_OPTIONS = [('Indoors', 'Indoors'),
                    ('Outdoors', 'Outdoors')]

BASE_METAL_CHOICES = [('Steel', 'Steel'),
                      ('Copper', 'Copper'),
                      ('PVC', 'PVC')]

INSULATION_CHOICES = [('850', '850F Mineral Fiber PIPE, Type I, C547-11'),
                      ('1200', '1200F Mineral Fiber PIPE, Types II and III, C547-11'),
                      ('1000', '1000F Mineral Fiber PIPE, Type IV, C547-11'),
                      ('Poly', 'Polystyrene PIPE, Type XIII, C578-11b')]

INSULATION_THICKNESS_OPT = [(0.5, 0.5),
                            (0.75, 0.75),
                            (1, 1),
                            (1.5, 1.5),
                            (2, 2),
                            (2.5, 2.5),
                            (3, 3),
                            (3.5, 3.5),
                            (4, 4),
                            (4.5, 4.5),
                            (5, 5),
                            (6, 6),
                            (7, 7),
                            (8, 8)]
#   ('', ''),


class ValveInsulation(models.Model):
    client = models.ForeignKey(Client)
    start_date = models.DateTimeField('Registered Date')
    name = models.CharField('Valve Insulation Name',
                            default='',
                            max_length=128)
    # Existing Pipe Conditions
    valve_type = models.CharField('Valve Type',
                                  default='',
                                  max_length=128)
    quantity = models.IntegerField('Quantity', default=0)
    nps_pipe_size_inches = models.FloatField('NPS Pipe Size (inches)',
                                             choices=NPS_PIPE_SIZES,
                                             default=0.5)
    working_fluid = models.CharField('Working Fluid',
                                     choices=WORKING_FLUID,
                                     max_length=128,
                                     default='Steam')
    process_temp_or_pressure = models.IntegerField(
        'Process Temp or Pressure',
        default=0,
        help_text=('Noel Chambers: Select the temperature of the working fluid'
                   ' if the fluid a liquid. If the working fluid is steam '
                   'please select the working pressure of the system.'))
    system_efficiency = models.FloatField('System Efficiency',
                                          default=80)
    ambient_temp = models.FloatField('Ambient Temp',
                                     default=70)
    system_hours_per_year = models.FloatField('System Hours / Year',
                                              default=8760)
    wind_speed_mph = models.FloatField('Wind Speed (MPH)',
                                       default=0)
    location = models.CharField('Location',
                                default='Indoors',
                                max_length=128,
                                choices=LOCATION_OPTIONS)
    base_metal = models.CharField('Base Metal',
                                  default='Steel',
                                  max_length=128,
                                  choices=BASE_METAL_CHOICES)
    # Proposed Insulation
    insulation = models.CharField('Insulation',
                                  default='850',
                                  max_length=128,
                                  choices=INSULATION_CHOICES)
    insulation_thickness = models.FloatField('Insulation Thickness',
                                             default=0.5,
                                             choices=INSULATION_THICKNESS_OPT)
    jacket_material = models.CharField('Jacket Material',
                                       default='',
                                       max_length=128)
    notes = models.TextField('Notes', default='') 
    owner = models.ForeignKey('auth.User', related_name='valve_insulation')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # TODO: add owner
        self.start_date = datetime.datetime.utcnow()
        super(ValveInsulation, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
