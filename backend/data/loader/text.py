import yaml
import os

callouts_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'example_callouts.yml')

def get_callouts_data():
    with open(callouts_file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
