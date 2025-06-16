import json

def extract_nested_keys(data, parent_key=""):
    keys = []
    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            keys.extend(extract_nested_keys(value, full_key))
        else:
            keys.append(full_key)
    return keys

def get_nested_keys_from_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        nested_keys = extract_nested_keys(data)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        nested_keys = []
    return nested_keys

filepath = "happy.json"
print(get_nested_keys_from_json_file(filepath))