import csv
import json

data = []
with open('all_stocks_basic_data.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

with open('all_stocks_basic_data.json', 'w') as json_file:
    json.dump(data, json_file)