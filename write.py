import csv

with open('names.csv','w') as csvfile:
    fieldnames = ['firstName', 'lastName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'firstName':'Bob', 'lastName':'Pegas'})
    writer.writerow({'firstName':'Vasya', 'lastName':'Prostachok'})
    writer.writerow({'firstName':'Spam', 'lastName':'Eggs'})
