class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Cliente(Pessoa):
    def __init__(self, nome, email, comprasPassadas):
        super().__init__(nome, email)
        self.comprasPassadas = comprasPassadas


class Autor(Pessoa):
    def __init__(self, nome, email, obras):
        super().__init__(nome, email)
        self.obras = obras