#-*- coding:utf-8 -*-
from distutils.core import setup
import py2exe

#setup(windows=['Client2.py'])
setup(windows=[{"script":"Client.py"}],
      options={"py2exe":{"includes":["sip"]}},
      data_files=[('.', ['Bezymyanny-2.ico'])])
# консольное приложение с единственной точкой входа - файлом "myprog.py"
# setup(windows=['myprog.py']) # вариант для GUI-приложения

