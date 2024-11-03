"""Entrenadores"""


class Entrenadores:

    def entrenados_por(self, entrenadores):
        entrenados = {}

        for entrenador, socios in entrenadores.items():
            for s in socios:
                l = entrenados.get(s, [])
                l.append(entrenador)
                entrenados.update({s: l})

        return entrenados


# main

dicc = {
    "Bielsa": ["Juan", "Alberto", "Vero", "Tucu"],
    "Alvarez": ["Tom", "Vero", "Alberto"],
    "Melli": ["Tucu", "Alberto"],
}

ep = Entrenadores()
print(ep.entrenados_por(dicc))
