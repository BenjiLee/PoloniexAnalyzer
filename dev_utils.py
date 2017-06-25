"""
Utility methods for development
"""
import json


def dict_to_file(dict_input, filename):
    with open(filename, 'w') as f:
        json.dump(dict_input, f, indent=4, sort_keys=True)


def file_to_dict(filename):
    with open(filename, 'r') as f:
        return json.load(f)
