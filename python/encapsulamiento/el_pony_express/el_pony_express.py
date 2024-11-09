"""
Había una cierta cantidad de estaciones, donde cada jinete cambiaba su caballo 
por uno fresco, o se le pasaba la bolsa de correo a un relevo.

El problema (versión java)
Se te pide ayuda para implementar el siguiente método:
/**
 * @param distancias es la distancia en millas de una estación hasta la otra
 * @returns la cantidad de caballos necesarios para enviar el correo desde un
 * extremo hasta el otro del recorrido
 */
public int caballos(int[] distancias) { //TODO }

Nota: Cada caballo viaja tan lejos como puede, pero nunca lo hace más de 100 millas seguidas
"""


def caballos(distancias):
    """calcula cuantos caballos son necesarios para cubrir la ruta definida
    por la lista de distancias entre estaciones"""
    resto = 100
    c = 1
    for d in distancias:
        if d > 100:
            raise ValueError("La ruta es inaccesible")
        if d <= resto:
            resto -= d
        else:
            c += 1
            resto = 100 - d
    return c
