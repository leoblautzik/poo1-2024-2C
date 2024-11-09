"""Item sera el decorator abstracto"""

from abc import ABCMeta, abstractmethod
from unidad import Unidad


class Item(Unidad, metaclass=ABCMeta):

    @abstractmethod
    def puede_atacar(self, oponente) -> bool:
        pass

    @abstractmethod
    def infligir_danio(self, oponente) -> None:
        """El oponente recibe el danio inflingido por self"""

    @abstractmethod
    def sufrir_danio(self, danio) -> None:
        """self recibe el danio inflingido por el oponente"""
