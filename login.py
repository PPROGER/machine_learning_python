#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore





class Qlogin(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 350, 600)
        self.setWindowTitle('Login')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(350,600)
        #Картинка User
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/user.png')
        label_image.setPixmap(pixmap)
        label_image.setGeometry(110,50,128,128)



        #Поля ввода
        login = QtGui.QLabel(self)
        pixmap1 = QtGui.QPixmap('image/login.png')
        login.setPixmap(pixmap1)
        login.setGeometry(20,200,64,64)

        self.loginEdit = QtGui.QLineEdit(self)
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.loginEdit.setGeometry(80,222,240,30)

        password = QtGui.QLabel(self)
        pixmap2 = QtGui.QPixmap('image/password.png')
        password.setPixmap(pixmap2)
        password.setGeometry(20,300,64,64)

        self.passwordEdit = QtGui.QLineEdit(self)
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray;}")
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.passwordEdit.setGeometry(80,322,240,30)
        
        #Кнопка входа
        self.log_button = QtGui.QPushButton('Login', self)
        self.log_button.setStyleSheet("QPushButton {background:#088A08}")
        self.log_button.setGeometry(170,420,160,50)

        
        label_registration = QtGui.QLabel("Registration",self)
        label_registration.setStyleSheet("QLabel {color:#00FF00; font: 16px;}")
        label_registration.setGeometry(20,525,100,30)


        label_vostanovlenie = QtGui.QLabel("Forgot your password?",self)
        label_vostanovlenie.setStyleSheet("QLabel {color:#00FF00; font: 16px;}")
        label_vostanovlenie.setGeometry(170,525,200,30)


       




 
