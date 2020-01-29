#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore




class QRecovery(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 400,600)
        self.setWindowTitle('Account recovery')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(400,600)


        #Картинка registration
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/recovery.png')
        label_image.setPixmap(pixmap)
        label_image.setGeometry(85,0,256,256)


        firstname_label = QtGui.QLabel("Firstname",self)
        main_label = QtGui.QLabel("Gmail",self)
        password_label = QtGui.QLabel("New Password",self)
        

        firstname_label.setStyleSheet("QLabel {font: 20px;}")
        main_label.setStyleSheet("QLabel {font: 20px;}")
        password_label.setStyleSheet("QLabel {font: 20px;}")


        firstname_label.setGeometry(30,266,90,50)
        main_label.setGeometry(30,316,60,50)
        password_label.setGeometry(30,366,140,50)


       
        firstnameEdit = QtGui.QLineEdit(self)
        mailEdit = QtGui.QLineEdit(self)
        passwordEdit = QtGui.QLineEdit(self)

        firstnameEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        mailEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")

    
        firstnameEdit.setGeometry(170,278,220,30)
        mailEdit.setGeometry(170,328,220,30)
        passwordEdit.setGeometry(170,378,220,30)


        
        
        #Кнопка востановления
        registration_button = QtGui.QPushButton('Recovery', self)
        registration_button.setStyleSheet("QPushButton {background:#088A08}")
        registration_button.setGeometry(230,500,150,50)

        
        

    


app = QtGui.QApplication(sys.argv)
qb = QRecovery()

qb.show()
sys.exit(app.exec_())