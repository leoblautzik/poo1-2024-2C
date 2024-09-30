"""Main"""

from elipse import Elipse
from circulo import Circulo
from rectangulo import Rectangulo


def main():
    c1 = Circulo(5)
    e1 = Elipse(4, 5)
    r1 = Rectangulo(2, 6)

    figuras = []

    figuras.append(c1)
    figuras.append(Rectangulo(6, 2))
    figuras.append(e1)
    figuras.append(r1)

    for f in figuras:
        print(f.get_area())
    print("\n Ordenados: \n")
    figuras.sort()
    for f in figuras:
        print(f.get_area())


main()
