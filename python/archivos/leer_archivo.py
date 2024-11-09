"""Leer archivo"""

# f = open("archivo.txt", "r")
# contenido = f.read()
# print(contenido)
# for linea in f:
#     print(linea.split(" "))
import io

with io.open("archivo.txt", "r", encoding="utf-8") as file:
    # lineas = file.readlines()
    for linea in file:
        linea = linea.replace("\n", "")
        linea = linea.split(" ")
        for palabra in linea:
            print(palabra)
