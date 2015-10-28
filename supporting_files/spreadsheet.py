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
			'D': 'therm_rate',
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
				self.ws[cell_val] = each_steam_leak.get(self.data_column[each_column])
			count += 1

	def get_excel_raw(self):
		#self.wb.read_only = True
		self.wb.save(self.out)
		self.out.seek(0)
		response = HttpResponse(self.out, content_type='application/vnd.ms-excel')
		response['Content-Disposition'] = 'attachment; filename="%s"' % 'SteamLeak.xlsx'
		return response
