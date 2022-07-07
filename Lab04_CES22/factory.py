from __future__ import annotations
from abc import ABC, abstractmethod

# classe criadora para implementar o pattern de factory para criar veiculos
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def descricao_creator(self) -> str:
        product = self.factory_method()
        result = f"O veiculo feito foi: {product.descricao_veiculo()}"
        return result

# criadores concretos dos tipos de veiculo
class FazerCarro(Creator):
    def factory_method(self) -> Product:
        return Carro()


class FazerCaminhao(Creator):
    def factory_method(self) -> Product:
        return Caminhao()


class FazerMoto(Creator):
    def factory_method(self) -> Product:
        return Moto()

# classe abstrata para ser a base dos produtos feitos na factory (carro, moto e caminhao)
class Product(ABC):
    @abstractmethod
    def descricao_veiculo(self) -> str:
        pass

# classes concretas dos produtos carro, moto e caminhao em si
class Carro(Product):
    def descricao_veiculo(self) -> str:
        return "Carro"


class Caminhao(Product):
    def descricao_veiculo(self) -> str:
        return "Caminhao"


class Moto(Product):
    def descricao_veiculo(self) -> str:
        return "Moto"

# funcao que faz a requisicao para a criacao na fabrica, passando um criador concreto como parâmetro
def client_code_factory(creator: Creator) -> None:
    print(creator.descricao_creator(), end="")
