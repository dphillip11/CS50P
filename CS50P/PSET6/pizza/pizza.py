from tabulate import tabulate
import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Incorrect Usage!")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")

table =[]

reader = csv.reader(file)

for line in reader:
    table.append(line)

file.close()

print(tabulate(table, headers="firstrow", tablefmt="grid"))