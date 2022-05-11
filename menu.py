# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
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

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(220, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMinimumSize(QtCore.QSize(220, 300))
        Menu.setMaximumSize(QtCore.QSize(220, 300))
        font = QtGui.QFont()
        font.setItalic(False)
        Menu.setFont(font)
        Menu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Bezymyanny-2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Menu.setWindowIcon(icon)
        Menu.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Send_email = QtWidgets.QPushButton(self.centralwidget)
        self.Send_email.setGeometry(QtCore.QRect(20, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.Send_email.setFont(font)
        self.Send_email.setObjectName(_fromUtf8("Send_email"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 201, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Безымянный-2.bmp")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 211, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("logo1.svg")))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Sign_out = QtWidgets.QPushButton(self.centralwidget)
        self.Sign_out.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.Sign_out.setFont(font)
        self.Sign_out.setObjectName(_fromUtf8("Sign_out"))
        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "OurMail", None))
        self.Send_email.setText(_translate("Menu", "Отправить письмо", None))
        self.Sign_out.setText(_translate("Menu", "Выйти", None))

