import csv
import json

#read csv file
with open('all_stocks_basic_data.csv', 'r', encoding='utf-8') as csvf:
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf)

    #convert each csv row into python dict
    for row in csvReader:
        #add this python dict to json array
        jsonArray.append(row)

#convert python jsonArray to JSON String and write to file
with open('all_stocks_basic_data.csv', 'w', encoding='utf-8') as jsonf:
    jsonString = json.dumps(jsonArray, indent=4)
    jsonf.write(jsonString)