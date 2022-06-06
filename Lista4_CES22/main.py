from Livraria import Livraria
from Produto import Livro
from Genero import Genero
from Imposto import Imposto
from Pessoa import Autor, Cliente
from Compra import Compra

impostoCDV = Imposto()
policial = Genero("policial")
DanBrown = Autor("Dan Brown", "danbrown@gmail.com", ["O codigo da Vinci", "Anjos e Demonios", "Origem"])
CodigoDaVinci = Livro("O codigo da Vinci", DanBrown, policial.genero, 1, "Sextante", 22, 30, impostoCDV.calcular_imposto(policial, 30))

impostoIT = Imposto()
terror = Genero("terror")
StephenKing = Autor("Stephen King", "stephenking@gmail.com", ["It - a coisa", "Mr. Mercedes"])
IT = Livro("It - a coisa", StephenKing, terror.genero, 3, "Suma", 27, 40, impostoIT.calcular_imposto(terror, 40))

compras = [1,2,3,4,43,55,67,87,91]
nobel = Livraria([CodigoDaVinci, IT], [DanBrown, StephenKing], compras, "Nobel")

compra3 = Compra([CodigoDaVinci], [2], 3)
compra43 = Compra([IT], [1], 43)

BrunoFranzini = Cliente("Bruno Franzini", "bruno.m.franzini@gmail.com", [compra3, compra43]) # cada compra tem um indice associado

nobel.inserir_cliente(BrunoFranzini)
nobel.consultar_cliente(BrunoFranzini)
nobel.alterar_cliente(BrunoFranzini, "email", "bmf@gmail.com")
nobel.alterar_livro(CodigoDaVinci, "titulo", "O CODIGO DA VINCI")
nobel.consultar_cliente(BrunoFranzini)
nobel.alterar_compra(compra3, "listaQuantidades", 0, 4)
nobel.consultar_compra(compra3)
nobel.remover_compra(compra3)
nobel.consultar_compra(compra3)
nobel.inserir_compra(compra3)
nobel.consultar_compra(compra3)

print("\nLivros da livraria:\n")
for livro in nobel.listaLivros:
    print(livro.titulo)
nobel.remover_livro(CodigoDaVinci)
MrMercedes = Livro("Mr Mercedes", StephenKing, terror.genero, 2, "Suma", 27, 35, impostoIT.calcular_imposto(terror, 35))
nobel.inserir_livro(MrMercedes)
print("\nLivros da livraria:\n")
for livro in nobel.listaLivros:
    print(livro.titulo)
nobel.consultar_livro(StephenKing)


nobel.remover_cliente(BrunoFranzini)


