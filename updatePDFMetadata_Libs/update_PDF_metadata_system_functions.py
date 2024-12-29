import os, sys
import time
import tkinter as tk
from tkinter import filedialog




##############################################################
def select_pdf_file():
    time.sleep(1)
    print(" >> Initializing PDF File Selector (Please Minimize All Windows)")
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])

##############################################################
def print_list(list_items: list, title_matter: str) -> None:

    if not isinstance(list_items, list) or not all(isinstance(item, str) for item in list_items):
        exit_program(f"Error in Reading List For: {title_matter}")

    print(f"\n{title_matter}")
    for idx, item in enumerate(list_items, start=1):
        print(f"\t{idx}. {item}")
        time.sleep(0.4)

##############################################################
def get_root_dir_and_name(pdf_filepath: str) -> tuple[str, str]:

  root_dir = os.path.dirname(pdf_filepath)
  filename = os.path.basename(pdf_filepath)
  return root_dir, filename

##############################################################
def check_file_exists(check_file_path: str):
    return os.path.isfile(check_file_path)

##############################################################
def create_export_pdf_name(root_dir: str, screen_diction: dict, filename_key: str) -> str:
    # Creates a PDF filename to a targeted directory with a new filename from a dictionary

    new_pdf_filename: str = screen_diction[filename_key]
    return os.path.join(root_dir, new_pdf_filename + ".pdf")

##############################################################
def print_dictionary(diction_data: dict, title_matter: str) -> None:
    # Prints Friendly Dictionary to Console

    if not isinstance(diction_data, dict):
        exit_program(f"Error in Reading Dictionary For: {title_matter}")

    print(f"\n{title_matter}")
    print("_______________________________")
    for key, value in diction_data.items():
        print(f"\t{key}: {value}")
        time.sleep(0.4)

##############################################################
def select_item_from_list(items: list) -> str:

    if not items:
        print("The list is empty. Please provide a valid list.")
        exit_program(f"Excel File Found No Listings")

    print("\n\n   --- DATABASE QUERY EXTRACTION --- ")
    print(" >> Please select an item from the list below:")
    for idx, item in enumerate(items, start=1):
        print(f"\t{idx}. {item}")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print("\nInvalid choice. Please enter a number between 1 and", len(items))
        except ValueError:
            print("\nInvalid input. Please enter a number.")

##############################################################
def exit_program(exit_message: str):
    """Exits the Python program."""
    print(exit_message)
    sys.exit()





