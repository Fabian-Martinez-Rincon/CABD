dataset = [
    {"key": 34, "value": 21},
    {"key": 21, "value": 34},
    {"key": 10, "value": 18},
    {"key": 32, "value": 45},
    {"key": 23, "value": 45},
    {"key": 12, "value": 12},
    {"key": 36, "value": 18},
    {"key": 4, "value": 97},
    {"key": 3, "value": 21},
    {"key": 15, "value": 10},
    {"key": 14, "value": 18},
    {"key": 3, "value": 15},
    {"key": 30, "value": 91},
    {"key": 31, "value": 32},
    {"key": 32, "value": 53},
    {"key": 19, "value": 35},
]

import csv

with open('dataset.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["key", "value"])
    writer.writeheader()
    for data in dataset:
        writer.writerow(data)

print("El dataset se ha guardado en 'dataset.csv'.")
