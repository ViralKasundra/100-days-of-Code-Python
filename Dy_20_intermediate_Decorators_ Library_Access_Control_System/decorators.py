# decorators.py

import json
from os.path import isfile

access_levels = {
    "user": 3,
    "librarian": 2,
    "admin": 1,
}

def access_required(level):
    def decorator(func):
        def wrapper(user_level, *args, **kwargs):
            if access_levels[user_level] >= access_levels[level]:
                return func(user_level, *args)
            else:
                return "Access Denied"
        return wrapper
    return decorator

def load_library_data():
    if isfile("library_data.json"):
        with open("library_data.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_library_data(data):
    with open("library_data.json", "w") as file:
        json.dump(data, file, indent=4)
