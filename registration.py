#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore




class QRegistration(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 400,600)
        self.setWindowTitle('Registration')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(400,600)


        #Картинка registration
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/registration.png')
        label_image.setPixmap(pixmap)
        label_image.setGeometry(85,0,256,256)


        name_label = QtGui.QLabel("Name",self)
        firstname_label = QtGui.QLabel("Firstname",self)
        main_label = QtGui.QLabel("Gmail",self)
        password_label = QtGui.QLabel("Password",self)
        
        name_label.setStyleSheet("QLabel {font: 20px;}")
        firstname_label.setStyleSheet("QLabel {font: 20px;}")
        main_label.setStyleSheet("QLabel {font: 20px;}")
        password_label.setStyleSheet("QLabel {font: 20px;}")


        name_label.setGeometry(30,266,60,50)
        firstname_label.setGeometry(30,316,90,50)
        main_label.setGeometry(30,366,60,50)
        password_label.setGeometry(30,416,90,50)


        nameEdit = QtGui.QLineEdit(self)
        firstnameEdit = QtGui.QLineEdit(self)
        mailEdit = QtGui.QLineEdit(self)
        passwordEdit = QtGui.QLineEdit(self)
        nameEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        firstnameEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        mailEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")

        nameEdit.setGeometry(130,278,250,30)
        firstnameEdit.setGeometry(130,328,250,30)
        mailEdit.setGeometry(130,378,250,30)
        passwordEdit.setGeometry(130,428,250,30)


        
        
        #Кнопка регестрации
        registration_button = QtGui.QPushButton('Registration', self)
        registration_button.setStyleSheet("QPushButton {background:#088A08}")
        registration_button.setGeometry(230,500,150,50)

        
        

       


        
        

        #self.connect(quit, QtCore.SIGNAL('clicked()'),
            #QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QRegistration()

qb.show()
sys.exit(app.exec_())
