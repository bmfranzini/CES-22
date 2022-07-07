from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def bolo_recheio(self) -> None:
        pass

    @abstractmethod
    def bolo_cobertura(self) -> None:
        pass


class BoloCenouraCasamentoBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloCenouraCasamento()

    @property
    def product(self) -> BoloCenouraCasamento:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Cenoura")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Casamento")


class BoloCenouraCasamento():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloMandiocaCasamentoBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloMandiocaCasamento()

    @property
    def product(self) -> BoloMandiocaCasamento:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Mandioca")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Casamento")


class BoloMandiocaCasamento():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloChocolateCasamentoBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloChocolateCasamento()

    @property
    def product(self) -> BoloChocolateCasamento:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Chocolate")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Casamento")


class BoloChocolateCasamento():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloCenouraAniversarioBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloCenouraAniversario()

    @property
    def product(self) -> BoloCenouraAniversario:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Cenoura")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Aniversario")


class BoloCenouraAniversario():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloMandiocaAniversarioBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloMandiocaAniversario()

    @property
    def product(self) -> BoloMandiocaAniversario:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Mandioca")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Aniversario")


class BoloMandiocaAniversario():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloChocolateAniversarioBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloChocolateAniversario()

    @property
    def product(self) -> BoloChocolateAniversario:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Chocolate")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para Aniversario")


class BoloChocolateAniversario():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloCenouraFestaInformalBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloCenouraFestaInformal()

    @property
    def product(self) -> BoloCenouraFestaInformal:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Cenoura")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para FestaInformal")


class BoloCenouraFestaInformal():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloMandiocaFestaInformalBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloMandiocaFestaInformal()

    @property
    def product(self) -> BoloMandiocaFestaInformal:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Mandioca")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para FestaInformal")


class BoloMandiocaFestaInformal():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class BoloChocolateFestaInformalBuilder(Builder):

    def __init__(self) -> None:

        self.reset()

    def reset(self) -> None:
        self._product = BoloChocolateFestaInformal()

    @property
    def product(self) -> BoloChocolateFestaInformal:
        product = self._product
        self.reset()
        return product

    def bolo_recheio(self) -> None:
        self._product.add("Recheio de Chocolate")

    def bolo_cobertura(self) -> None:
        self._product.add("Cobertura para FestaInformal")


class BoloChocolateFestaInformal():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def descricao_bolo(self) -> None:
        print(f"Tipo do bolo: {', '.join(self.parts)}\n", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def fazer_bolo(self) -> None:
        self.builder.bolo_recheio()
        self.builder.bolo_cobertura()