# import openpyxl

from openpyxl import Workbook
import StringIO
from django.http import HttpResponse


class SteamLeakExcel(object):
    def __init__(self, steam_leak=None):
        self.steam_leak = steam_leak
        self.wb = Workbook()
        self.ws = self.wb.active
        self.out = StringIO.StringIO()
        self.headers_dict = {
            'A1': 'Leak #',
            'B1': 'Location/Description',
            'C1': 'Boiler Efficiency',
            'D1': 'Therms (Therm Rate)',
            'E1': 'Pressure (psig)',
            'F1': 'Absolute Pressure (psia)',
            'G1': 'Size Leak (inch)',
            'H1': 'Steam Loss (pph)',
            'I1': 'Steam Energy (Btu/lb)',
            'J1': 'Gas Usage (Therms/hour)',
            'K1': 'Cost / Hour',
            'L1': 'Hours of Operation',
            'M1': 'Cost / Year'
        }
        self.data_column = {
            'A': 'steam_leak_number',
            'B': 'location_description',
            'C': 'boiler_efficiency',
            'D': 'get_therm_rate',
            'E': 'pressure_in_psig',
            'F': 'absolute_pressure_psia',
            'G': 'size_leak_in_inch',
            'H': 'get_steam_loss_pph',
            'I': 'get_steam_energy_btu_per_lb',
            'J': 'get_gas_usage_therms_per_hour',
            'K': 'get_cost_per_hour',
            'L': 'hours_of_operation',
            'M': 'get_cost_per_year'
        }
        self.make_excel_headers()
        self.make_excel_data()

    def make_excel_headers(self):
        for each_cell in self.headers_dict:
            self.ws[each_cell] = self.headers_dict[each_cell]
            column = each_cell.replace('1', '')
            self.ws.column_dimensions[column].width = len(
                self.headers_dict[each_cell])

    def make_excel_data(self):
        count = 2
        for each_steam_leak in self.steam_leak:
            for each_column in self.data_column:
                cell_val = '%s%s' % (each_column, count)
                self.ws[cell_val] = each_steam_leak.get(
                    self.data_column[each_column])
            count += 1

    def get_excel_raw(self):
        # self.wb.read_only = True
        self.wb.save(self.out)
        self.out.seek(0)
        response = HttpResponse(self.out,
                                content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = ('attachment; filename="%s"'
                                           % 'SteamLeak.xlsx')
        return response


class SteamTrapExcel(object):
    def __init__(self, steam_trap=None):
        self.steam_trap = steam_trap
        self.wb = Workbook()
        self.ws = self.wb.active
        self.out = StringIO.StringIO()
        self.headers_dict = {
            'A1': 'Failed Trap #',
            'B1': 'Location/Description',
            'C1': 'Boiler Efficiency',
            'D1': 'Therms (Therm Rate)',
            'E1': 'Pressure (psig)',
            'F1': 'Absolute Pressure (psia)',
            'G1': 'Trap Pipe Size (inch)',
            'H1': 'Size Trap (inch)',
            'I1': 'Steam Loss (pph)',
            'J1': 'Steam Energy (Btu/lb)',
            'K1': 'Gas Usage (Therms/hour)',
            'L1': 'Cost / Hour',
            'M1': 'Hours of Operation',
            'N1': 'Cost / Year'
        }
        self.data_column = {
            'A': 'steam_trap_number',
            'B': 'location_description',
            'C': 'boiler_efficiency',
            'D': 'get_therm_rate',
            'E': 'pressure_in_psig',
            'F': 'absolute_pressure_psia',
            'G': 'trap_pipe_size',
            'H': 'size_trap_orifice',
            'I': 'get_steam_loss_pph',
            'J': 'get_steam_energy_btu_per_lb',
            'K': 'get_gas_usage_therms_per_hour',
            'L': 'get_cost_per_hour',
            'M': 'hours_of_operation',
            'N': 'get_cost_per_year'
        }
        self.make_excel_headers()
        self.make_excel_data()

    def make_excel_headers(self):
        for each_cell in self.headers_dict:
            self.ws[each_cell] = self.headers_dict[each_cell]
            column = each_cell.replace('1', '')
            self.ws.column_dimensions[column].width = len(
                self.headers_dict[each_cell])

    def make_excel_data(self):
        count = 2
        for each_steam_trap in self.steam_trap:
            for each_column in self.data_column:
                cell_val = '%s%s' % (each_column, count)
                self.ws[cell_val] = each_steam_trap.get(
                    self.data_column[each_column])
            count += 1

    def get_excel_raw(self):
        # self.wb.read_only = True
        self.wb.save(self.out)
        self.out.seek(0)
        response = HttpResponse(self.out,
                                content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = ('attachment; filename="%s"'
                                           % 'SteamTrap.xlsx')
        return response


class BoilerDatacollectionExcel(object):
    def __init__(self, boiler_datacollection=None):
        self.boiler_datacollection = boiler_datacollection
        self.wb = Workbook()
        self.ws = self.wb.active
        self.out = StringIO.StringIO()
        self.headers_dict = {
            'A1': 'Boiler Data Collection Name',
            'B1': 'Boiler capacity (MBH)',
            'C1': 'Yearly Hours of Operation',
            'D1': 'Separately Meter',
            'E1': 'Make Up Water Log/ Separate Bill',
            'F1': 'Number of Steam Traps',
            'G1': 'Date Last Steam Trap\nAudit Performed',
            'H1': 'Is the Header Insulated',
            'I1': 'Percent of Condensate\nthat returns to Boiler',
            'J1': 'Aerator Tank Temperature',
            'K1': 'Aerator Tank Pressure',
            'L1': 'Production Pressure',
        }
        self.data_column = {
            'A': 'name',
            'B': 'boiler_capacity_mbh',
            'C': 'hours_of_operation',
            'D': 'separately_meter',
            'E': 'make_up_water_log_separate_bill',
            'F': 'no_of_steam_traps',
            'G': 'steam_trap_audit_performed',
            'H': 'is_the_header_insulated',
            'I': 'percentage_condensate_that_returns_to_boiler',
            'J': 'aerator_tank_temp',
            'K': 'aerator_tank_pressure',
            'L': 'production_pressure',
        }
        self.make_excel_headers()
        self.make_excel_data()

    def make_excel_headers(self):
        for each_cell in self.headers_dict:
            self.ws[each_cell] = self.headers_dict[each_cell]
            column = each_cell.replace('1', '')
            self.ws.column_dimensions[column].width = len(
                self.headers_dict[each_cell])

    def make_excel_data(self):
        count = 2
        for each_boiler_datacollection in self.boiler_datacollection:
            for each_column in self.data_column:
                cell_val = '%s%s' % (each_column, count)
                column_val = self.data_column[each_column]
                if column_val in [
                        'separately_meter',
                        'make_up_water_log_separate_bill',
                        'is_the_header_insulated']:
                    self.ws[cell_val] = ('Yes' if
                                         each_boiler_datacollection.get(
                                            column_val)
                                         else 'No')
                else:
                    self.ws[cell_val] = each_boiler_datacollection.get(
                        column_val)
            count += 1

    def get_excel_raw(self):
        # self.wb.read_only = True
        self.wb.save(self.out)
        self.out.seek(0)
        response = HttpResponse(self.out,
                                content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = ('attachment; filename="%s"'
                                           % 'BoilerDatacollection.xlsx')
        return response
