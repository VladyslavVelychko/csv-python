import csv

f = open("data2.csv", "w", encoding="utf-8", newline="")
writer = csv.writer(f)
writer.writerow(['Vladyslav', '22', 'Programmer'])
writer.writerow(['Andriy','22','Bezdelnik'])

f.close()
