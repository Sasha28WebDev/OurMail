# -*- coding: cp1251 -*-
from socket import *
import sqlite3, sys, pickle, os, datetime


# ����� ������������ � ���� ������    
def Entrance_sign_in (dbname, email, password):
    con = sqlite3.connect(dbname)#�������� ���� ������
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM user")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            if email == row[2]:
                if password == row[3]:
                    return 'True'
                else:
                    return 'False'
    cur.close()#�������� �������-�������
    con.close()#�������� ���� ������

# ����� ���������� ������ ��������� ��� ����������� � ������� ������������ � ���� ������
def Entrance_reg (dbname, login, email):
    con = sqlite3.connect(dbname)#�������� ���� ������
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM user")
        a = 'False'
        while True:
            row = cur.fetchone()
            if row == None:
                break
            if (login == row[1]) and (email == row[2]):
                a = 'weal'#Weal = Wrong email and login
            else:
                if (login == row[1])or(email == row[2]):
                    if login == row[1]:
                        a = 'wl'
                    if email == row[2]:
                        a = 'we'
            if a !='False':
                return a
                break
        if a == 'False':
            return a
    cur.close()#�������� �������-�������
    con.close()#�������� ���� ������ 

# ����� ������ �� ������ ����� � ���� ������
def Entrance (dbname, email):
    con = sqlite3.connect(dbname)#�������� ���� ������
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM user")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            if email == row[2]:
                return row[1]
            else:
                return 'nodefine'
    cur.close()#�������� �������-�������
    con.close()#�������� ���� ������@mail.ru')

# ���������� ������������ � ���� ������
def AddUser (dbname, login, email, password):
    con = sqlite3.connect(dbname)#�������� ���� ������
    cur = con.cursor()#�������� �������-�������
    i = cur.lastrowid
    b = tuple([i,login, email, password])
    sql_b = "INSERT INTO user VALUES (?,?,?,?)"
    try: 
        cur.execute(sql_b, b)#������
    except sqlite3.DatabaseError as err:
        print("Error:",err)
    else:
        print("The request completed successfully")
        con.commit()
    cur.close()#�������� �������-�������
    con.close()#�������� ���� ������
    return

# �������� ���� ������ � �������� �����
def DeleteDB (dbname):
    con = sqlite3.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS user")
        cur.execute("CREATE TABLE user (Id INT, Login TEXT, Email TEXT, Password TEXT)")
    con.close()
 
# �������� ����� � ������ � ���� ������ ���������
def AddToFile (user_from, user_to,  theme, text):
    now_time = datetime.datetime.now() # ������� ���� �� ��������
    c = now_time.strftime("%d.%m.%Y_%I_%M_%p") 
    a = [user_to, theme, text]
    way = os.getcwd()+ '\\' + user_from + '\\'
    data = str(way + theme + '_' + c + '.txt')
    print (data)
    f = open(data,'w')
    f.writelines("%s\n" % i for i in a)
    f.close()

myHost = 'localhost'
myPort = 50087
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(2)
user=dict(login='',email='', password='')
#1-sign_in #2-reg #3-send_letter
while True:
    #name = raw_input('Enter name:')
    #if name == 'stop':
        #break 
    connection, address = sockobj.accept()
    print('Server connected by', address)
    while True:
         
        data = connection.recv(1024)
        if not data: 
            break
        buff = pickle.loads(data)
        print("buff=", buff)
        if buff[0] == '2':
            user_login = buff[1]
            user_email = buff[2]
            user_password = hash(buff[3])
            answer = Entrance_reg("database.db",user_login,user_email)
            if answer == 'False':
                print ("answer=", answer)
                AddUser ("database.db",user_login,user_email,user_password)
                os.mkdir(user_login)
            else:
                print ("answer=", answer)
            byte_answer = pickle.dumps(answer) 
            connection.send(byte_answer)  
        if buff[0] == '1':
            user_email = buff[1]
            user_password = str(hash(buff[2]))
            byte_answer =pickle.dumps(Entrance_sign_in ("database.db",user_email,user_password))
            connection.send(byte_answer)
        if buff[0] == '3':
            user_to = buff[1]
            user_subject = buff[2]
            user_text = buff[3]
            user_email = buff[4]
            user_from = Entrance("database.db",user_email)
            byte_answer = pickle.dumps('True')
            connection.send(byte_answer)
            AddToFile(user_from, user_to, user_subject, user_text)
            print (user_email, user_from)
    connection.close()
                 
       
                
        





