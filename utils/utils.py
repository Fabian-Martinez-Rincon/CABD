import os
from os import mkdir
from os.path import isdir
from pathlib import Path

def process_folder(name):
    PATH_BASE = Path(__file__).resolve().parent.parent
    PATH_DATA = os.path.join(PATH_BASE, "datasets")
    
    def load_dataset(subname):
        return os.path.join(PATH_DATA, subname)
    
    def create_directories(*directories):
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    input_path = load_dataset(name)
    output_path = load_dataset(f"{name}_output")
    intermediate_path = load_dataset(f"{name}_intermediate")
    
    create_directories(output_path, intermediate_path)
    return input_path, output_path, intermediate_path