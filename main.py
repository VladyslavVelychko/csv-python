import csv

f = open("data.csv", "r", encoding="utf-8", newline="")
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()
