"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 2
AMARANTA VILLEGAS 16-11247
cliente.py , este archivo permite al usuario ingresar una accion y una expresion para que se realice la accion correspondiente a la expresion ingresada
"""
#importamos la libreria libreria.py para poder usar sus funciones en este archivo
from libreria import *

#utilizamos un while True para que el usuario pueda ingresar una accion y una expresion las veces que quiera sin que el programa termine
while True:
    accion = input("Por favor ingrese una accion para proceder:"
                    "\nEVAL <orden> <expr>"
                    "\nMOSTRAR <orden> <expr>\n"
                    "SALIR\n\n")
    resultado = realizar_operacion_segun_entrada(accion)

    print("\n RESULTADO:", resultado, "\n")