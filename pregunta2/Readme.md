# EXAMEN 2 - CI3641 - PREGUNTA 2
# AMARANTA VILLEGAS 16-11247

## Instrucciones de Ejecucion

1. Abra la terminal o linea de comandos de linux (o alguna de sus distribuciones)
2. Navegue al directorio donde se encuentra el codigo fuente.
3. Ejecute el programa con los siguiente comando :

    Si desea probar el programa mediante acciones ingresadas por input, coloque este comando:

    ``` python3 cliente.py ```
    
    Para probar las pruebas unitarias y la cobertura, coloque estos comandos:

    ```python3 -m unittest -v test_pruebas_unitarias.py ```

    ```coverage run -m unittest discover``

    ```coverage report```


4. Requisitos del Sistema

- Se requiere tener instalado una version de python superior a la 3.8.10
-debe tener instalado la herramienta de analisis de cobertura de codigo para python "coverage", para ello vaya a su terminal e ingrese el siguiente comando:

```pip install coverage```
- Sistema operativo: Linux (puede funcionar en otros sistemas, pero se ha probado en estos).