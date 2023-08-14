import json, os

def append_to_file(file_name, key_string, value_list):
    # remove value if it is the same as key (helps prevent accidental deadlock)
    for value in value_list:
        if value == key_string: value_list.remove(value)
    
    if os.path.exists(file_name): 
        try:
            with open(file_name, 'r') as file: data = json.load(file)
        except: data = {}
    else: data = {}

    data[key_string] = value_list

    with open(file_name, 'w') as file: json.dump(data, file, indent=4)

def read_from_file(file_name):
    if os.path.exists(file_name): 
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                file.close()
                return data
        except: 
            Exception(f"No data in file \"{file_name}\"...")