from pizza import *


marguerita = QueijoMussarela(Manjericao(Tomate((MassaDePizza()))))
print(marguerita.getDescription() + ": $" + str(marguerita.getTotalCost()))
portuguesa = Ovo(Cebola(Presunto(QueijoMussarela(MassaDePizza()))))
print(portuguesa.getDescription() + ": $" + str(portuguesa.getTotalCost()))