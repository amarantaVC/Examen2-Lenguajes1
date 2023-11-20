"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 4
AMARANTA VILLEGAS 16-11247
Archivo misterioCreciente.py este archivo contiene el codigo de la pregunta 3 asociado al fragmento de codigo de la funcion misterio y que imprime el resultado de la funcion misterio.
"""

## def misterioCreciente(p):
def misterioCreciente(p):
    if p == []:
        yield []
    else:
        for x in misterioCreciente(p[1:]):
            yield x
            if x==[] or p[0]<= x[0]:
                yield [p[0], *x]

#salida
for x in misterioCreciente([1,4,3,2,5]):
    print(x)
    

