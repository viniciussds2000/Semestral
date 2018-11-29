from tkinter import *
from Detalhes.detalhes import *

'''from Detalhes.detalhes2 import Detalhes2
from Detalhes.detalhes3 import Detalhes3
from Detalhes.detalhes4 import Detalhes4
from Detalhes.detalhes5 import Detalhes5
from Detalhes.detalhes6 import Detalhes6
from Detalhes.detalhes7 import Detalhes7
from Detalhes.detalhes8 import Detalhes8
from Detalhes.detalhes9 import Detalhes9
'''
class Patio(Tk):
    def __init__(self,controle):
        super().__init__()

        modelo=""
        print ("Abrir tela principal")
        self.controle=controle
        self["bg"] = "black"
        self.title("Concessionaria TINOVO ")
        self.geometry("450x500+50+200")
        self.headfont = ("Arial", "30", "bold")

        self.head = Label(text="TINOVO", font=self.headfont, bg="black", fg="red2")
        self.bd = Label(text=("Como posso-lhe ajudar?"), font=("Arial", "16", "bold"), fg="white", bg="black")

        # Buttons
        self.bt = Button(width=8, height=3, text="Uno", command=self.btn1_detalhes, borderwidth=5, bg="red2",
                         fg="white", font=("Arial", "13", "bold"))
        self.bt2 = Button(width=8, height=3, text="Hilux", command=self.btn2_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt3 = Button(width=8, height=3, text="UP", command=self.btn3_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt4 = Button(width=8, height=3, text="Ford Ka", command=self.btn4_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt5 = Button(width=8, height=3, text="Corsa", command=self.btn5_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt6 = Button(width=8, height=3, text="Civic", command=self.btn6_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt7 = Button(width=8, height=3, text="Palio", command=self.btn7_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt8 = Button(width=8, height=3, text="March", command=self.btn8_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        self.bt9 = Button(width=8, height=3, text="New QQ", command=self.btn9_detalhes, borderwidth=5, bg="red2",
                          fg="white", font=("Arial", "13", "bold"))
        #
        self.bd.grid(row=1, column=0, pady=5, columnspan=3)
        self.head.grid(row=0, column=1, pady=2)

        # Grid
        self.bt.grid(row=3, column=0, padx=25, pady=25)
        self.bt2.grid(row=3, column=1, padx=25, pady=10)
        self.bt3.grid(row=3, column=2, padx=25, pady=10)
        self.bt4.grid(row=4, column=0, padx=1, pady=25)
        self.bt5.grid(row=4, column=1, padx=1, pady=10)
        self.bt6.grid(row=4, column=2, padx=1, pady=10)
        self.bt7.grid(row=5, column=0, padx=1, pady=25)
        self.bt8.grid(row=5, column=1, padx=1, pady=10)
        self.bt9.grid(row=5, column=2, padx=1, pady=10)


    def btn_venda(self):
        print('test')


    def btn1_detalhes(self):

        Detalhes(self)


    def btn2_detalhes(self):
        Detalhes2(self)

    def btn3_detalhes(self):
        Detalhes3(self)

    def btn4_detalhes(self):
        Detalhes4(self)

    def btn5_detalhes(self):
        Detalhes5(self)

    def btn6_detalhes(self):
        Detalhes6(self)

    def btn7_detalhes(self):
        Detalhes7(self)

    def btn8_detalhes(self):
        Detalhes8(self)

    def btn9_detalhes(self):
        Detalhes9(self)

