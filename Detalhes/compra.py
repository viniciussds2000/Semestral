from tkinter import *
from tkinter import messagebox



class Compra(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+720+200")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        linha1=Frame(self,bg="black")
        linha1.pack(anchor=NW,pady=35)
        linha2=Frame(self,bg="black")
        linha2.pack(anchor=W,pady=29)
        linha3=Frame(self,bg="black")
        linha3.pack(anchor=SW)
        linha4=Frame(self,bg="black")
        linha4.pack(anchor=S,pady=35)
        
        self.head = Label(topframe,text="Finalização da compra",font=("Arial","20","bold"),fg="red2",bg="black")

        self.CPF= Label(linha2,text="CPF: ",bg="black",fg="white",font=("Arial","12","bold"))
        self.CLIENTE= Label(linha2,text="Nome Completo: ",bg="black",fg="white",font=("Arial","12","bold"))

        self.CEP= Label(linha3,text="CEP: ",bg="black",fg="white",font=("Arial","12","bold"))
        self.RG= Label(linha3,text="RG: ",bg="black",fg="white",font=("Arial","12","bold"))

        self.VENDEDOR= Label(linha1,text="Vendedor: ",bg="black",fg="white",font=("Arial","12","bold"))
        self.VALOR= Label(linha1,text="Vendido por: R$",bg="black",fg="white",font=("Arial","12","bold"))



        self.vendedor = Entry(linha1,bg="black",fg="white",width=10,font=("Arial","12"))
        self.valor = Entry(linha1, bg="black", fg="white", width=7, font=("Arial", "12"))

        self.cliente = Entry(linha2,bg="black",fg="white",width=21,font=("Arial","12"))
        self.cpf = Entry(linha2,bg="black",fg="white",width=11,font=("Arial","12"))

        self.cep = Entry(linha3,bg="black",fg="white",width=8,font=("Arial","12"))
        self.rg = Entry(linha3, bg="black", fg="white", width=9, font=("Arial", "12"))

        self.finalizar = Button(linha4,text="Finalizar",width=10,height=3,borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.Finalizar_compra)
        self.voltar = Button(linha4,text="Voltar",width=10,height=3,borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.destroy)





        self.head.pack()

        self.VENDEDOR.pack(side=LEFT)
        self.vendedor.pack(side=LEFT)

        self.VALOR.pack(side=LEFT,padx=15)
        self.valor.pack(side=LEFT)

        self.CLIENTE.pack(side=LEFT)
        self.cliente.pack(side=LEFT)

        self.CPF.pack(side=LEFT,padx=0)
        self.cpf.pack(side=LEFT)

        self.CEP.pack(side=LEFT)
        self.cep.pack(side=LEFT)

        self.RG.pack(side=LEFT,padx=9)
        self.rg.pack(side=LEFT)


        self.finalizar.pack(side=LEFT,padx=20)
        self.voltar.pack(side=LEFT)

        self.vend= self.vendedor.get()

    def get_vendedor(self):
        vendedor = self.vendedor.get()
        return vendedor

    def get_cliente(self):
        cliente = self.cliente.get()
        return cliente

    def get_valor(self):
        valor = self.valor.get()
        return valor

    def get_cpf(self):
        cpf = self.cpf.get()
        return cpf

    def get_cep(self):
        cep = self.cep.get()
        return cep

    def get_rg(self):
        rg = self.rg.get()
        return rg


    '''
        cliente = self.cliente.get()
        cpf = self.cpf.get()
        rg = self.cep.get()
        cep = self.cep.get()
        valor = self.valor.get()'''



    def Finalizar_compra(self):
        print("foi")

        messagebox.showinfo("Nota_Fiscal", "COMPRA FINALIZADA!!\n"
                                           ""
                                           "Vendido por: "+Compra.get_vendedor(self)+"\n"
                                            "\n"
                                            "Comprado por: "+Compra.get_cliente(self)+"\n"
                                            "CPF: "+Compra.get_cpf(self)+"\n"
                                            "RG: "+Compra.get_rg(self)+"\n"
                                            "CEP: "+Compra.get_cep(self)+"\n"
                                            "Pelo o valor de : R$"+Compra.get_valor(self)+"\n"
                                            "\n"
                                            "Obrigado pela a preferencia! Volte TINOVO!")







        '''class Nota_fiscal()
        def __init__(self, parent):
            super().__init__(parent)
            self.geometry("500x400+520+200")
            self.title("Notafiscal")
            self["bg"] = "black"

            topframe=Frame(self)
            topframe.pack()
            bottonframe=Frame(self,bg="black")
            bottonframe.pack()


            self.head = Label(topframe,text=,font=("Arial","20","bold"),fg="red2",bg="black")
            self.head.pack()'''



