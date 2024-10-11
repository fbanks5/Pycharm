import openpyxl

def modify_excel_spreadsheet(filename):
    """
    Modifies an Excel spreadsheet and allows changes within the script.

    Args:
        filename (str): The name of the Excel file.
    """

    # Load the workbook
    workbook = openpyxl.load_workbook(filename)

    # Get the active sheet (you can specify a sheet name if needed)
    sheet = workbook.active

    # Make your changes here
    # Example: Modify cell A1
    sheet['A1'] = 'New value'

    # Add more modification logic as needed

    # Save the modified workbook
    workbook.save(filename)

if __name__ == '__main__':
    filename = 'your_spreadsheet.xlsx'
    modify_excel_spreadsheet(filename)