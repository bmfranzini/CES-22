class Produto:
    def __init__(self, tipo):
        self.tipo = tipo


class Livro(Produto):
    def __init__(self, titulo, autor, genero, edicao, editora, precoCompra, precoVenda, imposto):
        super().__init__("livro")
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.editora = editora
        self.precoCompra = precoCompra
        self.precoVenda = precoVenda
        self.imposto = imposto




