# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtWidgets,QtGui

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

class Ui_Sign_in(object):
    def setupUi(self, Sign_in):
        Sign_in.setObjectName(_fromUtf8("Sign_in"))
        Sign_in.resize(220, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sign_in.sizePolicy().hasHeightForWidth())
        Sign_in.setSizePolicy(sizePolicy)
        Sign_in.setMinimumSize(QtCore.QSize(220, 300))
        Sign_in.setMaximumSize(QtCore.QSize(220, 300))
        font = QtGui.QFont()
        font.setItalic(False)
        Sign_in.setFont(font)
        Sign_in.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Bezymyanny-2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Sign_in.setWindowIcon(icon)
        Sign_in.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Sign_in)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 110, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 140, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 201, 51))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Безымянный-2.bmp")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 20, 211, 71))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo1.svg")))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        Sign_in.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Sign_in)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Sign_in.setStatusBar(self.statusbar)

        self.retranslateUi(Sign_in)
        QtCore.QMetaObject.connectSlotsByName(Sign_in)

    def retranslateUi(self, Sign_in):
        Sign_in.setWindowTitle(_translate("Sign_in", "OurMail", None))
        self.pushButton.setText(_translate("Sign_in", "Регистрация", None))
        self.pushButton_2.setText(_translate("Sign_in", "Вход", None))
        self.lineEdit.setToolTip(_translate("Sign_in", "<html><head/><body><p><span style=\" font-family:\'Courier New,courier\';\">Введите адрес электронной почты (email)</span></p></body></html>", None))
        self.lineEdit.setText(_translate("Sign_in", "адрес электронной почты", None))
        self.lineEdit_2.setToolTip(_translate("Sign_in", "<html><head/><body><p>Введите пароль от вашей электронной почты</p></body></html>", None))
        self.lineEdit_2.setText(_translate("Sign_in", "пароль", None))
        self.label.setText(_translate("Sign_in", "Войдите в вашу учетную запись", None))

