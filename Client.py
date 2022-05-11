# -*- coding:utf-8 -*-
import sys, math, os, pickle
from socket import *
from PyQt5 import QtCore, QtGui,QtWidgets
# pyuic4.bat reg.ui o project1.py #заупуск скрипта преобразующего ui в py
from project1 import Ui_Reg
from project import Ui_Sign_in
from menu import Ui_Menu
from SendLetter import Ui_Send_Letter
from PyQt5.QtWidgets import QApplication,QLabel, QLineEdit
#from PyQt5.QtGui import  QLabel, QLineEdit


class Start_Client(QtWidgets.QMainWindow):
    # класс Start_Client наследует класс QMainWindow находящицся в QtGui
    def __init__(self, parent=None):  # __init__- метод иницализации(присваивает начальные значения атрибутам класса)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Sign_in()  # интерфейс пользователя управляется из основного окна
        self.child = Ui_Reg()  # child, ui, menu, send - это экземпляры класса
        self.menu = Ui_Menu()  # self - ссылка на атрибут экземпляра класса
        self.send = Ui_Send_Letter()
        self.ui.setupUi(self)  # компоновка гафического интерфейса
        self.Sign_in_connectSlots()  # подключаем кнопки окна входа в систему 
        self.serverHost = 'localhost'  # '192.168.1.2'# задаем хост сервера
        
        self.serverPort = 50087  # задаем порт сервера
    # Открытие окна входа в учетную запись пользователя
    def Open_Sign_in(self):
        self.ui.setupUi(self)
        self.Sign_in_connectSlots()
    # Установка обработчиков сигналов на кнопки в окне входа в учетную запись
    def Sign_in_connectSlots(self):  # Устанавливаем обработчики сингналов на кнопки

        #self.connect(origin, SIGNAL('completed'), self._show_results)
        #origin.completed.connect(self._show_results)
        self.ui.pushButton.clicked.connect(self.Open_Reg)
        #self.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.Open_Reg)
        self.ui.pushButton_2.clicked.connect(self.Sign_in_slotAddClicked)
        #self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.Sign_in_slotAddClicked)
        self.ui.lineEdit_2.setEchoMode(2)  # режим ввода - звездочки вместо символов
    # Считывание данных из форм окна входа в учетную запись принажатии кнопки "Вход" 
    def Sign_in_slotAddClicked(self):
        self.email = self.ui.lineEdit.text()  # считываем данные из полей ввода адреса почты и пароля
        self.password =( self.ui.lineEdit_2.text())
        self.Send_Sign_in()        
    # Отправка указанных при входе данных на сервер
    def Send_Sign_in (self):
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.serverHost, self.serverPort))
        message = ['1', self.email, self.password]
        byte_message = pickle.dumps(message)  # преобразование символов в байты
        sockobj.send(byte_message)  # через сокет передаются только байты
        byte_data = sockobj.recv(1024)  # прием ответа с сервера 
        print ('byte data=', byte_data)
        data = pickle.loads(byte_data)  # реобразование байтов в символы
        print ('data=', data)
        if data == 'True':
            self.Open_Menu()  # открываем меню, если пользователь найден в бд
        else:
            msgBox = QtWidgets.QMessageBox()  # выводим окно с ошибкой, если такого пользователя нет в бд
            msgBox.setWindowTitle(u'Ошибка!')
            msgBox.setText(u"Введен неверный email или пароль. Пожалйста, повторите ввод.")
            msgBox.exec_()
        sockobj.close()  # закрываем соединение с сервером   
    #функция открывающая окно регистрации
    def Open_Reg(self):
        self.child.setupUi(self)
        self.Reg_connectSlots()
    # открытие отправки сообщения
    def Open_Send_Letter(self):
        self.send.setupUi(self)
        self.Send_Letter_connectSlots()
    # подключение кнопок окна отправки сообщения
    def Send_Letter_connectSlots(self):
        self.send.pushButton_2.clicked.connect(self.Send_Letter_slotAddClicked)
        #self.connect(self.send.pushButton_2,QtCore.SIGNAL("clicked()"),self.Send_Letter_slotAddClicked)
        self.send.pushButton.clicked.connect(self.Open_Menu)
        #self.connect(self.send.pushButton,QtCore.SIGNAL("clicked()"),self.Open_Menu)
    # действие при нажатие на кнопку "отправить" 
    def Send_Letter_slotAddClicked (self):# считываем данные из форм окна(кому, тема, текст сообщения)
        self.user_to =self.send.user_to.text()
        self.subject = self.send.subject_line.text()
        self.text = self.send.textEdit.toPlainText()
        self.Send_Send_Letter()
        self.Open_Menu()
    # отправка сообщения на сервер    
    def Send_Send_Letter (self):
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.serverHost, self.serverPort))# подключаемся по ранее указанному хосту и порту
        message = ['3',self.user_to,self.subject, self.text, self.email]# компануем сообщение, которое будем отправлять на сервер
        print (self.email)
        byte_message = pickle.dumps(message)# преобразуем символы в байты (в данном случае мы хотим передать не строку, а список,
        #причем сохранив его структуру. поэтому мы переводим его в биты при помощи pickle и получив сообщение на сервере преобразуем его обратно)
        sockobj.send(byte_message)# отправляем сообщение на сервер (через сокеты можно передовать только байты)
        byte_data = sockobj.recv(1024)# принимаем ответ от сервера
        print ('byte data=', byte_data)
        data = pickle.loads(byte_data)# преобразуем ответ из байтов в строку
        print ('data=', data.encode('utf8'))#
        if data == 'True':# если ответ положительный, то выводим окно с сообщением о успешной отправке
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle(u'Письмо отправлено')
            msgBox.setText(u"Письмо успешно отправлено")
            msgBox.exec_()
        else:# иначе выводим окно с ошибкой
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle(u'Ошибка!')
            msgBox.setText(u"Ошибка при отправке письма")
            msgBox.exec_()
        sockobj.close()
    #функция устанавливающая обработчики сигналов на кнопки
    def Reg_connectSlots(self):
        self.child.pushButton_2.clicked.connect(self.Reg_slotAddClicked)
        #self.connect(self.child.pushButton_2,QtCore.SIGNAL("clicked()"),self.Reg_slotAddClicked)
        self.child.pushButton_3.clicked.connect(self.Open_Sign_in)
        #self.connect(self.child.pushButton_3,QtCore.SIGNAL("clicked()"),self.Open_Sign_in)
        self.child.lineEdit_2.setEchoMode(3)
    def Reg_slotAddClicked(self):
        self.login = self.child.lineEdit_3.text()
        self.email =self.child.lineEdit.text()
        self.password = self.child.lineEdit_2.text()
        self.Send_reg()
    # Отправка указанных при регистрации данных на сервер
    def Send_reg (self):
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.serverHost, self.serverPort))
        message = ['2',self.login,self.email,self.password]
        byte_message = pickle.dumps(message)
        sockobj.send(byte_message)
        byte_data = sockobj.recv(1024)
        print ('byte data=', byte_data)
        data = pickle.loads(byte_data)
        print('Client recieved:', data)   
        if data == 'False':
            self.Open_Sign_in()
        else:
            if data == 'weal':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle(u'Ошибка!')
                msgBox.setText(u"Пользователь с таким логином и почтой уже существует.")
                msgBox.exec_()
            if data == 'we':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle(u'Ошибка!')
                msgBox.setText(u"Пользователь с таким адресом электронной почты уже существет.")
                msgBox.exec_()
            if data == 'wl':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle(u'Ошибка!')
                msgBox.setText(u"Пользователь с таким логином уже существует.")
                msgBox.exec_()
        sockobj.close()
    # Открытие основного меню
    def Open_Menu(self):
        self.menu.setupUi(self)
        self.Menu_connectSlots()
    # Установка обработчиков сигналов на кнопки в окне главного меню
    def Menu_connectSlots(self):# Устанавливаем обработчики сингналов на кнопки
        
        self.menu.Sign_out.clicked.connect(self.Open_Sign_in)
        #self.connect(self.menu.Sign_out,QtCore.SIGNAL("clicked()"),self.Open_Sign_in)
        self.menu.Send_email.clicked.connect(self.Open_Send_Letter)
        #self.connect(self.menu.Send_email,QtCore.SIGNAL("clicked()"),self.Open_Send_Letter)
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   myapp = Start_Client()
   pal = myapp.palette()
   pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#B0E2FF"))  # настройка фона окна
   myapp.setPalette(pal)
   myapp.show()
   try:
      sys.exit(app.exec_())
   except SystemExit:
      pass

    



