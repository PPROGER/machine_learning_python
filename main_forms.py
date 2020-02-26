#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore




class QMain(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 1600,900)
        self.setWindowTitle('Main')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        menu = QtGui.QLabel(self)
        menu.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        menu.resize(250, 900)
       
        menu.setGeometry(0,0,250,900)

        style_button = "QPushButton {background:#696969; border-radius: 10px; border: 1px solid #C0C0C0;}"

        self.cam_button = QtGui.QPushButton('CAM', menu)
        self.cam_button.setStyleSheet(style_button)
        self.cam_button.setIcon(QtGui.QIcon('image/cam.png'))
        self.cam_button.setIconSize(QtCore.QSize(48,48))
        self.cam_button.setGeometry(25,100,200,100)




        self.video_button = QtGui.QPushButton('VIDEO', menu)
        self.video_button.setStyleSheet(style_button)
        self.video_button.setIcon(QtGui.QIcon('image/video.png'))
        self.video_button.setIconSize(QtCore.QSize(48,48))
        self.video_button.setGeometry(25,250,200,100)



        self.foto_button = QtGui.QPushButton('FOTO', menu)
        self.foto_button.setStyleSheet(style_button)
        self.foto_button.setIcon(QtGui.QIcon('image/foto.png'))
        self.foto_button.setIconSize(QtCore.QSize(48,48))
        self.foto_button.setGeometry(25,400,200,100)




        self.db_button = QtGui.QPushButton('DB', menu)
        self.db_button.setStyleSheet(style_button)
        self.db_button.setIcon(QtGui.QIcon('image/db.png'))
        self.db_button.setIconSize(QtCore.QSize(48,48))
        self.db_button.setGeometry(25,550,200,100)
        


        self.settings_button = QtGui.QPushButton('SETTINGS', menu)
        self.settings_button.setStyleSheet(style_button)
        self.settings_button.setIcon(QtGui.QIcon('image/settings.png'))
        self.settings_button.setIconSize(QtCore.QSize(48,48))
        self.settings_button.setGeometry(25,700,200,100)



        #Панель инструментов
        panel = QtGui.QLabel(self)
        panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        panel.setGeometry(242,0,1100,60)

        #Профіль панель
        profil_panel = QtGui.QLabel(self)
        profil_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        profil_panel.setGeometry(1334,0,266,60)

        label_image_user = QtGui.QLabel(profil_panel)
        pixmap = QtGui.QPixmap('image/profil.png')
        label_image_user.setPixmap(pixmap)
        label_image_user.setStyleSheet("QLabel {background:#808080; border: 1px solid #808080; border-radius: 1px; padding-left: 5px; margin: 6px}")
        label_image_user.resize(80,60)

        self.FIO_label = QtGui.QLabel('Andrey Kornienko',profil_panel)
        self.FIO_label.setStyleSheet("QLabel {background:#808080; border: 1px solid #808080; border-radius: 1px; padding-left: 1px; margin: 6px}")
        self.FIO_label.setGeometry(80,0,181,60)

        #Settings panel
        self.main_panel = QtGui.QLabel(self)
        self.main_panel.setVisible(False)
        self.main_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.main_panel.setGeometry(242,52,1359,848)


        #Фон для Face id
        bagraound_label = QtGui.QLabel(self.main_panel)
        bagraound_label.setStyleSheet("QLabel {background:#696969; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        bagraound_label.setGeometry(0,0,1359,400)

        #Регистрация Фейс айди
        label_registartion = QtGui.QLabel("Registartion Face ID:",self.main_panel)
        label_registartion.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969;}")
        label_registartion.setGeometry(10,10,300,50)
        self.face_registration = QtGui.QPushButton("Registartion",self.main_panel)
        self.face_registration.setIcon(QtGui.QIcon('image/faceID_registration'))
        self.face_registration.setIconSize(QtCore.QSize(50,50))
        self.face_registration.setStyleSheet("QPushButton {background:#696969; border-radius: 10px; border: 1px solid #C0C0C0; font: 20px;}")
        self.face_registration.setGeometry(40,70,250,50)
        
        #Использовать Face id для входа в БД
        label_db = QtGui.QLabel("Use Face ID to enter the database:",self.main_panel)
        label_db.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969;}")
        label_db.setGeometry(10,150,410,50)
        

        yes_label_db = QtGui.QLabel("Yes",self.main_panel)
        yes_label_db.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969;}")
        yes_label_db.setGeometry(15,210,60,30)

        self.db_faceid_button = QtGui.QPushButton(self.main_panel)
        self.db_faceid_button.setIcon(QtGui.QIcon('image/0.png'))
        self.db_faceid_button.setIconSize(QtCore.QSize(70,70))
        self.db_faceid_button.setStyleSheet("QPushButton {background:#696969; border-radius: 16px; }")
        self.db_faceid_button.setGeometry(85,210,70,35)

        false_label_db = QtGui.QLabel("False",self.main_panel)
        false_label_db.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969;}")
        false_label_db.setGeometry(150,205,80,40)
        
        
        #Использование фейс айди для входа в приложение
        label_log = QtGui.QLabel("Using face id to enter the application:",self.main_panel)
        label_log.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_log.setGeometry(10,260,440,50)
        
        yes_label_log = QtGui.QLabel("Yes",self.main_panel)
        yes_label_log.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969;}")
        yes_label_log.setGeometry(15,320,60,30)

        self.log_button = QtGui.QPushButton(self.main_panel)
        self.log_button.setIcon(QtGui.QIcon('image/0.png'))
        self.log_button.setIconSize(QtCore.QSize(70,70))
        self.log_button.setStyleSheet("QPushButton {background:#696969; border-radius: 16px; }")
        self.log_button.setGeometry(85,320,70,35)

        false_label_log = QtGui.QLabel("False",self.main_panel)
        false_label_log.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969;}")
        false_label_log.setGeometry(150,315,80,40)       
        
        #Фон для системных настроек 
        system_label = QtGui.QLabel(self.main_panel)
        system_label.setStyleSheet("QLabel {background:#696969; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        system_label.setGeometry(0,392,679.5,455)

        #Светлая тема или темная
        label_theme = QtGui.QLabel("Theme:",system_label)
        label_theme.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_theme.setGeometry(10,10,150,30)
        black_tema = QtGui.QLabel("Dark",system_label)
        black_tema.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969}")
        black_tema.setGeometry(15,50,70,30)

        self.tema_button = QtGui.QPushButton(system_label)
        self.tema_button.setIcon(QtGui.QIcon('image/0.png'))
        self.tema_button.setIconSize(QtCore.QSize(70,70))
        self.tema_button.setStyleSheet("QPushButton {background:#696969; border-radius: 16px; }")
        self.tema_button.setGeometry(95,50,70,35)

        theme_tema = QtGui.QLabel("Light",system_label)
        theme_tema.setStyleSheet("QLabel {background:#696969; color: black; font: 20px; border: 1px solid #696969}")
        theme_tema.setGeometry(165,45,70,40)

        #Язык системы 
        label_language = QtGui.QLabel("Language:",system_label)
        label_language.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_language.setGeometry(15,100,150,50)

        ukr_button = QtGui.QPushButton(system_label)
        ukr_button.setIcon(QtGui.QIcon('image/english.png'))
        ukr_button.setIconSize(QtCore.QSize(70,70))
        ukr_button.setGeometry(50,160,64,40)
        english_button = QtGui.QPushButton(system_label)
        english_button.setIcon(QtGui.QIcon('image/ukraine.png'))
        english_button.setIconSize(QtCore.QSize(70,70))
        english_button.setGeometry(116,160,64,40)

        #Фон для технічної підтримки
        label_tehn = QtGui.QLabel(self.main_panel)
        label_tehn.setStyleSheet("QLabel {background:#696969; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        label_tehn.setGeometry(671,392,686,455)
        
        label_podderjka = QtGui.QLabel("Technical support:",label_tehn)
        label_podderjka.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_podderjka.setGeometry(1,1,250,50)
        label_mail_tehn = QtGui.QLabel("Gmail:",label_tehn)
        label_mail_tehn.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_mail_tehn.setGeometry(20,52,100,50)
        
        self.mail_edit_tehn = QtGui.QLineEdit(label_tehn)
        self.mail_edit_tehn.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.mail_edit_tehn.setGeometry(130,63,400,30)

        label_text = QtGui.QLabel("Message:",label_tehn)
        label_text.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_text.setGeometry(20,110,150,50)

        self.message_edit = QtGui.QTextEdit(label_tehn)
        self.message_edit.setStyleSheet("QTextEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.message_edit.setGeometry(40,170,605,200)

        self.enter_button = QtGui.QPushButton(label_tehn)
        self.enter_button.setIcon(QtGui.QIcon('image/message.png'))
        self.enter_button.setIconSize(QtCore.QSize(84,84))
        self.enter_button.setStyleSheet("QPushButton {background:#696969; border-radius: 10px; border: 1px solid #C0C0C0;}")
        self.enter_button.setGeometry(500,380,154,60)

        

        #DB panel  
        self.db_panel = QtGui.QLabel(self)
        #self.db_panel.setVisible(False)
        self.db_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.db_panel.setGeometry(242,52,1359,848)

        #Login panel DB
        self.panel_loning_db = QtGui.QLabel(self.db_panel)
        #self.panel_loning_db.setVisible(False)
        self.panel_loning_db.setStyleSheet("QLabel {background:#696969; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.panel_loning_db.setGeometry(459.5,100,400,600)

        label_image = QtGui.QLabel(self.panel_loning_db)
        pixmap = QtGui.QPixmap('image/db_image')
        label_image.setPixmap(pixmap)
        label_image.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        label_image.setGeometry(120,50,160,145)

        login = QtGui.QLabel(self.panel_loning_db)
        pixmap1 = QtGui.QPixmap('image/login.png')
        login.setPixmap(pixmap1)
        login.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        login.setGeometry(20,200,74,74)

        self.loginEdit = QtGui.QLineEdit(self.panel_loning_db)
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.loginEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.loginEdit.setGeometry(100,222,240,30)
        self.loginEdit.setAlignment(QtCore.Qt.AlignCenter)

        password = QtGui.QLabel(self.panel_loning_db)
        pixmap2 = QtGui.QPixmap('image/password.png')
        password.setPixmap(pixmap2)
        password.setStyleSheet("QLabel {background:#696969; color: black; font: 25px; border: 1px solid #696969}")
        password.setGeometry(20,300,74,74)

        self.passwordEdit = QtGui.QLineEdit(self.panel_loning_db)
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray;}")
        self.passwordEdit.setStyleSheet("QLineEdit {color:orange; font: 16px;}")
        self.passwordEdit.setGeometry(100,322,240,30)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        #Кнопка входа
        self.log_button = QtGui.QPushButton('Login', self.panel_loning_db)
        self.log_button.setStyleSheet("QPushButton {background:#088A08}")
        self.log_button.setGeometry(200,450,160,50)

        #Кнопка face id
        self.face_button = QtGui.QPushButton(self.panel_loning_db)
        #self.face_button.setStyleSheet("QPushButton {background:#696969}")
        self.face_button.setIcon(QtGui.QIcon('image/face.png'))
        self.face_button.setIconSize(QtCore.QSize(64,64))
        self.face_button.setGeometry(60,450,50,53)

        #DB FUNCTION PANEL
        self.db_panel_function = QtGui.QLabel(self)
        self.db_panel_function.setVisible(False)
        self.db_panel_function.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.db_panel_function.setGeometry(242,52,1359,848)


        #FOTO panel  
        self.foto_panel = QtGui.QLabel(self)
        self.foto_panel.setVisible(False)
        self.foto_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.foto_panel.setGeometry(242,52,1359,848)




        #Video panel  
        self.video_panel = QtGui.QLabel(self)
        self.video_panel.setVisible(False)
        self.video_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.video_panel.setGeometry(242,52,1359,848)


        #Cam panel  
        self.cam_panel = QtGui.QLabel(self)
        self.cam_panel.setVisible(False)
        self.cam_panel.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.cam_panel.setGeometry(242,52,1359,848)  


#app = QtGui.QApplication(sys.argv)
#qb = QMain()

#qb.show()
#sys.exit(app.exec_())
