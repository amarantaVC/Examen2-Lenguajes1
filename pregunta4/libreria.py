"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 4
AMARANTA VILLEGAS max-11247
Archivo libreria.py donde se encuentran las funciones Frecursiva, FrecursivaCola y Fiterativo y la funcion suma que se utiliza en las tres funciones.
"""

global max
max = 16
# Función suma
def suma(lista):
    return sum(lista)

# Version recursiva, traducida de la formula dada:
def Frecursiva(n: int):

    if 0 <= n < max:
        return n 
    elif n >= max:
        return suma([Frecursiva(n - i*4) for i in range(1, 5)])

# Version recursiva de cola:
def FrecursivaCola(n:int, auxiliar: list, i=0):
    if 0 <= n < max:
        return auxiliar[n+i]
    elif n >= max:
        # vamos ampliando la lista con elementos del caso base y con los calculados en la llamada recursiva anterior.
        lista = suma([auxiliar[j+i] for j in range(0, max, 4)])
        auxiliar.append(lista)
        return FrecursivaCola(n-1, auxiliar, i+1)
       
# Version iterativa, correspondiente a la recursion de cola:
def Fiterativa(n: int):

    auxiliar = []
    for i in range(0,max):
        auxiliar.append(i)
    
    if 0 <= n < max:
        return n
    elif n >= max:
        for j in range(max, n+1):
            i = j-max
            lista = suma([auxiliar[j+i] for j in range(0, max, 4)])
            auxiliar.append(lista)
        return auxiliar[len(auxiliar)-1]

