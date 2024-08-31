"""Escribir una función que reciba una cadena de 
caracteres muestre por pantalla la frecuencia de 
aparición de cada letra. """

# hola como estas


def frecuencia(s):
    """Frec"""
    f = []
    for i in range(26):
        f.append(0)

    s = s.upper()
    for l in s:
        pos = ord(l) - 65
        if 0 <= pos <= 25:
            f[pos] += 1

    for i in range(26):
        if f[i] != 0:
            print(chr(i + 65), ":", f[i])


palabra = input("Ingrese una frase: ")
frecuencia(palabra)
