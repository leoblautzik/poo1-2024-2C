""" Se ingresa por teclado un conjunto de valores numéricos 
enteros positivos, se pide informar, por cada uno, 
si el valor ingresado es par o impar. 
Para indicar el final se ingresará un valor cero o negativo.
"""
v = int(input("Ingrese un valor entero positivo: "))

while v > 0:
    if v % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    v = int(input("Ingrese un valor entero positivo: "))

print("Fin")
