from TelaInicial_ui import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys



class TelaInicial(QMainWindow) :
    def __init__(self,parent = None):
        super().__init__(parent)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    telainicial = TelaInicial()
    telainicial.show()
    qt.exec_()
    