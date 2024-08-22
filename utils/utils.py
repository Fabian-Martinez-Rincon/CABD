import os
from os import mkdir
from os.path import isdir

def create_directories(*dirs):
    """Crea los directorios si no existen."""
    for directory in dirs:
        if not isdir(directory):
            mkdir(directory)
