import Produto
import Pessoa


class Livraria:
    def __init__(self, listaLivros, listaAutores, ordensCompra, nome):
        self.listaLivros = listaLivros
        self.listaClientes = []
        self.listaAutores = listaAutores
        self.ordensCompra = ordensCompra
        self.nome = nome

    def inserir_livro(self, livro):
        self.listaLivros.append(livro)
        print("\nLivro", livro.titulo, "inserido da livraria\n")

    def remover_livro(self, livro):
        self.listaLivros.remove(livro)
        print("\nLivro", livro.titulo, "removido da livraria\n")

    def consultar_livro(self, autor):
        print("\nAutor consultado:", autor.nome)
        for livro in autor.obras:
            if livro not in self.listaLivros:
                print("\tA livraria", self.nome, "possui o livro", livro)
            else:
                print("\tA livraria", self.nome, "nao possui o livro", livro)

    def alterar_livro(self, livro, itemAlterado, novoValor):
        if itemAlterado == "genero":
            livro.genero = novoValor
        elif itemAlterado == "titulo":
            livro.titulo = novoValor
        elif itemAlterado == "precoCompra":
            livro.precoCompra = novoValor
        elif itemAlterado == "precoVenda":
            livro.precoVenda = novoValor
        elif itemAlterado == "autor":
            livro.autor = novoValor
        elif itemAlterado == "edicao":
            livro.edicao = novoValor
        elif itemAlterado == "editora":
            livro.editora = novoValor

    def inserir_cliente(self, cliente):
        self.listaClientes.append(cliente)
        print("\nCliente", cliente.nome, "inserido na base de dados da livraria", self.nome, "!")

    def remover_cliente(self, cliente):
        self.listaClientes.remove(cliente)
        print("\nCliente", cliente.nome, "removido da base de dados da livraria", self.nome, "!")

    def consultar_cliente(self, cliente):
        if cliente not in self.listaClientes:
            print("Cliente não cadastrado\n")
        else:
            print("Nome: ", cliente.nome)
            print("Email: ", cliente.email)
            print("Compras feitas: \n")
            for compra in cliente.comprasPassadas:
                print("\tCompra de indice", compra.ordemCompra)
                for item, quant in zip(compra.listaItens, compra.listaQuantidades):
                    print("\tItem: ", item.titulo, ",", quant, "volume(s)")
                print("\t\tValor da compra:", compra.valorCompra, "reais")

    def alterar_cliente(self, cliente, itemAlterado, novoValor):
        if itemAlterado == "nome":
            cliente.nome = novoValor
        elif itemAlterado == "email":
            cliente.email = novoValor
        print("\nAlteracao feita no", itemAlterado, "do cliente", cliente.nome, "para", novoValor)


    def inserir_compra(self, compra):
        self.ordensCompra.append(compra.ordemCompra)

    def remover_compra(self, compra):
        self.ordensCompra.remove(compra.ordemCompra)

    def consultar_compra(self, compra):
        if compra.ordemCompra not in self.ordensCompra:
            print("\nCompra de indice", compra.ordemCompra, "não existente")
        else:
            print("\nEssa compra existe e tem indice", compra.ordemCompra)
            for item, quant in zip(compra.listaItens, compra.listaQuantidades):
                print("\tItem comprado: ", item.titulo, ",", quant, "volume(s)")

    def alterar_compra(self, compra, itemAlterado, index, novoValor):
        if itemAlterado == "listaItens":
            compra.listaItens[index] = novoValor
        elif itemAlterado == "listaQuantidades":
            compra.listaQuantidades[index] = novoValor
        elif itemAlterado == "valorCompra":
            compra.valorCompra = novoValor
        elif itemAlterado == "ordemCompra":
            compra.ordemCompra = novoValor


