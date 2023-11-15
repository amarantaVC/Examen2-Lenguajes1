/*
CI3641 - LENGUAJES DE PROGRAMACION I 
EXAMEN2 - PREGUNTA 1
AMARANTA VILLEGAS 16-11247
Arbol Binario
*/


#include <iostream>
#include <vector>
using namespace std;

// Estructura para representar un árbol binario
struct Arbol {
    int info;
    Arbol* hijoIzq;
    Arbol* hijoDer;
};

// Variables globales usadas para almacenar el recorrido de los algoritmos
vector<int> preorder;
vector<int> postorder;

// Función para recorrer el árbol en pre-order
void recorridoPreOrder(Arbol* a) {
    // Si el árbol no está vacío, recorremos el árbol en pre-order
    if (a != nullptr) {
        // Agregamos el valor de la raíz al vector preorder
        preorder.push_back(a->info);
        recorridoPreOrder(a->hijoIzq);
        recorridoPreOrder(a->hijoDer);
    }
}

// Función para recorrer el árbol en post-order
void recorridoPostOrder(Arbol* a) {
    // Si el árbol no está vacío, recorremos el árbol en post-order
    if (a != nullptr) {
        recorridoPostOrder(a->hijoIzq);
        recorridoPostOrder(a->hijoDer);
        // Agregamos el valor de la raíz al vector postorder
        postorder.push_back(a->info);
    }
}

// Función para determinar si es un max heap
bool esMaxHeap(Arbol* nodoRaiz) {

    // Si el árbol está vacío, es un max heap
    if (nodoRaiz == nullptr) {
        return true;
    }
    // Si el árbol no está vacío, comparamos el valor de la raíz con el de sus hijos de la izquierda
    if (nodoRaiz->hijoIzq != nullptr) {
        if (nodoRaiz->info < nodoRaiz->hijoIzq->info) {
            return false;
        }
        if (!esMaxHeap(nodoRaiz->hijoIzq)) {
            return false;
        }
    }
    // Si el árbol no está vacío, comparamos el valor de la raíz con el de sus hijos de la derecha
    if (nodoRaiz->hijoDer != nullptr) {
        if (nodoRaiz->info < nodoRaiz->hijoDer->info) {
            return false;
        }
        if (!esMaxHeap(nodoRaiz->hijoDer)) {
            return false;
        }
    }

    return true;
}

// Función para comparar si dos vectores son iguales
bool iguales(vector<int> a, vector<int> b) {

    // Si los vectores no tienen el mismo tamaño, no son iguales
    if (a.size() != b.size()) {
        return false;
    }
    // Si los vectores tienen el mismo tamaño, comparamos cada elemento
    for (size_t i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

//funcion para determinar si un arbol es un max heap simetrico o no.
bool esMaxHeapSimetrico(Arbol* A) {

    //limpiamos los vectores para que no se acumulen los valores de los arboles anteriores
    preorder.clear();
    postorder.clear();

    //llamamos a las funciones para recorrer el arbol en pre-order y post-order
    recorridoPreOrder(A);
    recorridoPostOrder(A);

    //comparamos los vectores para determinar si el arbol es un max heap simetrico o no
    if (esMaxHeap(A)) {
        if (iguales(preorder, postorder)) {
            cout << "El árbol es un max heap simétrico \n" << endl;
            return true;
        } else {
            cout << "El árbol es un max heap pero no es simétrico \n" << endl;
            return false;
        }
    }
    cout << "El árbol no es un max heap \n" << endl;
    return false;
}

// Función main para probar si un árbol es un max heap simétrico o no. 
int main() {

    //Definimos dos arboles para probar la funcion esMaxHeapSimetrico
    Arbol* primerArbol = new Arbol{5, 
    new Arbol{4, 
        new Arbol{3, nullptr, nullptr}, 
        new Arbol{2, nullptr, nullptr}}, 
    new Arbol{3, 
        new Arbol{2, nullptr, nullptr}, 
        new Arbol{1, nullptr, nullptr}}
        };

        //arbol 1

    //         5
    //	     /   \
    // 	   4       3
    //	 /  \     /  \
    //  3    2   2    1

    //llamamos a la funcion esMaxHeapSimetrico para el primer arbol
    cout << "Primer arbol:" << endl;
    esMaxHeapSimetrico(primerArbol);

    Arbol* segundoArbol = new Arbol{5, 
    new Arbol{5, 
        new Arbol{5, nullptr, nullptr}, 
        new Arbol{5, nullptr, nullptr}}, 
    new Arbol{5, 
        new Arbol{5, nullptr, nullptr}, 
        new Arbol{5, nullptr, nullptr}}
        };

        //arbol 2

    //         5
    //	     /   \
    // 	   5       5
    //	 /  \     /  \
    //  5    5   5    5

    //llamamos a la funcion esMaxHeapSimetrico para el segundo arbol 
    cout << "Segundo arbol:" << endl;
    esMaxHeapSimetrico(segundoArbol);

    return 0;
}
