from __future__ import annotations
from abc import ABC, abstractmethod

# classe abstrata para a implementação do pattern bridge
class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def descricao(self) -> str:
        return (f" com a tecnologia:\n"
                f"\t{self.implementation.descricao_motor()}")

# implementacao das caracteristicas que serao modeladas pela ponte (tipo do motor)
class Implementation(ABC):

    @abstractmethod
    def descricao_motor(self) -> str:
        pass

# classes concretas de tipos de motores herdadas da abstrata
class MotorEletrico(Implementation):
    def descricao_motor(self) -> str:
        return "Motor elétrico."


class MotorACombustao(Implementation):
    def descricao_motor(self) -> str:
        return "Motor à combustão."


class MotorHibrido(Implementation):
    def descricao_motor(self) -> str:
        return "Motor híbrido."

# funcao de requisicao que recebe uma instancia da classe abstrata "Abstraction" 
def client_code_bridge(abstraction: Abstraction) -> None:
    print(abstraction.descricao(), end="")

