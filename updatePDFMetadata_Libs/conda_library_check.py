import re
import importlib
import time


#########################################################################
def extract_module_name(module_str):
    match = re.search(r"module '(.+?)'", module_str)
    if match:
        return match.group(1)
    return None


#########################################################################
def check_library(library_name: str) -> None:
    """Checks if a library is installed. If not, informs the user and exits."""
    try:
        module = importlib.import_module(library_name)
        module_name = extract_module_name(str(module))
        return module, module_name
    except ImportError:
        print(f"\n >> ERROR: The '{library_name}' library is not installed.")
        print(f"Please install it using 'pip install {library_name}' and try again.")
        print("Ending...\n\n")
        exit(1)


#########################################################################
def library_inspection(module_inspection: str) -> None:
    """ Runs both the check_library and extract_module_name Functions"""

    module_inspect, module_name = check_library(module_inspection)
    try:
        version = module_inspect.__version__
        print(f"Library: {module_name} Installed - Version:{str(version)}")
        time.sleep(0.5)
    except AttributeError:
        version = "Version Not Specified"
        print(f"Library: {module_name} Installed - {str(version)}")


