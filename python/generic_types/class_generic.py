from typing import TypeVar, Generic

T = TypeVar("T")


class Contenedor(Generic[T]):

    def __init__(self, contenido: T):
        self.contenido = contenido

    def get_contenido(self) -> T:
        return self.contenido

    def set_contenido(self, nuevo_contenido: T) -> None:
        self.contenido = nuevo_contenido


def main() -> None:
    c_int = Contenedor[int](10)
    a = c_int.get_contenido() + 1
    print(a)
    # c_int.set_contenido("x")

    c_str = Contenedor[str]("Oi")
    b = c_str.get_contenido() + "3"
    print(b)
    # c_str.set_contenido(10)


if __name__ == "__main__":
    main()
