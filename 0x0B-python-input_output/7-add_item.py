#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the add_item.json file exists, if not, create it with an empty list.
filename = 'add_item.json'
if not os.path.exists(filename):
    save_to_json_file([], filename)

# Load the list from the JSON file
my_list = load_from_json_file(filename)

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
