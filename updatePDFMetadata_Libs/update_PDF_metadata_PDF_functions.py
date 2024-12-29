import sys
import time
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter



##############################################################
def exit_program(exit_message: str):
    """Exits the Python program."""
    print(exit_message)
    sys.exit()

##############################################################
def search_excel_record(excel_file_path: str, sheet_name: str, search_column: str, search_value: str) -> dict:

    try:
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    except ValueError as e:
        print(f"Error: {e}")
        return None

    result = df[df[search_column] == search_value]

    if not result.empty:
        return result.iloc[0].to_dict()
    else:
        print(f"No record found for {search_value} in column {search_column}.")
        return None

##############################################################
def get_cell_value(file_path: str, column_name: str, row_index):

    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')

        # Check if the column exists
        if column_name not in df.columns:
            return f"Column '{column_name}' does not exist in the file."

        # Check if the row index is valid
        if row_index < 0 or row_index >= len(df):
            return "Row index is out of range."

        # Get the cell value
        cell_value = df.at[row_index, column_name]

        # Return the string value of the selected cell
        return str(cell_value)

    except Exception as e:
        return f"An error occurred: {e}"

##############################################################
def get_column_values_from_excel(file_path: str, sheet_name: str, column_name: str) -> list:

    try:
        # Read the specified sheet from the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

        # Check if the column exists in the DataFrame
        if column_name not in df.columns:
            exit_program(f"Column '{column_name}' does not exist in the sheet '{sheet_name}'.")

        # Get all values from the specified column
        column_values = df[column_name].tolist()

        # Return the values as a list
        return column_values

    except Exception as e:
        exit_program(f"An error occurred: {e}")

##############################################################
def update_pdf_metadata(input_pdf_path: str, output_pdf_path: str, metadata: dict) -> None:
    ## Updates the PDF file metadata

    time.sleep(1)
    pdf_reader = PdfReader(input_pdf_path)

    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.add_metadata(metadata)

    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

##############################################################
def print_pdf_metadata(pdf_path: str) -> None:
    ## Reads out current metadata

    time.sleep(1)
    print("\n\n >> Reading PDF Metadata")
    pdf_reader = PdfReader(pdf_path)

    metadata = pdf_reader.metadata

    if metadata:
        print("\n\tMetadata:")
        for key, value in metadata.items():
            print(f"\t\t{key}: {value}")
    else:
        print("\nNo metadata found.")

##############################################################
def get_pdf_metadata(pdf_path: str) -> dict:

    pdf_reader = PdfReader(pdf_path)

    metadata = pdf_reader.metadata
    return metadata


