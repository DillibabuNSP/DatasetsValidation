import csv
import openpyxl

input_file = "C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt"
output_file = "newcsvfile.csv"

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)

wb.save(output_file)
