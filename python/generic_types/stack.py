from typing import TypeVar, Generic

T = TypeVar("T")


class Pila:
    """Pila NO GENERICA"""

    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        """apilar"""
        self.items.append(item)

    def pop(self):
        """desapilar"""
        return self.items.pop()

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


class Stack(Generic[T]):
    """Pila Generica"""

    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        """apila un elemento de tipo T"""
        self.items.append(item)

    def pop(self) -> T:
        """desapila el tope de la pila y devuelve un elemento de tipo T"""
        return self.items.pop()

    def is_empty(self) -> bool:
        """pila vacia"""
        return len(self.items) == 0


def main() -> None:
    """main"""
    pila = Pila()
    pila.push(2)  # OK
    pila.push("x")  # OK pero tendremos una pila con elementos de diferentes tipos
    print(pila.pop())
    print(pila.pop())

    stack = Stack[int]()
    stack.push(2)  # OK
    print(stack.pop())  # OK
    # stack.push("x") # error, solo se permmite apilar elementos de tipo int


if __name__ == "__main__":
    main()
