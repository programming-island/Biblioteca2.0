from TelaInicial_ui import *
import sys
from PyQt5.QtWidgets import QtmainWindow, QApplication


class TelaInicial(QtmainWindow) :
    def __init__(self,parent = None):
        super().__init__(parent)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    telainicial = TelaInicial()
    telainicial.show()
    qt.exec_()
    