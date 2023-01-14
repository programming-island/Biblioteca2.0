from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from TelaInicial_ui import *
from TelaBuscarLivros_ui import *


class BuscarLivros(QMainWindow,Ui_pesquisalivros) :
    def __init__(self,parent = None):
        super().__init__(parent)
        super().setupUi(self)


class TelaInicial(QMainWindow,Ui_TelaPrinciapal) :
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_TelaPrinciapal()
        self.ui.setupUi(self)
        self.ui.btnpesquisar.clicked.connect(self.entrar_telaBusacarLivros)
        
    def entrar_telaBusacarLivros(self):
        self.tela=BuscarLivros()
        self.tela.show()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    telainicial = TelaInicial()
    telainicial.show()
    qt.exec_()
    


    