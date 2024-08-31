""""26-Invertir un string, sin usar la biblioteca que lo haga 
    automáticamente.
    27-Escribir una función que reciba un string y lo 
    devuelva invertido. 
    Por ejemplo: invertirCadena("Hola"),retorna "aloH". 
    Reutilice la función implementada para decir si una palabra es o no,
    un palíndromo. 
    esPalindromo("neuquen") devuelve true.
"""


def invertir(a):
    """Devuelve una cadena resultado de invertir
    la que se recibe por parametro
    """
    b = ""
    for i in range(0, len(a), 1):
        b = a[i] + b
    return b


def es_palindromo(a):
    s = a.lower()
    s = sin_acentos(s)
    s = sin_signos_de_puntuacion(s)
    s = sin_espacios(s)

    return s == invertir(s)


def sin_espacios(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] != " ":
            b = b + a[i]
    return b


def sin_signos_de_puntuacion(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] != "," and a[i] != "." and a[i] != ";":
            b = b + a[i]
    return b


def sin_acentos(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] == "á":
            b = b + "a"
        elif a[i] == "é":
            b = b + "e"
        elif a[i] == "í":
            b = b + "i"
        elif a[i] == "ó":
            b = b + "o"
        elif a[i] == "ú":
            b = b + "u"
        else:
            b = b + a[i]
    return b


s = "Hola"
print(s)
print(invertir(s))

p = "neuquen"
print(es_palindromo(p))
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
print(es_palindromo("aña"))
