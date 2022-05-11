# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui,QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Reg(object):
    def setupUi(self, Reg):
        Reg.setObjectName(_fromUtf8("Reg"))
        Reg.resize(220, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Reg.sizePolicy().hasHeightForWidth())
        Reg.setSizePolicy(sizePolicy)
        Reg.setMinimumSize(QtCore.QSize(220, 300))
        Reg.setMaximumSize(QtCore.QSize(220, 300))
        font = QtGui.QFont()
        font.setItalic(False)
        Reg.setFont(font)
        Reg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Bezymyanny-2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Reg.setWindowIcon(icon)
        Reg.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Reg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 110, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 240, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 211, 71))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("logo1.svg")))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        Reg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Reg.setStatusBar(self.statusbar)

        self.retranslateUi(Reg)
        QtCore.QMetaObject.connectSlotsByName(Reg)

    def retranslateUi(self, Reg):
        Reg.setWindowTitle(_translate("Reg", "OurMail", None))
        self.pushButton_2.setText(_translate("Reg", "Зарегестрироваться", None))
        self.lineEdit.setToolTip(_translate("Reg", "<html><head/><body><p><span style=\" font-family:\'Courier New,courier\';\">Придумайте адрес электронной почты (email)</span></p></body></html>", None))
        self.lineEdit.setText(_translate("Reg", "адрес электронной почты", None))
        self.lineEdit_2.setToolTip(_translate("Reg", "<html><head/><body><p><span style=\" font-family:\'Courier New,courier\';\">Придумайте пароль для своей почты</span></p></body></html>", None))
        self.lineEdit_2.setText(_translate("Reg", "пароль", None))
        self.label.setText(_translate("Reg", "Зарегестрируйтесь", None))
        self.lineEdit_3.setToolTip(_translate("Reg", "<html><head/><body><p>Придумайте логин для вашей учетной записи</p></body></html>", None))
        self.lineEdit_3.setText(_translate("Reg", "логин", None))
        self.pushButton_3.setText(_translate("Reg", "Отмена", None))

