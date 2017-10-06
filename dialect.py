#!/usr/bin/python3

import csv
csv.register_dialect("hashes", delimiter="@")

f = open('items3.csv', 'w')
with f:
    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("another_pens", 24))
    writer.writerow(("desks", 15))
    writer.writerow(("boards", 8))
