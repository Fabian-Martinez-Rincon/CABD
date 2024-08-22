from os import mkdir
from os.path import isdir
import os
import MRE

def map(k1, v1, context):
    context.write(1, v1)

def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n += 1
    context.write(k2, n)

#base_directory = 'datasets'

input_dir = os.path.join('datasets', "Inversionistas")

#input_dir = "/datasets/Inversionistas"
output_dir = "output_dir"
intermediate_dir = "intermediate_dir"

if not isdir(input_dir):
    mkdir(input_dir)
if not isdir(output_dir):
    mkdir(output_dir)
if not isdir(intermediate_dir):
    mkdir(intermediate_dir)

job = MRE.Job(input_dir, output_dir, map, reduce)
job.setIntermDir(intermediate_dir)

job.waitForCompletion()

with open(f"{output_dir}/output.txt", "r") as f:
    print(f.read())
