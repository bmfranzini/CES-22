#importando módulo do SQLite
import sqlite3


class Banco():


    def __init__(self):
        self.conexao = sqlite3.connect('saldo.db')
        self.createTable()


    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists saldos(
                     cd_conta integer primary key autoincrement,
                     saldo text, 
                     nome text,
                     cpf text)""")
        self.conexao.commit()
        c.close()
