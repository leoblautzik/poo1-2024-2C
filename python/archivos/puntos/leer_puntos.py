"""Leer puntos"""

from punto import Punto
from punto import EstaSobreUnEjeException

with open("puntos.in", "r", encoding="utf-8") as file:
    puntos = []
    for cada_linea in file:
        coordenadas = cada_linea.split(",")
        x = float(coordenadas[0])
        y = float(coordenadas[1])
        puntos.append(Punto(x, y))
with open("c1.txt", "w", encoding="utf-8") as c1, open(
    "c2.txt", "w", encoding="utf-8"
) as c2, open("c3.txt", "w", encoding="utf-8") as c3, open(
    "c4.txt", "w", encoding="utf-8"
) as c4:
    for p in puntos:
        try:
            if p.pertenece_al_cuadrante() == 1:
                c1.write(str(p) + "\n")
            if p.pertenece_al_cuadrante() == 2:
                c2.write(str(p))
            if p.pertenece_al_cuadrante() == 3:
                c3.write(str(p))
            if p.pertenece_al_cuadrante() == 4:
                c4.write(str(p))
        except EstaSobreUnEjeException:
            print("El punto " + str(p) + " esta sobre uno de los ejes")
