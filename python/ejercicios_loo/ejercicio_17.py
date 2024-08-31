"""
Se ingresa por consola un número entero que representa un sueldo que se debe pagar. 
Considerando que existen billetes de las denominaciones que se indican más abajo; 
informar, que cantidad de billetes de cada denominación se deberá utilizar, 
dando prioridad a los de valor nominal más alto. 
Denominaciones ($) = {100, 50, 20, 10, 5, 2, 1}
"""


def cuantos_billetes(importe):
    """Calcula la cantidad de billetes de cada denominación
    a entregar para cumplir con el importe que se pasa por parámetro"""

    billetes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for billete in billetes:
        contador_de_billetes = importe // billete
        importe = importe % billete
        if contador_de_billetes > 0:
            print(contador_de_billetes, " billetes de ", billete)


sueldo = int(input("Indique el importe a abonar: "))
cuantos_billetes(sueldo)
