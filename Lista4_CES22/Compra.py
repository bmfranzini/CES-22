class Compra:
    def __init__(self, listaItens, listaQuantidades, ordemCompra):
        self.listaItens = listaItens
        self.listaQuantidades = listaQuantidades
        self.ordemCompra = ordemCompra
        self.valorCompra = 0
        self.lista = {}
        self.gerar_lista()

    def gerar_lista(self):
        for item, quant in zip(self.listaItens, self.listaQuantidades):
            self.valorCompra += item.precoVenda * quant
            self.lista[item] = quant