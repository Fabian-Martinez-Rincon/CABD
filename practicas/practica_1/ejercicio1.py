import practicas.utils.MRE as MRE
from practicas.utils.utils import process_folder, display_final_output

"""
Responda para cada job: 
- ¿Cuántas veces (invocaciones) se ejecuta la función map?
- ¿Cuántas veces (invocaciones) se ejecuta la función reduce?
- ¿Cuántos mappers se ejecutan?
- ¿Cuántos reducers se ejecutan?
- ¿Qué datos recibe cada función reduce?
- ¿Cuál es la salida de cada job?
"""

##################################################

def mapA(k1, v1, context):
    context.write(1, v1)
 
def reduceA(k2, v2, context):
    n = 0
    for _ in v2:
        n += 1
    context.write(k2, n)

##################################################    
    
def mapB(k1, v1, context):
    context.write(1, v1)

def reduceB(k2, v2, context):
    n = 0
    for v in v2:
        n = n + int(v)
    context.write(k2, n)
    
##################################################

def mapC(k1, v1, context):
    if (int(v1) < 30):
        context.write(1, k1)
    else:
        context.write(2, k1)

def reduceC(k2, v2, context):
    max = -1
    for v in v2:
        if(int(v) > int(max)):
            max = v
    context.write(k2, max)

##################################################

def mapD(k1, v1, context):
    for v in range(int(v1)):
        context.write(k1, v1)
        
def reduceD(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(k2, n)

##################################################

def mapE(k1, v1, context):
    context.write(v1, k1)
    
def reduceE(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
        context.write(v, n)

##################################################

def ejercicio1_run():
    input_path, output, intermediate = process_folder("ejercicio1A")
    
    job = MRE.Job(input_path, output, mapE, reduceE)
    job.setIntermDir(intermediate)
    job.waitForCompletion()
    
    display_final_output(output)   
    
if __name__ == "__main__":
    ejercicio1_run()
