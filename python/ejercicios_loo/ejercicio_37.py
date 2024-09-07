"""Escribir una función que reciba una cadena de 
caracteres muestre por pantalla la frecuencia de 
aparición de cada letra. """


def frecuencia(s) -> str:
    """Devuelve un string con la frecuencia de aparicion de cada letra en la cadena s"""
    info = ""
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
            info = info + chr(i + 65) + ":\t" + str(f[i]) + "\n"
            # print(chr(i + 65), ":", f[i])
    return info


def frecuencia_ascii(s) -> str:
    """Devuelve un string con la frecuencia de aparicion
    de cada letra (no cuenta los espacios) en la cadena s - Tabla ASCII extendida"""
    info = ""
    # Se define a f como una lista de 224 contadores
    # y se los inicializa a todos en cero
    f = []
    for i in range(224):
        f.append(0)

    # Se recorre la cadena s y para cada letra procesada
    # se incrementa en 1 el contador asociado a su código ascii
    for l in s:
        pos = ord(l) - 33
        if 0 <= pos <= 222:
            f[pos] += 1

    # Se recorre la lista de contadores y se construye un
    # string que contiene la info solicitada y que será retornado
    for i in range(222):
        if f[i] != 0:
            info = info + chr(i + 33) + ":\t" + str(f[i]) + "\n"

    return info


# palabra = input("Ingrese una frase: ")
print(
    frecuencia_ascii(
        "¿Hola cóno estás ñandú? ¿Qué tal te sientes después de la visita del pingüino?"
    )
)
print(frecuencia_ascii("Neovim ejecutando Python"))
