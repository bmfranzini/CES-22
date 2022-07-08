from Banco import Banco


class Saldo(object):


    def __init__(self, cd_conta=0, saldo="", nome="", cpf=""):
        self.info = {}
        self.cd_conta = cd_conta
        self.saldo = saldo
        self.nome = nome
        self.cpf = cpf


    def insertMusic(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into saldos (saldo, nome, cpf) values('" + self.saldo + "', '" +
                      self.nome + "', '" + self.cpf + "' )")

            banco.conexao.commit()
            c.close()

            return "Saldo cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do saldo"


    @property
    def updateMusic(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update saldos set saldo = '" + self.saldo + "', nome = '" + self.nome +
                      "', cpf = '" + self.cpf + "' where cd_conta = " + self.cd_conta + " ")

            banco.conexao.commit()
            c.close()

            return "Saldo atualizado com sucesso"
        except:
            return "Ocorreu um erro na alteração da conta"


    @property
    def deleteMusic(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from saldos where cd_conta = " + self.cd_conta + " ")

            banco.conexao.commit()
            c.close()

            return "Conta excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da conta"


    def selectMusic(self, cd_conta):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from saldos where cd_conta = " + cd_conta + " ")

            for linha in c:
                self.cd_conta = linha[0]
                self.saldo = linha[1]
                self.nome = linha[2]
                self.cpf = linha[3]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da música"