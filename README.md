# CABD

Conceptos y Aplicaciones de Big Data

- [Practica 1 Paradigma MapReduce](#practica-1-paradigma-mapreduce)
- [Practica 2 Hadoop MapReduce](#practica-2-hadoop-mapreduce)
- [Practica 3](#practica-3)
- [Practica 4](#practica-4)
- [Practica 5](#practica-5)
- [Practica 6](#practica-6)
- [Practica 7](#practica-7)

---

## Practica 1 Paradigma MapReduce

#### Ejercicio 1

Dado el siguiente dataset:

![image](https://github.com/user-attachments/assets/6109904a-7c94-423f-aeed-f72853224529)

Responda para cada job: 

`¿Cuántas veces (invocaciones) se ejecuta la función map?`

`¿Cuántas veces (invocaciones) se ejecuta la función reduce?`

`¿Cuántos mappers se ejecutan?`

`¿Cuántos reducers se ejecutan?`

`¿Qué datos recibe cada función reduce?`

`¿Cuál es la salida de cada job?`

**a) Job A**

```python
def map(k1, v1, context):
    context.write(1, v1)
def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(k2, n)
```

**b) Job B**

```python
def map(k1, v1, context):
    context.write(1, v1)
def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + v
    context.write(k2, n)
```

**c) Job C**

```python
def map(k1, v1, context):
    if (v1 < 30):
        context.write(1, k1)
    else:
        context.write(2, k1)
    def reduce(k2, v2, context):
        max = -1
        for v in v2:
            if(v > max):
                max = v
        context.write(k2, max)
```

**d) Job D**

```python
def map(k1, v1, context):
    for v in range(v1):
        context.write(k1, v1)
def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(k2, n)
```

**e) Job E**

```python
def map(k1, v1, context):
    context.write(v1, k1)
def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(v, n)
```

#### Ejercicio 2

El dataset Libros provisto por la cátedra almacena libros cada uno en un archivo separado. Dentro de cada archivo, la primera línea tiene el título del libro y luego en las líneas siguientes un párrafo por línea. Ejecute el proyecto WordCount dado por la cátedra para saber cuántas veces es utilizada cada palabra

#### Ejercicio 3

En el ejercicio anterior ¿Cómo haría para obtener el top 20 de las palabras más usadas?

#### Ejercicio 4

Modifique el proyecto WordCount para contar cuántas vocales, consonantes, dígitos, espacios y otros caracteres posee el data set Libros.

#### Ejercicio 5

Indique si utilizando el dataset Libros es posible resolver los siguientes problemas:
- `a)` Obtener los títulos de todos los libros
- `b)` Obtener la cantidad de palabras promedio por párrafo
- `c)` Obtener la cantidad de párrafos promedio por libro
- `d)` Obtener la cantidad de caracteres del párrafo más extenso
- `e)` Cantidad total de párrafos con diálogos (se entiende por párrafo con diálogo aquel que empieza con un guión)
- `f)` El diálogo más largo (se entiende por diálogo a una secuencia de párrafos con diálogo que aparecen de manera consecutiva)
- `g)` El top 20 de las palabras más usadas por cada libro


#### Ejercicio 6

Una empresa proveedora de internet realizó una encuesta para conocer el grado de satisfacción de sus clientes, en un formulario web los clientes debían completar un campo con los textos "Muy satisfecho", "Algo satisfecho", "Poco satisfecho", “Disconforme” o "Muy disconforme". Utilice el dataset Encuesta para saber cuántos clientes están en cada una de las cinco categorías.

#### Ejercicio 7

El dataset Inversionistas posee los nombres, dni, fecha de nacimiento (día, mes y año como campos separados) e importe invertido por diferentes personas en la apertura de un nuevo negocio en la ciudad. Se desea saber:
- `a)` El nombre del inversionista más joven
- `b)` El total del importe invertido por todos los inversionistas
- `c)` El promedio de edad

Implemente una solución en MapReduce. ¿Se puede resolver los tres problemas en un único job?

#### Ejercicio 8

Si contáramos con un cluster donde podemos configurar 100 nodos para la tarea de reduce ¿De qué manera se podrían usar esos 100 nodos en el ejemplo de los eventos POSITIVO, NEGATIVO y NEUTRO visto en la teoría?


---

## Practica 2 Hadoop MapReduce

#### Ejercicio 1

¿En el dataset del ejercicio 1 de la práctica 1 indique para cada Job, si se vería beneficiado por una función combiner? En caso afirmativo, ¿cuál es la implementación de dicha función? ¿Qué datos recibe cada reduce, al utilizar la función combiner?

#### Ejercicio 2

Implemente una función combiner para el problema del WordCount.

#### Ejercicio 3

Implemente un job MapReduce para calcular el máximo, mínimo, promedio y desvío stándard de las ocurrencias de todas las palabras del dataset Libros.


#### Ejercicio 4

Utilice el dataset Libros para implementar una aplicación MapReduce que devuelva como salida todos los párrafos que tienen una longitud mayor al promedio.


#### Ejercicio 5

El dataset website tiene información sobre el tiempo de permanencia de sus usuarios en cada una de las páginas del sitio. El formato de los datos del dataset es:

```html
<id_user, id_page, time>
```

Implemente una aplicación MapReduce, utilizando combiners en los casos que
considere necesario, que calcule

- `a)` La página más visitada (la página en la que más tiempo permaneció) para cada usuario
- `b)` El usuario que más páginas distintas visitó
- `c)`. La página más visitada (en cuanto a cantidad de visitas, sin importar el tiempo de permanencia) por todos los usuarios.

Indique como queda el DAG del proceso completo (las tres consultas)


#### Ejercicio 6


#### Ejercicio 7


#### Ejercicio 8



---

## Practica 3

---

## Practica 4

---

## Practica 5

---

## Practica 6

---

## Practica 7
