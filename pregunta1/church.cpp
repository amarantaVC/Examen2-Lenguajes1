/*
CI3641 - LENGUAJES DE PROGRAMACION I 
EXAMEN2 - PREGUNTA 1
AMARANTA VILLEGAS 16-11247
Numerales de Church
*/

#include <iostream>
using namespace std;

// Estructura para representar un numeral de Church
class Church {

public:
    // Puntero al numeral de Church
    Church* numeral;
    // Constructor para crear un numeral de Church
    Church() : numeral(nullptr) {}

    // Constructor para crear un numeral de Church a partir de otro
    Church(Church* num) : numeral(num) {}

    // Función para crear un sucesor de un numeral de Church
    Church* Suc() {
        return new Church(this);
    }

    // Función para convertir un numeral de Church a un entero
    int toInt() {
        int inicial = 0;
        Church* actual = this->numeral;
        while (actual != nullptr) {
            inicial++;
            actual = actual->numeral;
        }
        return inicial;
    }

    // Función para sumar dos numerales de Church
    Church* suma(Church* m) {
        if (m->numeral == nullptr) {
            return this;
        }
        return this->suma(m->numeral)->Suc();
    }

    // Función para multiplicar dos numerales de Church
    Church* multiplicacion(Church* m) {
        if (m->numeral == nullptr) {
            return m;
        }
        return this->suma(this->multiplicacion(m->numeral));
    }
};

// Función para convertir un entero a un numeral de Church
Church* intToChurch(int n) {
    Church* church = new Church();
    while (n != 0) {
        church = church->Suc();
        n--;
    }
    return church;
}

// Función para convertir un numeral de Church a un entero
int main() {

    // Ejemplos de uso de la clase Church
    Church zero;

    Church* zero_zero_zero = zero.Suc()->Suc()->Suc();

    Church a(new Church(new Church()));

    Church* b = a.Suc()->Suc();

    Church* c = a.Suc()->Suc()->Suc()->Suc();

    // d es el resultado de convertir el entero 20 a un numeral de Church
    Church* d = intToChurch(20);

    printf("| Numerales de Church |\n\n");
    
    cout << "zero = " << zero.toInt() << endl;
    cout << "zero_zero_zero = " << zero_zero_zero->toInt() << "\n" <<endl;

    cout << "a = " << a.toInt() << endl;
    cout << "b = " << b->toInt() << endl;
    cout << "c = " << c->toInt() << endl;

    cout << "d = " << d->toInt() << "\n" <<endl;
    cout << "suma d + b = " << d->suma(b)->toInt() <<"\n" <<endl;
    cout << "multiplicacion a*b = " << a.multiplicacion(b)->toInt() << "\n" <<endl;
    cout << "multiplicacion a*b*c = " << a.multiplicacion(b)->multiplicacion(c)->toInt() << "\n" <<endl;
    
    return 0;
}
