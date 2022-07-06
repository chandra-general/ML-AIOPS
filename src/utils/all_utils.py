import yaml
import os

def read_yaml(path_to_yaml:str) -> dict:
    """
    Reads a yaml file and returns a dictionary
    """
    with open(path_to_yaml, 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except yaml.YAMLError as exc:
            print(exc)

def create_directory(dirs: list):
    """
    Creates a directory if it doesn't exist
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory is created at {dir_path}")