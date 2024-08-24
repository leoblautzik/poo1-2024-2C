""" Encriptar un mensaje usando el método de "la cifra del césar", 
que consiste en correr cada letra -considerando la posición de 
cada una en el alfabeto- una determinada cantidad de lugares. 
Ejemplo: si el corrimiento es de 2 lugares, la palabra "HOLA" se transforma en "JQNC". 
Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, 
se vuelve a comenzar desde la letra "a".
"""


def encriptar_letra(l, d):
    """Devuelve la letra resultante de hacer el corrimiento
    indicado por d"""
    return chr(((ord(l) - 65 + d) % 26) + 65)


def desencriptar_letra(l, d):
    """Devuelve la letra resultante de hacer el corrimiento inverso"""
    return chr(((ord(l) - d + 65) % 26) + 65)


def encriptar_palabra(p, d):
    """Devuelve la palabra encriptada"""
    pe = ""
    for letra in p:
        pe += encriptar_letra(letra, d)
    return pe


def desencriptar_palabra(p, d):
    """Devuelve la palabra desencriptada"""
    pe = ""
    for letra in p:
        pe += desencriptar_letra(letra, d)
    return pe


# Main
palabra = input("Ingrese la palabra a encriptar: ")
despl = int(input("Ingrese el corrimiento: "))
palabra = palabra.upper()

palabra_encriptada = encriptar_palabra(palabra, despl)
print(palabra_encriptada)
print(desencriptar_palabra(palabra_encriptada, despl))
