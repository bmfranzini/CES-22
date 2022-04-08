class Objeto(object):
    def __init__(self, text):
        print(text)


class Fruta(Objeto):
    def __init__(self, text):
        super().__init__(text)
        print("classe fruta chamada")


class Vermelho(Objeto):
    def __init__(self, text):
        super().__init__(text)
        print("classe vermelho chamada")


class Maca(Fruta, Vermelho):
    def __init(self, text):
        super().__init__(text)


maca = Maca("Essa fruta eh uma maça")