import csv

with open('steam_trap.csv', 'rbU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print ','.join(row)
