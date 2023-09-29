import openpyxl


# Function to parse EDI data
def parse_edi_data(edi_file_path):
    with open(edi_file_path, 'r') as edi_file:
        edi_data = edi_file.read()

    edi_segments = edi_data.strip().split('~')
    parsed_edi_data = []

    for segment in edi_segments:
        elements = segment.split('*')
        parsed_edi_data.append(elements)

    return parsed_edi_data


# Function to perform the comparison
def compare_edi_with_excel(parsed_edi_data, excel_file_path):
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active

    # Assuming you have a unique identifier or key field in both EDI and Excel data
    for edi_record in parsed_edi_data:
        edi_key_field = edi_record[0]  # Replace with the actual key field from EDI
        for row in sheet.iter_rows(min_row=2, values_only=True):
            excel_key_field = row[0]  # Replace with the actual key field column in Excel
            if edi_key_field == excel_key_field:
                print("Match found!")
    workbook.close()


# Main program
def main():
    edi_file_path = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt'  # Replace with the path to your EDI data file
    excel_file_path = 'C:\\Users\\dillibabu.nsp\\PycharmProjects\\DatasetsValidation\\test\\20230725155251122.xlsx'  # Replace with the path to your Excel file

    parsed_edi_data = parse_edi_data(edi_file_path)
    compare_edi_with_excel(parsed_edi_data, excel_file_path)


if __name__ == "__main__":
    main()
