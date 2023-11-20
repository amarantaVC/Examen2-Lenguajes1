"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 5
AMARANTA VILLEGAS 16-11247
Archivo main.py que tendra la funcion main para el simulador de manejador de tipos de datos
"""

# creamos la clase tipo que tendra la informacion de cada tipo de dato y sus metodos
class Tipo:

    def __init__(self, nombre, representacion, alineacion) -> None:
        self.nombre = nombre
        self.representacion = int(representacion)
        self.alineacion = int(alineacion)
        self.sinP = [self.representacion, self.alineacion, 0]
        self.emp = [self.representacion, self.alineacion, 0]
        self.ord = [self.representacion, self.alineacion, 0]

#creamos la clase manejador de tipos que tendra la informacion de los tipos de datos y sus metodos tales como definir y describir
class ManejadorDeTipos:

    def __init__(self) -> None:
        self.tiposG = {}

    def definir_atomico(self, atomico) -> bool:
        if self.tiposG.get(atomico[0]) is not None:
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False
        self.tiposG[atomico[0]] = Tipo(*atomico)
        print(f"Definición exitosa. Se ha creado un tipo atómico llamado '{atomico[0]}'.\n")
        return True

    def definir_struct(self, struct) -> bool:
        if self.tiposG.get(struct[0]) is not None:
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False

        for i in struct[1:]:
            if self.tiposG.get(i) is None:
                print(f"Error, el tipo {i} no está definido.")
                return False

        self.tiposG[struct[0]] = Tipo(struct[0], struct[1], self.tiposG)
        print(f"Definición exitosa. Se ha creado un tipo estructura llamado '{struct[0]}'.\n")
        return True

    def definir_union(self, union) -> bool:
        if self.tiposG.get(union[0]) is not None:
            print("Error, el nombre especificado ya tiene un tipo asociado.")
            return False
        for i in union[1:]:
            if self.tiposG.get(i) is None:
                print(f"Error, el tipo {i} no está definido.")
                return False

        self.tiposG[union[0]] = Tipo(union[0], union[1], self.tiposG)
        print(f"Definición exitosa. Se ha creado un tipo unión llamado '{union[0]}'.\n")
        return True

    def describir_tipo(self, tipo) -> list:
        t = self.tiposG.get(tipo)
        if t is None:
            print("Error, el nombre especificado no tiene un tipo asociado.")
            return [None, None, None]
        print(f"El tipo asociado al nombre especificado tiene la siguiente información:\n"
              f"-----------------------------------------------------------------------\n"
              f"Sin empaquetar:\nTamaño total del tipo: {t.sinP[0]} bytes.\n"
              f"Alineación del tipo: {t.sinP[1]} bytes.\nEspacio total desperdiciado: {t.sinP[2]} bytes.\n"
              f"-----------------------------------------------------------------------\n"
              f"Empaquetado:\nTamaño total del tipo: {t.emp[0]} bytes.\n"
              f"Alineación del tipo: {t.emp[1]} bytes.\nEspacio total desperdiciado: {t.emp[2]} bytes.\n"
              f"-----------------------------------------------------------------------\n"
              f"Ordenado de manera óptima:\nTamaño total del tipo: {t.ord[0]} bytes.\n"
              f"Alineación del tipo: {t.ord[1]} bytes.\nEspacio total desperdiciado: {t.ord[2]} bytes.")
        return [t.sinP, t.emp, t.ord]

# main
def main():
    print("------- Simulador de manejador de tipo de datos -------")
    manejador = ManejadorDeTipos()
    while True:
        print("Elija una opción: 'ATOMICO' 'STRUCT' 'UNION' 'DESCRIBIR' 'SALIR'.")
        opcion = input().split()
        if opcion[0] == "ATOMICO":
            manejador.definir_atomico(opcion[1:])
        elif opcion[0] == "STRUCT":
            manejador.definir_struct(opcion[1:])
        elif opcion[0] == "UNION":
            manejador.definir_union(opcion[1:])
        elif opcion[0] == "DESCRIBIR":
            manejador.describir_tipo(opcion[1])
        elif opcion[0] == "SALIR":
            break
        else:
            print("Error, por favor ingrese una opcion valida.")

if __name__ == '__main__':
    main()
