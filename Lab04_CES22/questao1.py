from bridge import *
from factory import *

print("Vamos fazer um carro com motor eletrico")
fazerCarro = FazerCarro()
client_code_factory(fazerCarro)
implementation = MotorEletrico()
abstraction = Abstraction(implementation)
client_code_bridge(abstraction)

print("\n")

print("Vamos fazer uma moto com motor à combustão")
fazerMoto = FazerMoto()
client_code_factory(fazerMoto)
implementation = MotorACombustao()
abstraction = Abstraction(implementation)
client_code_bridge(abstraction)

print("\n")

print("Vamos fazer um caminhao com motor hibrido")
fazerCaminhao = FazerCaminhao()
client_code_factory(fazerCaminhao)
implementation = MotorHibrido()
abstraction = Abstraction(implementation)
client_code_bridge(abstraction)
