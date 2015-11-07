import csv
from main_app.settings import BASE_DIR

def get_steam_trap_data():
    first = True
    header = []
    steam_trap_dict = {}
    with open('%s/supporting_files/steam_trap.csv' % (BASE_DIR, ),
              'rbU') as csvfile:
        steam_trap_raw = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in steam_trap_raw:
            if first:
                header = row
                first = False
            else:
                int_row = [int(x) for x in row]
                steam_trap_dict[int(row[0])] = dict(zip(header, int_row))

    return steam_trap_dict


def get_trap_size_data():
    first = True
    header = []
    trap_size_dict = {}
    with open('%s/supporting_files/trap_orifice_table.csv' % (BASE_DIR, ),
              'rbU') as csvfile:
        trap_size_raw = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in trap_size_raw:
            if first:
                header = row
                first = False
            else:
                int_row = [float(x) for x in row]
                trap_size_dict[float(row[0])] = dict(zip(header, int_row))

    return trap_size_dict

if __name__ == '__main__':
    print get_steam_trap_data()
    print get_trap_size_data()
