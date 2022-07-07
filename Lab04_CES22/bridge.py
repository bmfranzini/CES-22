from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def descricao(self) -> str:
        return (f" com a tecnologia:\n"
                f"\t{self.implementation.descricao_motor()}")


class Implementation(ABC):

    @abstractmethod
    def descricao_motor(self) -> str:
        pass


class MotorEletrico(Implementation):
    def descricao_motor(self) -> str:
        return "Motor elétrico."


class MotorACombustao(Implementation):
    def descricao_motor(self) -> str:
        return "Motor à combustão."


class MotorHibrido(Implementation):
    def descricao_motor(self) -> str:
        return "Motor híbrido."


def client_code_bridge(abstraction: Abstraction) -> None:
    print(abstraction.descricao(), end="")

