from pyxlsb import open_workbook


# Function to read data from the XLSB file
def read_xlsb_file(file_path):
    xlsb_workbook = open_workbook(file_path)
    with xlsb_workbook.get_sheet(1) as sheet:
        xlsb_data = []
        for row in sheet.rows():
            row_data = [item.v for item in row]
            xlsb_data.append(row_data)

    return xlsb_data


# Function to read data from the database file
def read_database_file(file_path):
    with open(file_path, 'r') as file:
        database_data = file.readlines()

    return database_data


# Function to compare data between database and XLSB
def compare_data(database_data, xlsb_data):
    mismatches = []

    # Iterate through rows in the database file and XLSB data
    for i, (db_row, xlsb_row) in enumerate(zip(database_data, xlsb_data), start=1):
        db_values = db_row.strip().split('*')

        # Check if the number of columns is different
        if len(db_values) != len(xlsb_row):
            print(f"Row {i}:")
            print(f"Database row has {len(db_values)} columns: {db_values}")
            print(f"XLSB row has {len(xlsb_row)} columns: {xlsb_row}")
            mismatches.append(f"Row {i}: Column count mismatch")

    return mismatches


if __name__ == "__main__":
    database_file = "C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt"
    xlsb_file = "C:\\Users\\dillibabu.nsp\\Downloads\\20230725155251122.xlsb"

    # Read data from files
    database_data = read_database_file(database_file)
    xlsb_data = read_xlsb_file(xlsb_file)

    # Compare data
    mismatches = compare_data(database_data, xlsb_data)

    # Display mismatches
    if mismatches:
        print("\nData mismatches found:")
        for mismatch in mismatches:
            print(mismatch)
    else:
        print("No data mismatches found.")
