from state import *
#realizando casos de testes da nossa maquina de estado

contexto = Contexto(DraftState())
print("\n\nComeçamos no draft, agora vamos simular a publicacao pelo usuario, que deve levar ao Moderation\n")
contexto.requisicao1()
print("\n\nApós aprovado pelo admin, deveir ao Published\n")
contexto.requisicao1()
print("\n\nExpirada a publicação, voltamos ao Draft\n")
contexto.requisicao1()

print("\n\nVoltando ao draft, agora vamos simular a publicacao pelo admin, que deve levar ao Published\n")
contexto.requisicao2()
print("\n\nExpirada a publicação, voltamos ao Draft\n")
contexto.requisicao1()

