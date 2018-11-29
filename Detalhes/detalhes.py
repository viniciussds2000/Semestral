from tkinter import *
from Detalhes.compra import Compra


class Detalhes(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: Uno Vivace ",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: FIAT ", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2016", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado(39.000 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Preto  ", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Hatch", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 1.0 ", font=("Arial", "11"))
        self.info8 = Label(bottonframe,bg="black",fg="white", text="Combustivel: Gasolina e álcool ", font=("Arial", "11"))
        self.info9 = Label(bottonframe,bg="black",fg="white", text="Trasmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe,bg="black",fg="white", text="Valor no mercado: 33.600", font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 27.190 ", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar= Button(bottonframe,width=10,height=2,text="Voltar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20,padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20,padx=10)


    def btn_comprei(self):
        Compra(self)
        

    

class Detalhes2(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: Hilux Cab. Dupla",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: Toyota", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2016 ", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado (45.000 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Preto", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Pick-up", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 2.8", font=("Arial", "11"))
        self.info8 = Label(bottonframe,bg="black",fg="white", text="Combustivel: Diesel ", font=("Arial", "11"))
        self.info9 = Label(bottonframe,bg="black",fg="white", text="Transmissão: Manual, 6 velocidades", font=("Arial", "11"))
        self.info10 = Label(bottonframe,bg="black",fg="white", text="Valor no mercado: 160.456 ", font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 144.900 ", font=("Arial", "11"))


        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)




class Detalhes3(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"] = "black"

        topframe = Frame(self)
        topframe.pack()
        bottonframe = Frame(self, bg="black")
        bottonframe.pack()

        self.head = Label(topframe, text="Detalhes do veiculo", font=("Arial", "20", "bold"), fg="red2", bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe, bg="black", fg="white", text="Modelo: Up! MPI FLEX", font=("Arial", "11"))
        self.info2 = Label(bottonframe, bg="black", fg="white", text="Marca: Volkswagen", font=("Arial", "11"))
        self.info3 = Label(bottonframe, bg="black", fg="white", text="Ano: 2015", font=("Arial", "11"))
        self.info4 = Label(bottonframe, bg="black", fg="white", text="Estado: Usado (38.000 km)",
                               font=("Arial", "11"))
        self.info5 = Label(bottonframe, bg="black", fg="white", text="Cor: Preto ", font=("Arial", "11"))
        self.info6 = Label(bottonframe, bg="black", fg="white", text="Tipo: Hatch", font=("Arial", "11"))
        self.info7 = Label(bottonframe, bg="black", fg="white", text="Motor: 1.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe, bg="black", fg="white", text="Combustivel: Gasolina e álcool",
                               font=("Arial", "11"))
        self.info9 = Label(bottonframe, bg="black", fg="white", text="Transmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe, bg="black", fg="white", text="Valor no mercado 30.500 :  ",
                                font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 26.900", font=("Arial", "11"))

        self.btn_comprar = Button(bottonframe, width=10, height=2, text="Comprar", borderwidth=10, bg="red2",
                                      fg="white", font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)


class Detalhes4(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: Ford Ka SE",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: Ford", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2018", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado (29.000 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Branco  ", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Sedan", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 1.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe,bg="black",fg="white", text="Combustivel: Gasolina e álcool ", font=("Arial", "11"))
        self.info9 = Label(bottonframe,bg="black",fg="white", text="Transmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe,bg="black",fg="white", text="Valor no mercado: 48.990 ",font=("Arial", "11"))
        self.info11 = Label(bottonframe,bg="black",fg="white", text="Valor na loja: 41.900", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)

class Detalhes5(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"] = "black"

        topframe = Frame(self)
        topframe.pack()
        bottonframe = Frame(self, bg="black")
        bottonframe.pack()

        self.head = Label(topframe, text="Detalhes do veiculo", font=("Arial", "20", "bold"), fg="red2",
                                  bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe, bg="black", fg="white", text="Modelo: Corsa MPFI MAXX",
                                   font=("Arial", "11"))
        self.info2 = Label(bottonframe, bg="black", fg="white", text="Marca: Chevrolet", font=("Arial", "11"))
        self.info3 = Label(bottonframe, bg="black", fg="white", text="Ano: 2007 ", font=("Arial", "11"))
        self.info4 = Label(bottonframe, bg="black", fg="white", text="Estado: Usado (1 km)",
                                   font=("Arial", "11"))
        self.info5 = Label(bottonframe, bg="black", fg="white", text="Cor: Amarelo ", font=("Arial", "11"))
        self.info6 = Label(bottonframe, bg="black", fg="white", text="Tipo: Hatch", font=("Arial", "11"))
        self.info7 = Label(bottonframe, bg="black", fg="white", text="Motor:1.0 8V", font=("Arial", "11"))
        self.info8 = Label(bottonframe, bg="black", fg="white", text="Combustivel: Gasolina e álcool ",
                                   font=("Arial", "11"))
        self.info9 = Label(bottonframe, bg="black", fg="white", text="Transmissão: Manual ",
                                   font=("Arial", "11"))
        self.info10 = Label(bottonframe, bg="black", fg="white", text="Valor no mercado: Não é mais fabricado ",
                                    font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 16.500 ",
                                    font=("Arial", "11"))

        self.btn_comprar = Button(bottonframe, width=10, height=2, text="Comprar", borderwidth=10, bg="red2",
                                          fg="white", font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)


class Detalhes6(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: Civic Lxr",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: Honda", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2014", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado (93 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Branca ", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Sedan", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 2.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe,bg="black",fg="white", text="Combustivel: Gasolina e álcool", font=("Arial", "11"))
        self.info9 = Label(bottonframe,bg="black",fg="white", text="Transmissão: Automatica", font=("Arial", "11"))
        self.info10 = Label(bottonframe, bg="black", fg="white", text="Valor no mercado: 57.500  ", font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 49.900 ", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)


class Detalhes7(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: Palio MPI FIRE",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: FIAT", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2010", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado (100.500 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Cinza", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Hatch", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 1.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe, bg="black", fg="white", text="Combustivel: Gasolina e álcool ",font=("Arial", "11"))
        self.info9 = Label(bottonframe, bg="black", fg="white", text="Transmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe, bg="black", fg="white", text="Valor no mercado: 18.500 ", font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 15.900 ", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)


class Detalhes8(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: March S",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: Nissan", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2015", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Usado(47.867 km)", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Cinza", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: Hatch", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 1.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe, bg="black", fg="white", text="Combustivel: Gasolina e álcool ", font=("Arial", "11"))
        self.info9 = Label(bottonframe, bg="black", fg="white", text="Transmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe, bg="black", fg="white", text="Valor no mercado: 30.500 ", font=("Arial", "11"))
        self.info11 = Label(bottonframe, bg="black", fg="white", text="Valor na loja: 27.900 ", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)
    def get_valor(self):
        self.valor="27.900"

class Detalhes9(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x400+200+220")
        self.title("Detalhes")
        self["bg"]="black"


        topframe=Frame(self)
        topframe.pack()
        bottonframe=Frame(self,bg="black")
        bottonframe.pack()

        self.head = Label(topframe,text="Detalhes do veiculo",font=("Arial","20","bold"),fg="red2",bg="black")
        self.head.pack()

        self.info1 = Label(bottonframe,bg="black",fg="white", text="Modelo: New Qq Smile",font=("Arial","11"))
        self.info2 = Label(bottonframe,bg="black",fg="white", text="Marca: Cherry", font=("Arial", "11"))
        self.info3 = Label(bottonframe,bg="black",fg="white", text="Ano: 2019", font=("Arial", "11"))
        self.info4 = Label(bottonframe,bg="black",fg="white", text="Estado: Novo", font=("Arial", "11"))
        self.info5 = Label(bottonframe,bg="black",fg="white", text="Cor: Branco ", font=("Arial", "11"))
        self.info6 = Label(bottonframe,bg="black",fg="white", text="Tipo: ", font=("Arial", "11"))
        self.info7 = Label(bottonframe,bg="black",fg="white", text="Motor: 1.0", font=("Arial", "11"))
        self.info8 = Label(bottonframe,bg="black", fg="white", text="Combustivel: Gasolina e álcool ", font=("Arial", "11"))
        self.info9 = Label(bottonframe,bg="black", fg="white", text="Transmissão: Manual ", font=("Arial", "11"))
        self.info10 = Label(bottonframe,bg="black", fg="white", text="Valor no mercado : 30.600 ", font=("Arial", "11"))
        self.info11 = Label(bottonframe,bg="black", fg="white", text="Valor na loja: 24.190 ", font=("Arial", "11"))

        self.btn_comprar= Button(bottonframe,width=10,height=2,text="Comprar",borderwidth=10,bg="red2",fg="white",font=("Arial", "11", "bold"),command=self.btn_comprei)
        self.btn_voltar = Button(bottonframe, width=10, height=2, text="Voltar", borderwidth=10, bg="red2", fg="white",
                                 font=("Arial", "11", "bold"), command=self.destroy)


        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.info4.pack()
        self.info5.pack()
        self.info6.pack()
        self.info7.pack()
        self.info8.pack()
        self.info9.pack()
        self.info10.pack()
        self.info11.pack()

        self.btn_comprar.pack(side=LEFT, pady=20, padx=10)
        self.btn_voltar.pack(side=LEFT, pady=20, padx=10)

    def btn_comprei(self):
        Compra(self)













