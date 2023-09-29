from pyxlsb import open_workbook

# Step 1: Read Data from the Text File
with open('C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt', 'r') as db_file:
    db_data = [line.strip() for line in db_file.readlines()]

# Step 2: Read Data from the XLSB File
excel_data = []
with open_workbook('C:\\Users\\dillibabu.nsp\\Downloads\\20230725155251122.xlsb') as wb:  # Replace with your XLSB file path
    with wb.get_sheet(1) as sheet:  # Assuming you're working with the first sheet
        for row in sheet.rows():
            excel_data.append([item.v for item in row])

# Step 3: Compare the Data
mismatches = []  # To store mismatched data

for idx, (db_value, excel_row) in enumerate(zip(db_data, excel_data), start=1):
    for excel_value in excel_row:
        if db_value != excel_value:
            mismatches.append((idx, db_value, excel_value))

# Step 4: Handle Data Mismatches (Modify this part as needed)
if mismatches:
    print("Data mismatches found:")
    for idx, db_value, excel_value in mismatches:
        print(f"Row {idx}, Database value: {db_value}, Excel value: {excel_value}")
else:
    print("No data mismatches found.")

# Step 5: Error Handling (Implement as needed)
# You can add error handling here for file not found or other exceptions.

# Step 6: Close Resources (Not needed here)
