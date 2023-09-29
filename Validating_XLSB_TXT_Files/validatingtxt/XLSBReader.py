import pyxlsb


class XLSBReader:
    def __init__(self, xlsb_file_path):
        """
        Initialize the XLSBReader with the given xlsb_file_path.

        Args:
            xlsb_file_path (str): The path to the XLSB file.
        """
        self.xlsb_file_path = xlsb_file_path

    def read_xlsb(self, sheet_index, headings_to_search):
        """
        Read the specified sheet in the XLSB file and extract data from specified columns.

        Args:
            sheet_index (int): The index of the sheet to read (0-based).
            headings_to_search (list): A list of column headings to extract data from.

        Returns:
            list: A list containing the extracted values from specified columns.
        """
        combined_column_values = []

        with pyxlsb.open_workbook(self.xlsb_file_path) as wb:
            with wb.get_sheet(sheet_index) as sheet:
                column_indices = {heading.strip(): None for heading in headings_to_search}
                header_row = None

                for row in sheet.rows():
                    if header_row is None:
                        header_row = row
                        for heading in headings_to_search:
                            for idx, cell in enumerate(header_row):
                                if cell.v.strip() == heading.strip():
                                    column_indices[heading] = idx
                                    break
                    else:
                        for heading in headings_to_search:
                            column_index = column_indices[heading]
                            if column_index is not None and 0 <= column_index < len(row):
                                cell_value = row[column_index].v
                                if cell_value is not None:
                                    cell_value = str(cell_value).strip("'")
                                    combined_column_values.append(cell_value)

        return combined_column_values
