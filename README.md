# Update PDF Metadata from Table Record

This Python program allows you to update the metadata of a PDF file using information extracted from a record in a table. 

**Key Features:**

* **Dynamic Metadata Updates:** Easily modify various PDF metadata fields such as:
    * Title
    * Author
    * Subject
    * Keywords
    * Creation Date
    * Modification Date
    * Producer
    * Creator
    * Company
    * Department
    * Project
    * License
    * Copyright
    * Version


* **Table-Driven Updates:** Extract metadata values directly from a table record (e.g., in a database or spreadsheet).
* **Flexible Configuration:** Customize the mapping between table fields and PDF metadata fields to suit your specific needs.

**How it Works:**

1. **Read Table Record:** The program retrieves the necessary metadata values from the specified table record.
2. **Open PDF File:** The program opens the target PDF file using a suitable PDF library (e.g., PyPDF2, ReportLab).
3. **Select Record** A selection option will be listed to the console, using the filename as the option.
4. **Update Metadata:** The program modifies the PDF's metadata fields with the values extracted from the table record.
4. **Save Updated PDF:** The program saves the updated PDF file to a new or existing location.

**Usage:**

1. **Prepare Table Data:** Ensure your table contains the required metadata fields (e.g., "Title", "Author", "Subject").
2. **Configure Mapping:** Define the mapping between table fields and PDF metadata fields in the program's configuration.
3. **Run the Script:** Execute the Python script, providing the necessary input parameters (e.g., table record ID, PDF file path).

**Expandability**

The code can be upgrade in various ways to improve automation. Open for use, modifications, and suggestions.