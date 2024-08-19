"""
Leer tres valores numéricos enteros, indicar cual es el mayor, 
cuál es el del medio y cuál el menor. 
Considerar que los tres valores son diferentes.
"""

a = int(input("Ingrese un entero: "))
b = int(input("Ingrese otro entero: "))
c = int(input("Ingrese otro entero mas: "))

mayor = a

if b > a:
    medio = a
    mayor = b
else:
    medio = b

if c > mayor:
    menor = medio
    medio = mayor
    mayor = c
elif c > medio:
    menor = medio
    medio = c
else:
    menor = c

print("Mayor:", mayor, "Medio:", medio, "Menor:", menor)
