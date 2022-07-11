from __future__ import annotations
from abc import ABC, abstractmethod


#criamos o contexto e as funcoes correspondentes ao design pattern State
class Contexto:

    _state = None

    def __init__(self, state: State) -> None:
        self.transicao_para(state)

    def transicao_para(self, state: State):

        print(f"Agora vamos para o estado {type(state).__name__}")
        self._state = state
        self._state.contexto = self

    def requisicao1(self):
        self._state.transicao1()

    def requisicao2(self):
        self._state.transicao2()


#criamos a classe abstrata State, que servira de base para os estados concretos
class State(ABC):
    @property
    def contexto(self) -> Contexto:
        return self._contexto

    @contexto.setter
    def contexto(self, contexto: Contexto) -> None:
        self._contexto = contexto

    @abstractmethod
    def transicao1(self) -> None:
        pass

    @abstractmethod
    def transicao2(self) -> None:
        pass


# criamos os estados concretos Draft, Moderation e Published da nossa maquina de estados
class DraftState(State):
    def transicao1(self) -> None:
        print("Published by User -> Agora vamos para o estado: Moderation")
        self.contexto.transicao_para(ModerationState())

    def transicao2(self) -> None:
        print("Published by Admin -> Agora vamos para o estado: Published")
        self.contexto.transicao_para(PublishedState())


class ModerationState(State):
    def transicao1(self) -> None:
        print("Approved by Admin -> Agora vamos para o estado: Published")
        self.contexto.transicao_para(PublishedState())

    def transicao2(self) -> None:
        print("Review Failed -> Agora vamos para o estado: Draft")
        self.contexto.transicao_para(DraftState())


class PublishedState(State):
    def transicao1(self) -> None:
        print("Publication expired -> Agora vamos para o estado: Draft")
        self.contexto.transicao_para(DraftState())

    def transicao2(self) -> None:
        pass



