from Saldos import Saldo
from tkinter import *


class SisMus:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.saldo = Label(self.container1, text="* Conta Pessoal *")
        self.saldo["font"] = ("Calibri", "9", "bold")
        self.saldo.pack()

        self.lblcd_conta = Label(self.container2, text="Código Cliente:", font=self.fonte, width=15)
        self.lblcd_conta.pack(side=LEFT)

        self.txtcd_conta = Entry(self.container2)
        self.txtcd_conta["width"] = 10
        self.txtcd_conta["font"] = self.fonte
        self.txtcd_conta.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMusica
        self.btnBuscar.pack(side=RIGHT)

        self.lblsaldo = Label(self.container3, text="Saldo:", font=self.fonte, width=10)
        self.lblsaldo.pack(side=LEFT)

        self.txtsaldo = Entry(self.container3)
        self.txtsaldo["width"] = 25
        self.txtsaldo["font"] = self.fonte
        self.txtsaldo.pack(side=LEFT)

        self.lblnome = Label(self.container4, text="Nome: ", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblcpf = Label(self.container5, text="CPF:", font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container5)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)


        self.btnInsert = Button(self.container8, text="Depositar", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirMusica
        self.btnInsert.pack(side=LEFT)

        self.btnTransferir = Button(self.container8, text="Transferir", font=self.fonte, width=12)
        self.btnTransferir["command"] = self.alterarMusica
        self.btnTransferir.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir Conta", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirMusica
        self.btnExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text=" ")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirMusica(self):
        music = Saldo()

        music.saldo = self.txtsaldo.get()
        music.nome = self.txtnome.get()
        music.cpf = self.txtcpf.get()

        self.lblmsg["text"] = music.insertMusic()

        self.txtcd_conta.delete(0, END)
        self.txtsaldo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)


    def alterarMusica(self):
        music = Saldo()

        music.cd_conta = self.txtcd_conta.get()
        music.saldo = self.txtsaldo.get()
        music.nome = self.txtnome.get()
        music.cpf = self.txtcpf.get()

        self.lblmsg["text"] = music.updateMusic()

        self.txtcd_conta.delete(0, END)
        self.txtsaldo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

    def excluirMusica(self):
        music = Saldo()

        music.cd_conta = self.txtcd_conta.get()

        self.lblmsg["text"] = music.deleteMusic()

        self.txtcd_conta.delete(0, END)
        self.txtsaldo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

    def buscarMusica(self):
        music = Saldo()

        cd_conta = self.txtcd_conta.get()

        self.lblmsg["text"] = music.selectMusic(cd_conta)

        self.txtcd_conta.delete(0, END)
        self.txtcd_conta.insert(INSERT, music.cd_conta)

        self.txtsaldo.delete(0, END)
        self.txtsaldo.insert(INSERT, music.saldo)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, music.nome)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, music.cpf)


root = Tk()
SisMus(root)
root.mainloop()