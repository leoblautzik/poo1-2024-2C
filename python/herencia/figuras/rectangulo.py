from figura import Figura


class Rectangulo(Figura):

    def __init__(self, base, altura):
        super().__init__(base * altura)
