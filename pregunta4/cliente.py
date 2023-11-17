"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 4
AMARANTA VILLEGAS 16-11247
Archivo cliente.py para mostrar los resultados de las funciones de libreria.py y compararlas
"""
from libreria import *

import time
#entrada 
n = int(input("Indique el valor de n: "))

# Lista de funciones
funciones = [Frecursiva, FrecursivaCola, Fiterativa]
nombres_funciones = ["F recursiva", "F recursiva de cola", "F iterativa"]

for funcion, nombre in zip(funciones, nombres_funciones):
    print("-------------------------------\n")
    
    #tiempo de inicio de ejecucion
    inicio = time.time()
    if nombre == "F recursiva de cola":
        resultado = funcion(n, [i for i in range(0, 16)])
    else:
        resultado = funcion(n)
    #tiempo final de ejecucion
    fin = time.time()
    #calculo tiempo total 
    tiempo = round(fin-inicio, 4)
    #salida
    print(f"{nombre} de {n}: {resultado}")
    print(f"Con tiempo de ejecucion: {tiempo}")

