# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendletter.ui'
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

class Ui_Send_Letter(object):
    def setupUi(self, Send_Letter):
        Send_Letter.setObjectName(_fromUtf8("Send_Letter"))
        Send_Letter.setWindowModality(QtCore.Qt.NonModal)
        Send_Letter.setEnabled(True)
        Send_Letter.resize(612, 565)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Send_Letter.sizePolicy().hasHeightForWidth())
        Send_Letter.setSizePolicy(sizePolicy)
        Send_Letter.setMinimumSize(QtCore.QSize(612, 565))
        Send_Letter.setMaximumSize(QtCore.QSize(612, 565))
        font = QtGui.QFont()
        font.setItalic(False)
        Send_Letter.setFont(font)
        Send_Letter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Bezymyanny-2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Send_Letter.setWindowIcon(icon)
        Send_Letter.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Send_Letter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.user_to = QtWidgets.QLineEdit(self.centralwidget)
        self.user_to.setGeometry(QtCore.QRect(60, 80, 541, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        font.setPointSize(11)
        self.user_to.setFont(font)
        self.user_to.setText(_fromUtf8(""))
        self.user_to.setObjectName(_fromUtf8("user_to"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 51, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.subject_line = QtWidgets.QLineEdit(self.centralwidget)
        self.subject_line.setGeometry(QtCore.QRect(60, 110, 541, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        font.setPointSize(11)
        self.subject_line.setFont(font)
        self.subject_line.setText(_fromUtf8(""))
        self.subject_line.setObjectName(_fromUtf8("subject_line"))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 150, 541, 351))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 141, 51))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("logo1.svg")))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        Send_Letter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Send_Letter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Send_Letter.setStatusBar(self.statusbar)

        self.retranslateUi(Send_Letter)
        QtCore.QMetaObject.connectSlotsByName(Send_Letter)

    def retranslateUi(self, Send_Letter):
        Send_Letter.setWindowTitle(_translate("Send_Letter", "OurMail", None))
        self.pushButton.setText(_translate("Send_Letter", "Меню", None))
        self.pushButton_2.setText(_translate("Send_Letter", "Отправить", None))
        self.user_to.setToolTip(_translate("Send_Letter", "<html><head/><body><p>введите адресс почты пользователя, которому вы хотите отправить сообщение</p></body></html>", None))
        self.user_to.setWhatsThis(_translate("Send_Letter", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("Send_Letter", "Заполните все формы для отправки сообщения", None))
        self.label_2.setText(_translate("Send_Letter", "Кому:", None))
        self.label_3.setText(_translate("Send_Letter", "Тема:", None))
        self.subject_line.setToolTip(_translate("Send_Letter", "<html><head/><body><p>тема вашего письма</p></body></html>", None))
        self.subject_line.setWhatsThis(_translate("Send_Letter", "<html><head/><body><p><br/></p></body></html>", None))

