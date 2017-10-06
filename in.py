import csv
with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['firstName'], row['lastName'])
        print(row)
