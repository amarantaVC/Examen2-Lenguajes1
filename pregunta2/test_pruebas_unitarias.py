"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 2
AMARANTA VILLEGAS 16-11247
Archivo test_pruebas_unitarias.py, en este archivo se encuentran las pruebas unitarias para las funciones del archivo libreria.py 
"""

# Importamos la libreria unittest y las funciones que vamos a probar de libreria.py

from unittest import TestCase
from libreria import *

# Creamos la clase Pruebas_unitarias que hereda de TestCase y probamos las funciones evaluar_operacion, mostrar_expresion_infija, calcular_expresion_prefijo y calcular_expresion_postfijo con sus respectivos casos de prueba para ver si nos dan los resultados esperados
class Pruebas_Unitarias(TestCase):
    
    # test_evaluar_operacion es una funcion que prueba la funcion evaluar_operacion con los operadores +,-,*,/ y sus respectivos operandos
    def test_evaluar_operacion(self):
        casos_prueba = [
            ("+", "16", "11", 27),
            ("-", "69", "3", 66),
            ("*", "10", "10", 100),
            ("/", "6", "3", 2),
        ]

        # Recorremos los casos de prueba y comparamos el resultado de evaluar_operacion con el resultado esperado
        for operador, operadorIzq, operadorDer, resultado_esperado in casos_prueba:
            with self.subTest(operador=operador, operadorIzq=operadorIzq, operadorDer=operadorDer):
                self.assertEqual(evaluar_operacion(operador, operadorIzq, operadorDer), resultado_esperado)

    # test_mostrar_expresion_infija es una funcion que prueba la funcion mostrar_expresion_infija con los operadores +,-,*,/ y sus respectivos operandos
    def test_mostrar_expresion_infija(self):
        casos_prueba = [
            ("+", "25", "25", "25 + 25"),
            ("-", "10", "8", "10 - 8"),
            ("*", "7", "8", "7 * 8"),
            ("/", "5", "5", "5 / 5"),
        ]

        # Recorremos los casos de prueba y comparamos el resultado de mostrar_expresion_infija con el resultado esperado
        for operador, operadorIzq, operadorDer, resultado_esperado in casos_prueba:
            with self.subTest(operador=operador, operadorIzq=operadorIzq, operadorDer=operadorDer):
                self.assertEqual(mostrar_expresion_infija(operador, operadorIzq, operadorDer), resultado_esperado)

    # test_expresion_prefijo es una funcion que prueba la funcion calcular_expresion_prefijo con los operadores +,-,*,/ y sus respectivos operandos
    def test_expresion_prefijo(self):
        casos_prueba = [
            ("EVAL", ["+", "20", "25"], "45"),
            ("EVAL", ["-", "8", "5"], "3"),
            ("EVAL", ["*", "4", "5"], "20"),
            ("EVAL", ["/", "6", "2"], "3"),
            ("MOSTRAR", ["+", "24", "1"], "24 + 1"),
            ("MOSTRAR", ["-", "2", "0"], "2 - 0"),
            ("MOSTRAR", ["*", "4", "9"], "4 * 9"),
            ("MOSTRAR", ["/", "9", "3"], "9 / 3"),
        ]

        # Recorremos los casos de prueba y comparamos el resultado de calcular_expresion_prefijo con el resultado esperado
        for accion, expresion, resultado_esperado in casos_prueba:
            with self.subTest(accion=accion, expresion=expresion):
                self.assertEqual(calcular_expresion_prefijo(accion, expresion), resultado_esperado)

    #test_expresion_postfijo es una funcion que prueba la funcion calcular_expresion_postfijo con los operadores +,-,*,/ y sus respectivos operandos
    def test_expresion_postfijo(self):
        casos_prueba = [
            ("EVAL", ["0", "1", "+"], "1"),
            ("EVAL", ["10", "9", "-"], "1"),
            ("EVAL", ["8", "2", "*"], "16"),
            ("EVAL", ["36", "3", "/"], "12"),
            ("MOSTRAR", ["95", "5", "+"], "95 + 5"),
            ("MOSTRAR", ["6", "4", "-"], "6 - 4"),
            ("MOSTRAR", ["7", "1", "*"], "7 * 1"),
            ("MOSTRAR", ["9", "5", "/"], "9 / 5"),
        ]

        # Recorremos los casos de prueba y comparamos el resultado de calcular_expresion_postfijo con el resultado esperado
        for accion, expresion, resultado_esperado in casos_prueba:
            with self.subTest(accion=accion, expresion=expresion):
                self.assertEqual(calcular_expresion_postfijo(accion, expresion), resultado_esperado)
    
    #test_realizar_operacion_segun_entrada es una funcion que prueba la funcion realizar_operacion_segun_entrada con los operadores EVAL, MOSTRAR y SALIR y sus respectivos operandos
    def test_realizar_operacion_segun_entrada(self):
        casos_prueba = [
            # Ejemplos del parcial
            ("EVAL PRE + * + 3 4 5 7", "42"),
            ("MOSTRAR PRE + * + 3 4 5 7", "(3 + 4) * 5 + 7"),
            ("EVAL POST 8 3 - 8 4 4 + * +", "69"),
            ("MOSTRAR POST 8 3 - 8 4 4 + * +", "8 - 3 + 8 * (4 + 4)"),
            # Ejemplos adicionales usando PRE
            ("EVAL PRE * * + - 1 2 3 4 5", "40"),
            ("MOSTRAR PRE * * + - 1 2 3 4 5", "((1 - 2 + 3) * 4) * 5"),
            # Ejemplos adicionales usando POST
            ("EVAL POST 2 6 * 4 6 / 6 + 2", "12"),
            ("MOSTRAR POST 2 6 * 4 6 / 6 + 2", "2 * 6"),
            # Casos de error
            ("EVAL", "Error. Ingrese parametro <orden>"),
            ("EVAL PRE", "Error. Ingrese parametro <expr>"),
            ("EVAL POST", "Error. Ingrese parametro <expr>"),
            ("EVAL INF", "Error. Orden no valido, indique PRE o POST"),
            ("EVAL * * + - 1 2 -3 4 + * +", "Error. Orden no valido, indique PRE o POST"),
            ("MOSTRAR", "Error. Ingrese parametro <orden>"),
            ("MOSTRAR PRE", "Error. Ingrese parametro <expr>"),
            ("MOSTRAR POST", "Error. Ingrese parametro <expr>"),
            ("MOSTRAR INF", "Error. Orden no valido, indique PRE o POST"),
            ("MOSTRAR * * + - 1 2 -3 4 + * +", "Error. Orden no valido, indique PRE o POST"),
            ("EJECUTAR", "Error. Accion no es valida, indique si es EVAL, MOSTRAR o SALIR"),
            ("SALIR", None),
        ]

        # Recorremos los casos de prueba y comparamos el resultado de realizar_operacion_segun_entrada con el resultado esperado
        for entrada, resultado_esperado in casos_prueba:
            # Si el resultado esperado es None, entonces esperamos que se lance una excepcion
            if resultado_esperado is None:
                with self.assertRaises(SystemExit):
                    realizar_operacion_segun_entrada(entrada)
            # Si el resultado esperado no es None, entonces comparamos el resultado de realizar_operacion_segun_entrada con el resultado esperado
            else:
                self.assertEqual(realizar_operacion_segun_entrada(entrada), resultado_esperado)

