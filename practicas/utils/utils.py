import os
from pathlib import Path
import chardet

def process_folder(name):
    PATH_BASE = Path(__file__).resolve().parent.parent.parent
    print(PATH_BASE)
    PATH_DATA = os.path.join(PATH_BASE, "datasets")
    
    def load_dataset(subname):
        return os.path.join(PATH_DATA, subname)
    
    def create_directories(*directories):
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    input_path = load_dataset(name)
    output_path = os.path.join(input_path, f"{name}_output")
    intermediate_path = os.path.join(input_path, f"{name}_intermediate")
    
    create_directories(output_path, intermediate_path)
    return input_path, output_path, intermediate_path

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def display_final_output(output_directory):
    output_file_path = os.path.join(output_directory, "output.txt")
    try:
        encoding = detect_encoding(output_file_path)
        print(f"Codificación detectada: {encoding}")

        try:
            with open(output_file_path, "r", encoding=encoding) as file:
                print("Final output:")
                print(file.read())
        except UnicodeDecodeError:
            print(f"Error con la codificación {encoding}. Reintentando con 'ISO-8859-1'.")
            with open(output_file_path, "r", encoding="ISO-8859-1") as file:
                print("Final output:")
                print(file.read())

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en {output_file_path}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
