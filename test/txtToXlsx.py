import csv
from openpyxl import Workbook

# Open the text file for reading
with open('C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt', 'r') as text_file:
    # Create a new Excel workbook and sheet
    workbook = Workbook()
    sheet = workbook.active

    # Read the text file line by line
    for line in text_file:
        # Split the line using the asterisk (*) delimiter
        data = line.strip().split('*')

        # Write the data to the Excel sheet
        sheet.append(data)

    # Save the Excel workbook to a file
    workbook.save('output.xlsx')

print("Data has been successfully written to output.xlsx")
