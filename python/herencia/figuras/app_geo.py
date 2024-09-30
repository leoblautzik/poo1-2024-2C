"""Main"""

from elipse import Elipse
from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from triangulo import Triangulo


def main():
    """Se declaran varias figuras, se agregan a una lista y
    se ordena la lista de menor a mayor area"""
    c1 = Circulo(5)
    e1 = Elipse(4, 5)
    r1 = Rectangulo(2, 6)

    figuras = []

    figuras.append(c1)
    figuras.append(Rectangulo(6, 2))
    figuras.append(e1)
    figuras.append(r1)
    figuras.append(Triangulo(3, 4))
    figuras.append(Cuadrado(4))

    for f in figuras:
        print(f.get_area())

    figuras.sort()

    print("\nOrdenados:\n")
    for f in figuras:
        # cada figura se muestra de acuerso al str
        print(f)


main()
