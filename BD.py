#-*- coding:utf-8 -*-
import sys, sqlite3


def OutputDB (dbname):
    con = sqlite3.connect(dbname)#Открытие базы данных
    with con: 
        cur = con.cursor()#Создание обьекта-курсора
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
        for row in rows:
            print (row)

def Entrance_reg (dbname, login, email):
    con = sqlite3.connect(dbname)#Открытие базы данных
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
    cur.close()#Закрытие обЪекта-курсора
    con.close()#Закрытие базы данных 


      

def AddUser (dbname, login, email, password):
    con = sqlite3.connect(dbname)#Открытие базы данных
    cur = con.cursor()#Создание обьекта-курсора
    i = cur.lastrowid
    b = tuple([i,login, email, password])
    sql_b = "INSERT INTO user VALUES (?,?,?,?)"
    try: 
        cur.execute(sql_b, b)#кортеж
    except sqlite3.DatabaseError as err:
        print("Error:",err)
    else:
        print("The request completed successfully")
        con.commit()
    cur.close()#Закрытие обЪекта-курсора
    con.close()#Закрытие базы данных
    return

def DeleteDB (dbname):
    con = sqlite3.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS user")
        cur.execute("CREATE TABLE user (Id INT, Login TEXT, Email TEXT, Password TEXT)")
    con.close()

"""
con = lite.connect('test.db')
 
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
"""
#DeleteDB ("database.db")
#AddUser ("database.db",'lol','lol@lol.ru','pass')
OutputDB ("database.db")
