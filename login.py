#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore





class Qlogin(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(350, 200, 1200, 754)
        self.setWindowTitle('Laboratory detection')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(1200, 754)

        #Картинка
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/login_backgraund.jpg')
        label_image.setPixmap(pixmap)
        label_image.setGeometry(0,0,1200,754)
        
        #Общая панель для входа и регистрации
        self.panel_login_registration = QtGui.QLabel(self)
        self.panel_login_registration.setStyleSheet("QLabel {background: #010021}")
        self.panel_login_registration.setGeometry(620,90,450,565)

        #Общая панель для входа
        panel_login = QtGui.QLabel(self.panel_login_registration)
        panel_login.setStyleSheet("QLabel {background: #010021}")
        panel_login.setGeometry(600,200,450,465)
        



        #Поля ввода
        login = QtGui.QLabel(panel_login)
        pixmap1 = QtGui.QPixmap('image/login.png')
        login.setPixmap(pixmap1)
        login.setGeometry(60,80,64,64)

        self.loginEdit = QtGui.QLineEdit(panel_login)
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.loginEdit.setGeometry(130,102,240,30)
        self.loginEdit.setAlignment(QtCore.Qt.AlignCenter)

        password = QtGui.QLabel(panel_login)
        pixmap2 = QtGui.QPixmap('image/password.png')
        password.setPixmap(pixmap2)
        password.setGeometry(60,180,64,64)

        self.passwordEdit = QtGui.QLineEdit(panel_login)
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray;}")
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.passwordEdit.setGeometry(130,202,240,30)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        #Кнопка входа
        self.log_button = QtGui.QPushButton('Sign in', panel_login)
        self.log_button.setStyleSheet("QPushButton {background:#088A08; border: 1px solid #00FF00; border-radius: 5px;}")
        self.log_button.setGeometry(170,300,200,50)

        #Кнопка face id
        self.face_button = QtGui.QPushButton(panel_login)
        self.face_button.setStyleSheet("QPushButton {background:transparent}")
        self.face_button.setIcon(QtGui.QIcon('image/face.png'))
        self.face_button.setIconSize(QtCore.QSize(64,64))
        self.face_button.setGeometry(70,300,50,53)

        #self.registration_button = QtGui.QPushButton('Registration', panel_login)
        #self.registration_button.setStyleSheet("QPushButton {color:#00FF00; font: 16px;}")
        #self.registration_button.setGeometry(10,100,120,30)

        self.vostanovlenie_button = QtGui.QPushButton("Forgot your password?",panel_login)
        self.vostanovlenie_button.setStyleSheet("QPushButton  {background:transparent; color:#00FF00; font: 16px;}")
        self.vostanovlenie_button.setGeometry(130,400,200,30)




        #Панель для регистрации
        panel_registration = QtGui.QLabel(self.panel_login_registration)
        panel_registration.setStyleSheet("QLabel {background: #010021}")
        panel_registration.setGeometry(620,100,450,565)

        name_label = QtGui.QLabel("Name",panel_registration)
        firstname_label = QtGui.QLabel("Lastname",panel_registration)
        main_label = QtGui.QLabel("Gmail",panel_registration)
        password_label = QtGui.QLabel("Password",panel_registration)
        
        name_label.setStyleSheet("QLabel {font: 20px;}")
        firstname_label.setStyleSheet("QLabel {font: 20px;}")
        main_label.setStyleSheet("QLabel {font: 20px;}")
        password_label.setStyleSheet("QLabel {font: 20px;}")


        name_label.setGeometry(30,80,60,50)
        firstname_label.setGeometry(30,150,90,50)
        main_label.setGeometry(30,220,60,50)
        password_label.setGeometry(30,290,90,50)

        ctyle_texedit = "QLineEdit {color:orange; font: 16px;}"
        self.nameEdit = QtGui.QLineEdit(panel_registration)
        self.firstnameEdit = QtGui.QLineEdit(panel_registration)
        self.mailEdit = QtGui.QLineEdit(panel_registration)
        self.password_Edit = QtGui.QLineEdit(panel_registration)
        self.nameEdit.setStyleSheet(ctyle_texedit)
        self.firstnameEdit.setStyleSheet(ctyle_texedit)
        self.mailEdit.setStyleSheet(ctyle_texedit)
        self.password_Edit.setStyleSheet(ctyle_texedit)

       
        self.nameEdit.setGeometry(130,90,250,30)
        self.firstnameEdit.setGeometry(130,160,250,30)
        self.mailEdit.setGeometry(130,230,250,30)
        self.password_Edit.setGeometry(130,300,250,30)


        
        
        #Кнопка регестрации
        self.registration_button = QtGui.QPushButton('Registration', panel_registration)
        self.registration_button.setStyleSheet("QPushButton {background:#088A08; border: 1px solid #00FF00; border-radius: 5px;}")
        self.registration_button.setGeometry(180,380,200,50)



        self.tab = QtGui.QTabWidget(self.panel_login_registration)
        self.tab.setGeometry(0,30,600,545)
        self.tab.addTab(panel_login,'LOG IN')
        self.tab.addTab(panel_registration,'REGISTRATION')
        
        #Панель для востановление пароля
        self.panel_recovery = QtGui.QLabel(self)
        self.panel_recovery.setVisible(False)
        self.panel_recovery.setStyleSheet("QLabel {background: #010021}")
        self.panel_recovery.setGeometry(620,90,450,565)

        firstname__label = QtGui.QLabel("Firstname",self.panel_recovery)
        main__label = QtGui.QLabel("Gmail",self.panel_recovery)
        password__label = QtGui.QLabel("New Password",self.panel_recovery)
        

        firstname__label.setStyleSheet("QLabel {font: 20px;}")
        main__label.setStyleSheet("QLabel {font: 20px;}")
        password__label.setStyleSheet("QLabel {font: 20px;}")


        firstname__label.setGeometry(30,60,90,50)
        main__label.setGeometry(30,140,60,50)
        password__label.setGeometry(30,220,140,50)


       
        self.firstname__Edit = QtGui.QLineEdit(self.panel_recovery)
        self.mail__Edit = QtGui.QLineEdit(self.panel_recovery)
        self.password__Edit = QtGui.QLineEdit(self.panel_recovery)

        self.firstname__Edit.setStyleSheet("QLineEdit {color:orange; font: 16px; }")
        self.mail__Edit.setStyleSheet("QLineEdit {color:orange; font: 16px; }")
        self.password__Edit.setStyleSheet("QLineEdit {color:orange; font: 16px; }")

    
        self.firstname__Edit.setGeometry(170,70,220,30)
        self.mail__Edit.setGeometry(170,150,220,30)
        self.password__Edit.setGeometry(170,230,220,30)


        
        
        #Кнопка востановления
        self.recovey_button_ = QtGui.QPushButton('Recovery', self.panel_recovery)
        self.recovey_button_.setStyleSheet("QPushButton {background:#088A08; border: 1px solid #00FF00; border-radius: 5px;}")
        self.recovey_button_.setGeometry(100,350,250,50)


        self.log_r_button = QtGui.QPushButton("Log in",self.panel_recovery)
        self.log_r_button.setStyleSheet("QPushButton  {background:transparent; color:#00FF00; font: 16px;}")
        self.log_r_button.setGeometry(130,480,200,30)



        


 
