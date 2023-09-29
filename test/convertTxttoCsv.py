import csv


def parse_edi_data(edi_file_path, output_csv_path):
    with open(edi_file_path, 'r') as edi_file:
        edi_data = edi_file.read()

    edi_segments = edi_data.strip().split('~')
    parsed_edi_data = []

    for segment in edi_segments:
        elements = segment.split('*')
        parsed_edi_data.append(elements)

    # Write the parsed EDI data to a CSV file
    with open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(parsed_edi_data)


edi_file_path = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt'
output_csv_path = 'output.csv'
parse_edi_data(edi_file_path, output_csv_path)
