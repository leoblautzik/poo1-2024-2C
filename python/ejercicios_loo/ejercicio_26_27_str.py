""""26-Invertir un string, sin usar la biblioteca que lo haga
    automáticamente.
    27-Escribir una función que reciba un string y lo
    devuelva invertido.
    Por ejemplo: invertirCadena("Hola"),retorna "aloH".
    Reutilice la función implementada para decir si una palabra es o no,
    un palíndromo.
    esPalindromo("neuquen") devuelve true.
    VERSION STRING A LO PYTHON
"""


def invertir(a):
    """Devuelve una cadena resultado de invertir
    la que se recibe por parametro
    """
    b = ""
    for c in a:
        b = c + b
    return b


def es_palindromo(a):
    """Devuelve true o false según la cadena a sea no no palindromo"""
    a = a.lower()
    a = sin_acentos(a)
    a = sin_signos_de_puntuacion(a)
    a = sin_espacios(a)

    return a == invertir(a)


def sin_espacios(a):
    """Elimina todos los espacios de la cadena a"""
    b = ""
    for c in a:
        if c != " ":
            b = b + c
    return b


def sin_signos_de_puntuacion(a):
    """Elimina los signos de puntuacion de la cadena a"""
    b = ""
    for c in a:
        if c not in (",", ".", ";", ":"):
            b = b + c
    return b


def sin_acentos(a):
    """Reemplaza las vocales acentuadas por no acentuadas"""
    b = ""
    for c in a:
        if c == "á":
            b = b + "a"
        elif c == "é":
            b = b + "e"
        elif c == "í":
            b = b + "i"
        elif c == "ó":
            b = b + "o"
        elif c == "ú":
            b = b + "u"
        else:
            b = b + c
    return b


print("Hola Mundo")
print(invertir("Hola Mundo"))

print(es_palindromo("Neuquén"))
print(es_palindromo("a"))
print(es_palindromo(""))
print(es_palindromo("      A mi loca  Colima    "))
print(es_palindromo("A Mercedes, ese de crema."))
print(es_palindromo("A la catalana banal, atácala."))
print(
    es_palindromo(
        "Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida"
    )
)
print(es_palindromo("aña"))
print(es_palindromo("ñañañ"))
