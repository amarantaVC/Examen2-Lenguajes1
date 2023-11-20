"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 4
AMARANTA VILLEGAS 16-11247
Archivo misterio.py este archivo contiene el codigo de la pregunta 3 asociado al fragmento de codigo de la funcion misterio y que imprime el resultado de la funcion misterio.
"""

##variables globales necesarias para la ejecucion del programa
X,Y,Z = 2,4,7
a = 2 * X + 3 * Y + 2
b = 4 * Y + 5 * Z + 1
c = 5 * X + 2 * Z + 3
d = (a + b + c) % 7

##definicion de la funcion misterio
def misterio(a, b, c, d):
    if c == 0:
        yield a
        for x in misterio(b, a, b, d - 1):
            yield x
    elif d > 0:
        for x in misterio(a, b + 1, c - 1, d):
            yield x
##salida
for x in misterio(0, 1, 0, d + 1):
    print(x)

