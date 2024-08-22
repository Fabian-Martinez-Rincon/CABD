import os
import utils.MRE as MRE
from utils.utils import process_folder

def map_function(k1, v1, context):
    context.write(1, v1)
 
def reduce_function(k2, v2, context):
    n = 0
    for _ in v2:
        n += 1
    context.write(k2, n)

def main():
    input_path, output, intermediate = process_folder("Inversionistas")
    
    job = MRE.Job(input_path, output, map_function, reduce_function)
    job.setIntermDir(intermediate)
    job.waitForCompletion()

    with open(os.path.join(output, "output.txt"), "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()
