import os
import utils.MRE as MRE  # Asegúrate de que el módulo MRE esté disponible.
from utils.utils import create_directories

def map_function(k1, v1, context):
    context.write(1, v1)

def reduce_function(k2, v2, context):
    n = 0
    for _ in v2:
        n += 1
    context.write(k2, n)

PATH_BASE = os.path.dirname(os.path.abspath(__file__))
PATH_DATA = os.path.join(PATH_BASE, "datasets")

print(PATH_BASE)

def main():
    input_path = os.path.join(PATH_DATA, "Inversionistas")
    output = os.path.join(PATH_DATA, "Inversionistas_output")
    intermediate = os.path.join(PATH_DATA, "Inversionistas_intermediate_dir")

    create_directories(output, intermediate)

    job = MRE.Job(input_path, output, map_function, reduce_function)
    job.setIntermDir(intermediate)

    job.waitForCompletion()

    with open(os.path.join(output, "output.txt"), "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()
