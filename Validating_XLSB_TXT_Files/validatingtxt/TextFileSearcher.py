from Validating_XLSB_TXT_Files.lib.constant import XLSB_FILE_PATH, TEXT_FILE_PATH, COLUMN_NAMES
from Validating_XLSB_TXT_Files.validatingtxt.XLSBReader import XLSBReader


class DataValidator:
    def __init__(self, xlsb_file_path, text_file_path, sheet_index):
        """
        Initialize the DataValidator with XLSB and text file paths.

        Args:
            xlsb_file_path (str): The path to the XLSB file.
            text_file_path (str): The path to the text file.
            sheet_index (int): The index of the sheet to read (0-based).
        """
        self.xlsb_file_path = xlsb_file_path
        self.text_file_path = text_file_path
        self.sheet_index = sheet_index

    def validate_data(self):
        xlsb_reader = XLSBReader(self.xlsb_file_path)
        headings_to_search = COLUMN_NAMES
        values_to_search = xlsb_reader.read_xlsb(self.sheet_index, headings_to_search)

        matches = []
        mismatches = []

        with open(self.text_file_path, 'r') as file:
            file_content = file.read()
            for value in values_to_search:
                search_value = str(value)
                if search_value in file_content:
                    matches.append(search_value)
                else:
                    mismatches.append(search_value)

        if matches:
            print("Matches found in the text file:")
            for match in matches:
                print(match)
            # Add your custom actions here for each match
        else:
            print("No matches found in the text file.")

        if mismatches:
            print("Mismatched values not found in the text file:")
            for mismatch in mismatches:
                print(mismatch)
