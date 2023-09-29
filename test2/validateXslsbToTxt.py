from pyxlsb import open_workbook

# Step 1: Read data from the binary Excel file (XLSB)
excel_file_path = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230725155251122.xlsb'  # Replace with your XLSB file path

# Open the XLSB workbook
with open_workbook(excel_file_path) as wb:
    with wb.get_sheet(1) as sheet:  # Assuming the data is in the first sheet
        excel_data = []
        for row in sheet.rows():
            row_data = [item.v for item in row]
            excel_data.append(row_data)

# Step 2: Read data from the text file
text_file_path = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt'  # Replace with your text file path
with open(text_file_path, 'r') as file:
    text_data = file.read().splitlines()

# Step 3: Validate data
validation_result = []
for row_data in excel_data:
    # Assuming the "Container#" column is in index 0
    container_number = row_data[0]

    # Check if the container number exists in the text data
    if container_number in text_data:
        validation_result.append("Valid")
    else:
        validation_result.append("Invalid")

# Print or further process the validation results
for i, row_data in enumerate(excel_data):
    print(f"Container#: {row_data[0]}, Validation Result: {validation_result[i]}")
