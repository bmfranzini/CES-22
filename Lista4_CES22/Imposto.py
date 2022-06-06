class Imposto:
    def __init__(self):
        self.valor = 0

    def calcular_imposto(self, genero, precoVenda):
        if genero.genero == "terror":
            self.valor = 0.1 * precoVenda
        elif genero.genero == "policial":
            self.valor = 0.12 * precoVenda
        elif genero.genero == "romance":
            self.valor = 0.15 * precoVenda
        elif genero.genero == "infantil":
            self.valor = 0.08 * precoVenda

