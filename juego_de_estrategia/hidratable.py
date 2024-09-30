"""Interface Hidratable para el Soldado y el Caballo"""

from abc import abstractmethod
from abc import ABCMeta


class Hidratable(metaclass=ABCMeta):

    @abstractmethod
    def beber_agua(self):
        pass
