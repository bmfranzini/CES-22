from __future__ import annotations
from abc import ABC, abstractmethod

class FabricaBoloAbstrata(ABC):

    @abstractmethod
    def criar_bolo_cenoura(self) -> BoloCenouraAbstrato:
        pass

    @abstractmethod
    def criar_bolo_mandioca(self) -> BoloMandiocaAbstrato:
        pass
    
    @abstractmethod
    def criar_bolo_chocolate(self) -> BoloChocolateAbstrato:
        pass

class FabricaBoloCasamento(FabricaBoloAbstrata):

    def criar_bolo_cenoura(self) -> BoloCenouraAbstrato:
        return BoloCenouraCasamento()

    def criar_bolo_mandioca(self) -> BoloMandiocaAbstrato:
        return BoloMandiocaCasamento()

    def criar_bolo_chocolate(self) -> BoloChocolateAbstrato:
        return BoloChocolateCasamento()


class FabricaBoloAniversario(FabricaBoloAbstrata):

    def criar_bolo_cenoura(self) -> BoloCenouraAbstrato:
        return BoloCenouraAniversario()

    def criar_bolo_mandioca(self) -> BoloMandiocaAbstrato:
        return BoloMandiocaAniversario()

    def criar_bolo_chocolate(self) -> BoloChocolateAbstrato:
        return BoloChocolateAniversario()


class FabricaBoloFestaInformal(FabricaBoloAbstrata):

    def criar_bolo_cenoura(self) -> BoloCenouraAbstrato:
        return BoloCenouraFestaInformal()

    def criar_bolo_mandioca(self) -> BoloMandiocaAbstrato:
        return BoloMandiocaFestaInformal()

    def criar_bolo_chocolate(self) -> BoloChocolateAbstrato:
        return BoloChocolateFestaInformal()


class BoloCenouraAbstrato(ABC):

    @abstractmethod
    def descricao_bolo_cenoura(self) -> str:
        pass


class BoloCenouraCasamento(BoloCenouraAbstrato):
    def descricao_bolo_cenoura(self) -> str:
        return "Está feito um bolo de cenoura para casamento"

class BoloCenouraAniversario(BoloCenouraAbstrato):
    def descricao_bolo_cenoura(self) -> str:
        return "Está feito um bolo de cenoura para aniversário"

class BoloCenouraFestaInformal(BoloCenouraAbstrato):
    def descricao_bolo_cenoura(self) -> str:
        return "Está feito um bolo de cenoura para festa informal"


class BoloMandiocaAbstrato(ABC):

    @abstractmethod
    def descricao_bolo_mandioca(self) -> str:
        pass


class BoloMandiocaCasamento(BoloMandiocaAbstrato):
    def descricao_bolo_mandioca(self) -> str:
        return "Está feito um bolo de Mandioca para casamento"

class BoloMandiocaAniversario(BoloMandiocaAbstrato):
    def descricao_bolo_mandioca(self) -> str:
        return "Está feito um bolo de Mandioca para aniversário"

class BoloMandiocaFestaInformal(BoloMandiocaAbstrato):
    def descricao_bolo_mandioca(self) -> str:
        return "Está feito um bolo de Mandioca para festa informal"


class BoloChocolateAbstrato(ABC):

    @abstractmethod
    def descricao_bolo_chocolate(self) -> str:
        pass


class BoloChocolateCasamento(BoloChocolateAbstrato):
    def descricao_bolo_chocolate(self) -> str:
        return "Está feito um bolo de chocolate para casamento"

class BoloChocolateAniversario(BoloChocolateAbstrato):
    def descricao_bolo_chocolate(self) -> str:
        return "Está feito um bolo de chocolate para aniversário"

class BoloChocolateFestaInformal(BoloChocolateAbstrato):
    def descricao_bolo_chocolate(self) -> str:
        return "Está feito um bolo de chocolate para festa informal"


def requisicao(factory: FabricaBoloAbstrata) -> None:

    boloCenoura = factory.criar_bolo_cenoura()
    boloMandioca = factory.criar_bolo_mandioca()
    boloChocolate = factory.criar_bolo_chocolate()

    print("Usando a fabrica de bolo de cenoura:")
    print(f"{boloCenoura.descricao_bolo_cenoura()}")
    print("Usando a fabrica de bolo de mandioca:")
    print(f"{boloMandioca.descricao_bolo_mandioca()}")
    print("Usando a fabrica de bolo de chocolate:")
    print(f"{boloChocolate.descricao_bolo_chocolate()}")

