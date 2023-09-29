from Validating_XLSB_TXT_Files.lib.constant import XLSB_FILE_PATH, TEXT_FILE_PATH
from Validating_XLSB_TXT_Files.validatingtxt.TextFileSearcher import DataValidator


class DataValidation:
    def __init__(self, xlsb_file_path, text_file_path, sheet_index):
        """
        Initialize the DataValidationApplication.

        Args:
            xlsb_file_path (str): The path to the XLSB file.
            text_file_path (str): The path to the text file.
            sheet_index (int): The index of the sheet to read (0-based).
        """
        self.xlsb_file_path = xlsb_file_path
        self.text_file_path = text_file_path
        self.sheet_index = sheet_index

    def run(self):
        validator = DataValidator(self.xlsb_file_path, self.text_file_path, self.sheet_index)
        validator.validate_data()


if __name__ == "__main__":
    xlsb_file_path = XLSB_FILE_PATH
    text_file_path = TEXT_FILE_PATH
    sheet_index = 1

    app = DataValidation(xlsb_file_path, text_file_path, sheet_index)
    app.run()
