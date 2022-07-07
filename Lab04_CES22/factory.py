from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def descricao_creator(self) -> str:
        product = self.factory_method()
        result = f"O veiculo feito foi: {product.descricao_veiculo()}"
        return result


class FazerCarro(Creator):
    def factory_method(self) -> Product:
        return Carro()


class FazerCaminhao(Creator):
    def factory_method(self) -> Product:
        return Caminhao()


class FazerMoto(Creator):
    def factory_method(self) -> Product:
        return Moto()


class Product(ABC):
    @abstractmethod
    def descricao_veiculo(self) -> str:
        pass


class Carro(Product):
    def descricao_veiculo(self) -> str:
        return "Carro"


class Caminhao(Product):
    def descricao_veiculo(self) -> str:
        return "Caminhao"


class Moto(Product):
    def descricao_veiculo(self) -> str:
        return "Moto"


def client_code_factory(creator: Creator) -> None:
    print(creator.descricao_creator(), end="")