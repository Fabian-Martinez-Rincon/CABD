import practicas.utils.MRE as MRE
from practicas.utils.utils import process_folder, display_final_output

"""
El dataset Libros provisto por la cátedra almacena libros cada uno en un archivo
separado. Dentro de cada archivo, la primera línea tiene el título del libro y luego en
las líneas siguientes un párrafo por línea. Ejecute el proyecto WordCount dado por la
cátedra para saber cuántas veces es utilizada cada palabra.
"""

word_count = {}

def fmap(key, value, context):
    words = value.split()
    for w in words:
        context.write(w, 1)
        
def fred(key, values, context):
    c=0
    for v in values:
        c=c+1
    context.write(key, c)

def ejercicio2_run():
    input_path, output, intermediate = process_folder("libros")
    
    job = MRE.Job(input_path, output, fmap, fred)
    job.setIntermDir(intermediate)
    job.waitForCompletion()
    
    display_final_output(output)
    
if __name__ == "__main__":
    ejercicio2_run()
