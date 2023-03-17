import csv
import json

data = []
with open('aapl.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

with open('aapl.json', 'w') as json_file:
    json.dump(data, json_file)