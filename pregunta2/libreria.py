"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 2
AMARANTA VILLEGAS 16-11247 
libreria.py, en este archivo se encuentran las funciones que se usan en el archivo main.py y pruebas_unitarias.py correspondientes a la pregunta 2 del examen II
"""

#calcular_expresion_prefijo, es una funcion que tiene como parametros una accion y una expresion en notacion prefija. Retorna la evaluacion de la expresion.
def calcular_expresion_prefijo(accion: str,expresion: list) -> str:
    pila = []

    # Recorremos la expresion en orden inverso, es decir de derecha a izquierda
    for i in range(len(expresion) - 1, -1, -1):
        if expresion[i] in "+-*/":
            operadorIzq = pila.pop()
            operadorDer = pila.pop()
            operador = expresion[i]
            resultado = evaluar_operacion(operador, operadorIzq, operadorDer) if accion == "EVAL" else mostrar_expresion_infija(operador, operadorIzq, operadorDer)
            pila.append(f"{resultado}")
        else:
            pila.append(expresion[i])

    return pila[0]



# calcular_expresion_postfijo, es una funcion que tiene como parametros una accion y una expresion en notacion postfija. Retorna la evaluacion de la expresion.
def calcular_expresion_postfijo(accion: str,expresion: list) -> str:

    pila = []

    for i in range(0, len(expresion)):

        if expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "*" or expresion[i] == "/":
            operadorDer = pila.pop()
            operadorIzq = pila.pop()
            operador = expresion[i]

            if accion == "EVAL":
                resultado = evaluar_operacion(operador, operadorIzq, operadorDer)
            elif accion == "MOSTRAR":
                resultado = mostrar_expresion_infija(operador, operadorIzq, operadorDer)
            pila.append(f"{resultado}")

        else:

            pila.append(expresion[i])
    return pila[0]

#evaluar_operacion es una funcion que tiene como parametros un operador y los operadores izquierdo y derecho y nos retorna la evaluacion de la operacion para saber si es +,-,*,/
def evaluar_operacion(operador: str, operadorIzq: str, operadorDer: str) -> int:
    operaciones = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }
    return operaciones[operador](int(operadorIzq), int(operadorDer))

# mostrar_expresion_infija es una funcion que tiene como parametros un operador y los operadores izquierdo y derecho y nos retorna la expresion en notacion infija
def mostrar_expresion_infija(operador: str,operadorIzq: str,operadorDer: str) -> str:
    if operador in "+-":
        operadorDer = f"({operadorDer})" if len(operadorDer) == 2 and int(operadorDer) < 0 else operadorDer
        return f"{operadorIzq} {operador} {operadorDer}"
    elif operador in "*/":
        operadorIzq = f"({operadorIzq})" if len(operadorIzq) > 1 else operadorIzq
        operadorDer = f"({operadorDer})" if len(operadorDer) > 1 else operadorDer
        return f"{operadorIzq} {operador} {operadorDer}"

#realizar_operacion_segun_entrada es una funcion que tiene como parametro una accion y nos retorna el resultado de la accion correspondiente a la expresion ingresada
def realizar_operacion_segun_entrada(accion: str) -> str:
    
    # Separamos la accion en una lista donde cada elemento es una palabra
    accion = accion.strip().split()

    if accion[0] == "EVAL":
        try:
            orden = accion[1]
        except:
            return "Error. Ingrese parametro <orden>"
        if orden not in ["PRE","POST"]:
            return "Error. Orden no valido, indique PRE o POST"
        
        expr = accion[2:]
        if not expr:
            return "Error. Ingrese parametro <expr>"

        resultado = calcular_expresion_prefijo("EVAL", expr) if orden == "PRE" else calcular_expresion_postfijo("EVAL", expr)
        return resultado

    elif accion[0] == "MOSTRAR":
        try:
            orden = accion[1]
        except:
            return "Error. Ingrese parametro <orden>"
        if orden not in ["PRE","POST"]:
            return "Error. Orden no valido, indique PRE o POST"

        expr = accion[2:]
        if not expr:
            return "Error. Ingrese parametro <expr>"

        resultado = calcular_expresion_prefijo("MOSTRAR", expr) if orden == "PRE" else calcular_expresion_postfijo("MOSTRAR", expr)

        return resultado

    elif accion[0] == "SALIR":

        exit()
    else:
        return "Error. Accion no es valida, indique si es EVAL, MOSTRAR o SALIR"