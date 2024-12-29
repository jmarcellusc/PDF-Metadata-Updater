import pandas as pd

##############################################################
def drop_first_item(mod_dict: dict) -> dict:
    # Drops the first entry in a dictionary

    if not mod_dict:
        return {}

    first_key = next(iter(mod_dict))
    new_dict = mod_dict.copy()
    new_dict.pop(first_key)
    return new_dict

##############################################################
def add_slash_to_keys(metadata_dict: dict) -> dict:
    # Adds a "/" character to each key in a dictionary

    new_dict = {}
    for key, value in metadata_dict.items():
        new_key = "/" + key
        new_dict[new_key] = value
    return new_dict

##############################################################
def merge_dicts(original_dict: dict, inserting_dict: dict) -> dict:

    merged_dict = original_dict.copy()
    merged_dict.update(inserting_dict)

    return merged_dict

##############################################################
def screen_diction_values(screen_dict: dict) -> dict:
    # Screens a Dictionary for certain values

    new_data = {}
    for key, value in screen_dict.items():
        if value in (None, '', ' ', 'nan') or isinstance(value, float):
            new_data[key] = f"No {key.replace("/", "")
  } Entry"
        else:
            new_data[key] = value
    return new_data

##############################################################
def convert_timestamps_to_dates(date_convert_dict: dict) -> dict:
    # Screens a dictionary for Pandas Timestamp, converts that to string YYYY-MM-DD
    # Original Return = %Y%m%d%H%M%S

    def _convert_if_timestamp(value):
        if isinstance(value, pd.Timestamp):
            value += pd.Timedelta(hours=6)  ## Adjustment to Time
            return value.strftime('%Y%m%d%H%M%S')
        elif isinstance(value, dict):
            return convert_timestamps_to_dates(value)
        elif isinstance(value, list):
            return [_convert_if_timestamp(item) for item in value]
        else:
            return value

    return {k: _convert_if_timestamp(v) for k, v in date_convert_dict.items()}

##############################################################
def replace_key_value(screen_diction: dict, old_key: str, new_key:str, new_value) -> dict:
  # Searches for a key in a dictionary. If found, replaces the key and its value.

  if old_key in screen_diction:
    del screen_diction[old_key]
    screen_diction[new_key] = new_value
  return screen_diction

##############################################################
def replace_key(screen_diction: dict, old_key: str, new_key: str) -> dict:
  # Searches for a key in a dictionary. If found, replaces the key only,

  if old_key in screen_diction:
    new_dict = screen_diction.copy()  # Create a copy to avoid modifying the original
    new_dict[new_key] = new_dict.pop(old_key)
    return new_dict
  else:
    return screen_diction  # Return the original dictionary if the key is not found

##############################################################
def replace_value_remove_quotes(screen_diction: dict, key: str) -> dict:
  # Searches for a key in a dictionary. If found, replaces the value with itself,
  # ...but removes all occurrences of single and double quotes from the value.

  if key in screen_diction:
    new_dict = screen_diction.copy()  # Create a copy to avoid modifying the original
    new_dict[key] = new_dict[key].replace("'", "").replace('"', '')
    return new_dict
  else:
    return screen_diction  # Return the original dictionary if the key is not found