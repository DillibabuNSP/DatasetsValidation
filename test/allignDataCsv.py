import csv


def parse_edi_data(edi_file_path, output_csv_path):
    with open(edi_file_path, 'r') as edi_file:
        edi_data = edi_file.read()

    edi_segments = edi_data.strip().split('~')
    parsed_edi_data = []

    for segment in edi_segments:
        elements = segment.split('*')
        parsed_edi_data.append(elements)

    # Create a dictionary to group data by their names
    grouped_data = {}
    max_elements = 0  # Track the maximum number of elements

    for elements in parsed_edi_data:
        name = elements[0]  # Assuming the name is in the first element
        if name not in grouped_data:
            grouped_data[name] = []
        grouped_data[name].extend(elements[1:])  # Exclude the name itself

        # Update the maximum number of elements
        max_elements = max(max_elements, len(elements) - 1)

    # Create a list of lists for writing to CSV, aligning data by name
    rows = [['Name'] + [f'Data_{i + 1}' for i in range(max_elements)]]

    for name, data in grouped_data.items():
        row = [name] + data + [''] * (max_elements - len(data))
        rows.append(row)

    # Transpose the data to have names in columns
    transposed_data = list(map(list, zip(*rows)))

    # Write the transposed data to a CSV file
    with open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(transposed_data)


# Usage
edi_file_path = 'C:\\Users\\dillibabu.nsp\\Downloads\\20230727200135302.txt'
output_csv_path = 'alignedCSV.csv'
parse_edi_data(edi_file_path, output_csv_path)
