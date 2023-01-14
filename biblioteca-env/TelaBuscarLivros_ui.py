# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaBuscaLivros.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pesquisalivros(object):
    def setupUi(self, pesquisalivros):
        pesquisalivros.setObjectName("pesquisalivros")
        pesquisalivros.resize(387, 338)
        pesquisalivros.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(pesquisalivros)
        self.centralwidget.setObjectName("centralwidget")
        self.tblBuscalivros = QtWidgets.QTableWidget(self.centralwidget)
        self.tblBuscalivros.setGeometry(QtCore.QRect(0, 140, 391, 201))
        self.tblBuscalivros.setStyleSheet("background-color: rgb(225, 254, 255);")
        self.tblBuscalivros.setObjectName("tblBuscalivros")
        self.tblBuscalivros.setColumnCount(4)
        self.tblBuscalivros.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuscalivros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuscalivros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuscalivros.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuscalivros.setHorizontalHeaderItem(3, item)
        self.btnBuscarLivros = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarLivros.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.btnBuscarLivros.setStyleSheet("background-color: rgb(255, 255, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/arquivo-de-documento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarLivros.setIcon(icon)
        self.btnBuscarLivros.setObjectName("btnBuscarLivros")
        self.edtcodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.edtcodigo.setGeometry(QtCore.QRect(10, 60, 41, 20))
        self.edtcodigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtcodigo.setObjectName("edtcodigo")
        self.edtlivro = QtWidgets.QLineEdit(self.centralwidget)
        self.edtlivro.setGeometry(QtCore.QRect(60, 60, 121, 20))
        self.edtlivro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtlivro.setObjectName("edtlivro")
        self.edtautor = QtWidgets.QLineEdit(self.centralwidget)
        self.edtautor.setGeometry(QtCore.QRect(190, 60, 101, 20))
        self.edtautor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtautor.setObjectName("edtautor")
        pesquisalivros.setCentralWidget(self.centralwidget)

        self.retranslateUi(pesquisalivros)
        QtCore.QMetaObject.connectSlotsByName(pesquisalivros)

    def retranslateUi(self, pesquisalivros):
        _translate = QtCore.QCoreApplication.translate
        pesquisalivros.setWindowTitle(_translate("pesquisalivros", "Pesquisar Livros"))
        item = self.tblBuscalivros.horizontalHeaderItem(0)
        item.setText(_translate("pesquisalivros", "Código"))
        item = self.tblBuscalivros.horizontalHeaderItem(1)
        item.setText(_translate("pesquisalivros", "Livro"))
        item = self.tblBuscalivros.horizontalHeaderItem(2)
        item.setText(_translate("pesquisalivros", "Autor"))
        item = self.tblBuscalivros.horizontalHeaderItem(3)
        item.setText(_translate("pesquisalivros", "Preço"))
        self.btnBuscarLivros.setText(_translate("pesquisalivros", "Pesquisar"))
