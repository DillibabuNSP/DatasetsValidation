import pyxlsb
from openpyxl import Workbook

# Input XLSB file path
xlsb_file = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230725155251122.xlsb'

# Output XLSX file path
xlsx_file = '20230725155251122.xlsx'

# Create a new XLSX workbook
workbook = Workbook()
xlsx_sheet = workbook.active

# Open the XLSB file
with pyxlsb.open_workbook(xlsb_file) as xlsb:
    with xlsb.get_sheet(1) as sheet:
        for row in sheet.rows():
            # Read data from XLSB and write it to XLSX
            xlsx_sheet.append([item.v for item in row])

# Save the XLSX workbook to a file
workbook.save(xlsx_file)

print(f'XLSB file "{xlsb_file}" converted to XLSX file "{xlsx_file}" successfully.')
