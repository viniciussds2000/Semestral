from patio import Patio
from Detalhes.detalhes import Detalhes

class Controle():
    def __init__(self):

        self.janela=Patio(self)
        self.janela.mainloop()

    def open_detalhes(self):
        Detalhes(self)

    #def nota_fiscal(self):

