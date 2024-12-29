"""
Tool:               PDF Metadata Updater
Source Name:        PDF-Metadata-Updater
Version:            1.1
Author:             Juan-Marcel Campos
Usage:              Updates the PDF metadata
Required Arguments: PDF file and metadata information
Description:        Will update the PDF metadata from a table of updating values
"""


# ! Front Matter
#########################################################################
#########################################################################
VERSION_PDF_METADATA = 1.1

# * Starting Project:
#  GitHub Repo: Reverse Geocode
# Please install: ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.

# v1.0 -  Initial Creation of Script (Not yet commited)
# v1.1 -  Fixes Date Issue with Modification Date and Timezone creation offset. (NOTE: ModDate issue originates with ArcGIS Pro Software)

#########################################################################
#########################################################################
from updatePDFMetadata_Libs import conda_library_check as CLC

print("\n >> CHECKING CONDA LIBRARY REQUIREMENTS...")
CLC.library_inspection("pandas")
CLC.library_inspection("PyPDF2")
CLC.library_inspection("tkinter")
print(" >> CHECK PASS...\n\n\n")

#########################################################################
#########################################################################
print("\n")
import time
from updatePDFMetadata_Libs import update_PDF_metadata_Globals as UPM_GLOBALS ## Globals
from updatePDFMetadata_Libs import update_PDF_metadata_system_functions as UPMSF
from updatePDFMetadata_Libs import update_PDF_metadata_dict_functions as UPMDF
from updatePDFMetadata_Libs import update_PDF_metadata_PDF_functions as UPMPF





##=================================================
## >>>          _Main Script Process_           <<<
##=================================================
# ! Pandas Format
if __name__ == "__main__":
    ## Indent
    #
    #####################################################################################
    # ! Introduction
    time.sleep(5)
    print("########################################################")
    print("   | ---        PDF Metadata Toolkit           --- |   ")
    print("   | ---        \"Attribution Series\"           --- | ")
    print("########################################################")
    time.sleep(1)
    print(f"__Version: {VERSION_PDF_METADATA}\n\n")

    ## Import Globals (Please Update the Excel Metadata Database)
    EXCEL_METADATA_DB: str = UPM_GLOBALS.EXCEL_METADATA_DB
    EXCEL_SHEET: str = UPM_GLOBALS.EXCEL_SHEET
    FILE_NAME: str = UPM_GLOBALS.FILE_NAME
    FILENAME_KEY: str = UPM_GLOBALS.FILENAME_KEY

    ## Selects PDF
    pdf_file_path: str = UPMSF.select_pdf_file()
    print(f" ____ PDF File:  {pdf_file_path}\n")
    root_directory, pdf_name = UPMSF.get_root_dir_and_name(pdf_file_path) ## Gets file root directory and name


    ## Gets and Selects File from Excel Database
    time.sleep(1)
    files_list: list = UPMPF.get_column_values_from_excel(EXCEL_METADATA_DB, EXCEL_SHEET, FILE_NAME)
    selected_file: str = UPMSF.select_item_from_list(files_list)
    print(f" ___ SELECTED ATTRIBUTES FILE_NAME: \"{selected_file}\"\n\n")

    ## Returns Database Items for the Selected Record
    time.sleep(1)
    pdf_metadata_update: dict = UPMDF.add_slash_to_keys(UPMDF.drop_first_item(UPMPF.search_excel_record(EXCEL_METADATA_DB, EXCEL_SHEET, FILE_NAME, selected_file)))

    ## Process Conversions and screens
    time.sleep(1)
    merged_pdf_metadata = UPMDF.screen_diction_values(pdf_metadata_update)
    UPMSF.print_dictionary(merged_pdf_metadata, "Database Read PDF Metadata")
    merged_pdf_metadata = UPMDF.convert_timestamps_to_dates(merged_pdf_metadata)

    # Version 1.1
    merged_pdf_metadata = UPMDF.replace_key(merged_pdf_metadata, "/ModificationDate", "/ModDate") # Fixes Date Issue
    merged_pdf_metadata = UPMDF.replace_value_remove_quotes(merged_pdf_metadata, "/Keywords")  # Fixes Quotes Issue (Maybe not needed)

    ## Create Export File Name and Check if File Exist
    time.sleep(1)
    export_pdf_filepath = UPMSF.create_export_pdf_name(root_directory, merged_pdf_metadata, FILENAME_KEY)
    if UPMSF.check_file_exists(export_pdf_filepath):
        UPMSF.exit_program("ERROR: File Already Exist, Please Correct.")

    # Update PDF Metadata
    time.sleep(1)
    print("\n\n\n\n >> Running PDF Metadata Updater...")
    UPMPF.update_pdf_metadata(pdf_file_path, export_pdf_filepath, merged_pdf_metadata)

    ## Check Metadata Listing
    time.sleep(2)
    print("\n    ___ Checking NEW PDF Metadata...")
    pdf_metadata = UPMPF.get_pdf_metadata(export_pdf_filepath)
    UPMSF.print_dictionary(pdf_metadata, "UPDATED PDF Metadata Listing")
    print("\n >> Process Complete.\nEnding....\n")
