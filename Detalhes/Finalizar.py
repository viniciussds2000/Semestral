from tkinter import *

class Nota_fiscal(Toplevel):
    def __init__(self, parent, ):
        super().__init__(parent)
        self.geometry("500x400+520+200")
        self.title("Notafiscal")
        self["bg"] = "black"

        topframe = Frame(self)
        topframe.pack()
        bottonframe = Frame(self, bg="black")
        bottonframe.pack()

        self.head = Label(topframe, text="Detalhes do veiculo", font=("Arial", "20", "bold"), fg="red2", bg="black")
        self.head.pack()