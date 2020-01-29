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

        loginEdit = QtGui.QLineEdit(self)
<<<<<<< HEAD
        loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
=======
        loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
>>>>>>> login forms
        loginEdit.setGeometry(80,222,240,30)

        password = QtGui.QLabel(self)
        pixmap2 = QtGui.QPixmap('image/password.png')
        password.setPixmap(pixmap2)
        password.setGeometry(20,300,64,64)

        passwordEdit = QtGui.QLineEdit(self)
<<<<<<< HEAD
        passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray;}")
=======
        passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
>>>>>>> login forms
        passwordEdit.setGeometry(80,322,240,30)
        
        #Кнопка входа
        log_button = QtGui.QPushButton('Login', self)
        #log_button.setStyleSheet("QPushButton {background:#FF4500; color: black}")
        log_button.setGeometry(170,420,160,30)

        
        label_registration = QtGui.QLabel("Registration",self)
        label_registration.setStyleSheet("QLabel {color:#00FF00; font: 16px;}")
        label_registration.setGeometry(20,525,100,30)


        label_vostanovlenie = QtGui.QLabel("Forgot your password?",self)
        label_vostanovlenie.setStyleSheet("QLabel {color:#00FF00; font: 16px;}")
        label_vostanovlenie.setGeometry(170,525,200,30)


       


        
        

        #self.connect(quit, QtCore.SIGNAL('clicked()'),
            #QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = Qlogin()

qb.show()
sys.exit(app.exec_())