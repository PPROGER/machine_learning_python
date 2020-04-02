#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore




class QMain(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 1600,900)
        self.setWindowTitle('Laboratory detection')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        menu = QtGui.QLabel(self)
        menu.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        menu.resize(250, 900)
       
        menu.setGeometry(0,0,250,900)

        style_button = "QPushButton {background:transparent; border-radius: 5px; border: 2px solid #076CDA; font: 16px;} QPushButton:pressed {border: 2px solid #26B186}"

        self.cam_button = QtGui.QPushButton('CAM', menu)
        self.cam_button.setStyleSheet(style_button)
        self.cam_button.setIcon(QtGui.QIcon('image/cam.png'))
        self.cam_button.setIconSize(QtCore.QSize(48,48))
        self.cam_button.setGeometry(25,80,200,60)




        self.video_button = QtGui.QPushButton('VIDEO', menu)
        self.video_button.setStyleSheet(style_button)
        self.video_button.setIcon(QtGui.QIcon('image/video.png'))
        self.video_button.setIconSize(QtCore.QSize(48,48))
        self.video_button.setGeometry(25,160,200,60)



        self.foto_button = QtGui.QPushButton('FOTO', menu)
        self.foto_button.setStyleSheet(style_button)
        self.foto_button.setIcon(QtGui.QIcon('image/foto.png'))
        self.foto_button.setIconSize(QtCore.QSize(48,48))
        self.foto_button.setGeometry(25,240,200,60)




        self.db_button = QtGui.QPushButton('DB', menu)
        self.db_button.setStyleSheet(style_button)
        self.db_button.setIcon(QtGui.QIcon('image/db.png'))
        self.db_button.setIconSize(QtCore.QSize(48,48))
        self.db_button.setGeometry(25,320,200,60)
        


        self.settings_button = QtGui.QPushButton('SETTINGS', menu)
        self.settings_button.setStyleSheet(style_button)
        self.settings_button.setIcon(QtGui.QIcon('image/settings.png'))
        self.settings_button.setIconSize(QtCore.QSize(48,48))
        self.settings_button.setGeometry(25,400,200,60)


        #Плагины 
        self.plugins = QtGui.QPushButton('PLAGINS',menu)
        self.plugins.setStyleSheet(style_button)
        self.plugins.setIcon(QtGui.QIcon('image/plagin.png'))
        self.plugins.setIconSize(QtCore.QSize(48,48))
        self.plugins.setGeometry(25,480,200,60)

        #Голосовой асистент
        self.voise = QtGui.QPushButton('VOICE ASSISTANT', menu)
        self.voise.setStyleSheet(style_button)
        self.voise.setIcon(QtGui.QIcon('image/voice_assistant.png'))
        self.voise.setIconSize(QtCore.QSize(48,48))
        self.voise.setGeometry(25,560,200,60)

        #Помощь
        self.help = QtGui.QPushButton('HELP', menu)
        self.help.setStyleSheet(style_button)
        self.help.setIcon(QtGui.QIcon('image/help.png'))
        self.help.setIconSize(QtCore.QSize(64,64))
        self.help.setGeometry(25,640,200,60)

        line_label_menu = QtGui.QLabel(menu)
        line_label_menu.setStyleSheet("QLabel {background: #34393D}")
        line_label_menu.setGeometry(0,800,250,3)

        self.logout_button = QtGui.QPushButton('Logout',menu)
        self.logout_button.setStyleSheet("QPushButton {background: transparent; font: 14}")
        self.logout_button.setGeometry(100,820,50,50)

        #Панель инструментов
        panel = QtGui.QLabel(self)
        panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        panel.setGeometry(242,0,1100,60)

        

        #Профіль панель
        profil_panel = QtGui.QLabel(self)
        profil_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        profil_panel.setGeometry(1334,0,266,60)

        label_image_user = QtGui.QLabel(profil_panel)
        pixmap = QtGui.QPixmap('image/profil.png')
        label_image_user.setPixmap(pixmap)
        label_image_user.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 1px; padding-left: 5px; margin: 6px}")
        label_image_user.resize(80,60)

        self.FIO_label = QtGui.QLabel('Andrey Kornienko',profil_panel)
        self.FIO_label.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 1px; padding-left: 1px; margin: 6px; font: 18px}")
        self.FIO_label.setGeometry(80,0,181,60)

        #Settings panel
        self.main_panel = QtGui.QLabel(self)
        self.main_panel.setVisible(False)
        self.main_panel.setStyleSheet("QLabel {background:#1F2327; border: 1px solid transparent; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.main_panel.setGeometry(243,53,1359,848)


        #Фон для Face id
        bagraound_label = QtGui.QLabel(self.main_panel)
        bagraound_label.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        bagraound_label.setGeometry(10,10,1339,380)

        #Регистрация Фейс айди
        label_registartion = QtGui.QLabel("Registration Face ID:",self.main_panel)
        label_registartion.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_registartion.setGeometry(10,10,300,50)
        self.face_registration = QtGui.QPushButton("Registartion",self.main_panel)
        self.face_registration.setIcon(QtGui.QIcon('image/faceID_registration'))
        self.face_registration.setIconSize(QtCore.QSize(50,50))
        self.face_registration.setStyleSheet("QPushButton {background:transparent; border-radius: 10px; border: 1px solid #076CDA; font: 20px;}")
        self.face_registration.setGeometry(40,70,250,50)
        
        #Использовать Face id для входа в БД
        label_db = QtGui.QLabel("Use Face ID to enter the database:",self.main_panel)
        label_db.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_db.setGeometry(10,150,410,50)
        

        yes_label_db = QtGui.QLabel("Yes",self.main_panel)
        yes_label_db.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        yes_label_db.setGeometry(15,210,80,30)

        self.db_faceid_button = QtGui.QPushButton(self.main_panel)
        self.db_faceid_button.setIcon(QtGui.QIcon('image/0.png'))
        self.db_faceid_button.setIconSize(QtCore.QSize(70,70))
        self.db_faceid_button.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; }")
        self.db_faceid_button.setGeometry(100,210,70,35)

        false_label_db = QtGui.QLabel("False",self.main_panel)
        false_label_db.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        false_label_db.setGeometry(170,205,100,40)
        
        
        #Использование фейс айди для входа в приложение
        label_log = QtGui.QLabel("Using face id to enter the application:",self.main_panel)
        label_log.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_log.setGeometry(10,260,440,50)
        
        yes_label_log = QtGui.QLabel("Yes",self.main_panel)
        yes_label_log.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        yes_label_log.setGeometry(15,320,80,30)

        self.log_button_face = QtGui.QPushButton(self.main_panel)
        self.log_button_face.setIcon(QtGui.QIcon('image/0.png'))
        self.log_button_face.setIconSize(QtCore.QSize(70,70))
        self.log_button_face.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; }")
        self.log_button_face.setGeometry(100,320,70,35)

        false_label_log = QtGui.QLabel("False",self.main_panel)
        false_label_log.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        false_label_log.setGeometry(170,315,100,40)       
        
        #Фон для системных настроек 
        system_label = QtGui.QLabel(self.main_panel)
        system_label.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        system_label.setGeometry(10,392,664.5,445)

        #Светлая тема или темная
        label_theme = QtGui.QLabel("Theme:",system_label)
        label_theme.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_theme.setGeometry(10,10,150,30)
        black_tema = QtGui.QLabel("Dark",system_label)
        black_tema.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        black_tema.setGeometry(15,50,80,30)

        self.tema_button = QtGui.QPushButton(system_label)
        self.tema_button.setIcon(QtGui.QIcon('image/0.png'))
        self.tema_button.setIconSize(QtCore.QSize(70,70))
        self.tema_button.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; }")
        self.tema_button.setGeometry(110,50,70,35)

        theme_tema = QtGui.QLabel("Light",system_label)
        theme_tema.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        theme_tema.setGeometry(176,45,90,40)

        #Язык системы 
        label_language = QtGui.QLabel("Language:",system_label)
        label_language.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
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
        label_tehn.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        label_tehn.setGeometry(676,392,672,445)
        
        label_podderjka = QtGui.QLabel("Technical support:",label_tehn)
        label_podderjka.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_podderjka.setGeometry(1,1,250,50)
        label_mail_tehn = QtGui.QLabel("Gmail:",label_tehn)
        label_mail_tehn.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_mail_tehn.setGeometry(20,52,100,50)
        
        self.mail_edit_tehn = QtGui.QLineEdit(label_tehn)
        self.mail_edit_tehn.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.mail_edit_tehn.setGeometry(130,63,400,30)

        label_text = QtGui.QLabel("Message:",label_tehn)
        label_text.setStyleSheet("QLabel {background:transparent; color: white; font: 25px; border: 1px solid transparent;}")
        label_text.setGeometry(20,110,150,50)

        self.message_edit = QtGui.QTextEdit(label_tehn)
        self.message_edit.setStyleSheet("QTextEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.message_edit.setGeometry(40,170,605,200)

        self.enter_button = QtGui.QPushButton(label_tehn)
        self.enter_button.setIcon(QtGui.QIcon('image/message.png'))
        self.enter_button.setIconSize(QtCore.QSize(74,74))
        self.enter_button.setStyleSheet("QPushButton {background:transparent; border-radius: 10px; border: 2px solid #26B186} QPushButton:pressed {border: 2px solid #26B186}")
        self.enter_button.setGeometry(500,380,144,50)

        

        #DB panel  
        self.db_panel = QtGui.QLabel(self)
        #self.db_panel.setVisible(False)
        self.db_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.db_panel.setGeometry(243,53,1359,848)

        #Login panel DB
        self.panel_loning_db = QtGui.QLabel(self.db_panel)
        #self.panel_loning_db.setVisible(False)
        self.panel_loning_db.setStyleSheet("QLabel {background:#292E33; border: 3px solid #076CDA; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.panel_loning_db.setGeometry(459.5,100,400,600)

        label_image = QtGui.QLabel(self.panel_loning_db)
        pixmap = QtGui.QPixmap('image/db_image')
        label_image.setPixmap(pixmap)
        label_image.setStyleSheet("QLabel {background:#292E33; color: black; font: 25px; border: 1px solid #292E33}")
        label_image.setGeometry(120,50,160,145)

        login = QtGui.QLabel(self.panel_loning_db)
        pixmap1 = QtGui.QPixmap('image/login.png')
        login.setPixmap(pixmap1)
        login.setStyleSheet("QLabel {background:transparent; color: black; font: 25px; border: 1px solid transparent}")
        login.setGeometry(20,200,74,74)

        self.loginEdit = QtGui.QLineEdit(self.panel_loning_db)
        self.loginEdit.setStyleSheet("QLineEdit {background:transparent;color:orange; font: 16px; border: 1px solid gray; }")
        self.loginEdit.setGeometry(100,222,240,30)
        self.loginEdit.setAlignment(QtCore.Qt.AlignCenter)

        password = QtGui.QLabel(self.panel_loning_db)
        pixmap2 = QtGui.QPixmap('image/password.png')
        password.setPixmap(pixmap2)
        password.setStyleSheet("QLabel {background:#292E33; color: black; font: 25px; border: 1px solid #292E33}")
        password.setGeometry(20,300,74,74)

        self.passwordEdit = QtGui.QLineEdit(self.panel_loning_db)
        self.passwordEdit.setStyleSheet("QLineEdit {background:#292E33; color:orange; font: 16px; border: 1px solid gray;}")
        self.passwordEdit.setGeometry(100,322,240,30)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        #Кнопка входа
        self.log_button = QtGui.QPushButton('Login', self.panel_loning_db)
        self.log_button.setStyleSheet("QPushButton {background:#088A08; border: 1px solid #00FF00; border-radius: 5px;}")
        self.log_button.setGeometry(180,420,160,50)

        #Кнопка face id
        self.face_button = QtGui.QPushButton(self.panel_loning_db)
        self.face_button.setStyleSheet("QPushButton {background:#292E33}")
        self.face_button.setIcon(QtGui.QIcon('image/face.png'))
        self.face_button.setIconSize(QtCore.QSize(64,64))
        self.face_button.setGeometry(70,421,50,53)

        #DB FUNCTION PANEL
        self.db_panel_function = QtGui.QLabel(self)
        self.db_panel_function.setVisible(False)
        self.db_panel_function.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.db_panel_function.setGeometry(243,53,1359,848)

        self.label_datatime = QtGui.QLabel("03/23/21",self.db_panel_function)
        self.label_datatime.setStyleSheet("QLabel {background:#292E33; color: white; font: 25px; border: 1px solid #696969}")
        self.label_datatime.setGeometry(1180,10,170,50)
        
        #Панель для таблицы user
        self.table_user_panel = QtGui.QLabel()
        #self.table_user_panel.setVisible(False)
        self.table_user_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.table_user_panel.setGeometry(0,0,1200,780)

        #Таблица user
        self.table_widget = QtGui.QTableWidget(self.table_user_panel)
        self.table_widget.setGeometry(10,10,700,725)
        self.table_widget.setStyleSheet("QTableWidget {}")

        labels_column = ['ID','Name', 'Lastname', 'Gmail', 'Password']

        self.table_widget.setColumnCount(len(labels_column))
        self.table_widget.setHorizontalHeaderLabels(labels_column)

        #Поиск в таблице user
        label_znach = QtGui.QLabel("Enter value:",self.table_user_panel)
        label_znach.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_znach.setGeometry(725,20,200,50)

        self.poiskEdit = QtGui.QLineEdit(self.table_user_panel)
        self.poiskEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.poiskEdit.setGeometry(770,90,450,35)
        self.poiskEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.poisk_button = QtGui.QPushButton('Search', self.table_user_panel)
        self.poisk_button.setStyleSheet("QPushButton {background:#088A08; border-radius: 10px;border: 1px solid #088A08}")
        self.poisk_button.setGeometry(1150,150,160,50)


        label_image = QtGui.QLabel(self.table_user_panel)
        pixmap = QtGui.QPixmap('image/line.png')
        label_image.setPixmap(pixmap)
        label_image.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        label_image.setGeometry(715,200,600,50)

        #Добавление данных в таблицу user
        label_name = QtGui.QLabel("Name:",self.table_user_panel)
        label_name.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_name.setGeometry(725,250,150,50)

        self.nameEdit = QtGui.QLineEdit(self.table_user_panel)
        self.nameEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.nameEdit.setGeometry(880,258,300,30)
        self.nameEdit.setAlignment(QtCore.Qt.AlignCenter)


        label_lastname = QtGui.QLabel("Lastname:",self.table_user_panel)
        label_lastname.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_lastname.setGeometry(725,310,150,50)

        self.lastnameEdit = QtGui.QLineEdit(self.table_user_panel)
        self.lastnameEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.lastnameEdit.setGeometry(880,318,300,30)
        self.lastnameEdit.setAlignment(QtCore.Qt.AlignCenter)

        label_gmail = QtGui.QLabel("Gmail:",self.table_user_panel)
        label_gmail.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_gmail.setGeometry(725,370,150,50)

        self.gmailEdit = QtGui.QLineEdit(self.table_user_panel)
        self.gmailEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.gmailEdit.setGeometry(880,378,300,30)
        self.gmailEdit.setAlignment(QtCore.Qt.AlignCenter)

        label_password = QtGui.QLabel("Password:",self.table_user_panel)
        label_password.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_password.setGeometry(725,430,150,50)

        self.passEdit = QtGui.QLineEdit(self.table_user_panel)
        self.passEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.passEdit.setGeometry(880,438,300,30)
        self.passEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.add_button = QtGui.QPushButton('Add data', self.table_user_panel)
        self.add_button.setStyleSheet("QPushButton {background:#088A08; border-radius: 10px;border: 1px solid #088A08}")
        self.add_button.setGeometry(1150,500,160,50)


        label_image1 = QtGui.QLabel(self.table_user_panel)
        pixmap1 = QtGui.QPixmap('image/line.png')
        label_image1.setPixmap(pixmap1)
        label_image1.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        label_image1.setGeometry(715,550,600,50)

        #Удаление с таблицы user
        label_znach_del = QtGui.QLabel("Enter value:",self.table_user_panel)
        label_znach_del.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 25px;}")
        label_znach_del.setGeometry(725,600,170,50)

        self.delEdit = QtGui.QLineEdit(self.table_user_panel)
        self.delEdit.setStyleSheet("QLineEdit {color:orange; font: 16px; border: 2px solid gray; }")
        self.delEdit.setGeometry(900,608,350,35)
        self.delEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.del_button = QtGui.QPushButton('Delete', self.table_user_panel)
        self.del_button.setStyleSheet("QPushButton {background:#088A08; border-radius: 10px;border: 1px solid #088A08}")
        self.del_button.setGeometry(1150,670,160,50)

        #Панель для таблицы messager
        self.table_messager_panel = QtGui.QLabel()
        #self.table_messager_panel.setVisible(False)
        self.table_messager_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.table_messager_panel.setGeometry(0,0,1200,780)



        #Таб панель 
        self.tab = QtGui.QTabWidget(self.db_panel_function)
        self.tab.setGeometry(10,50,1339,780)
        self.tab.addTab(self.table_user_panel,'User')
        self.tab.addTab(self.table_messager_panel,'Message')



        #FOTO panel  
        self.foto_panel = QtGui.QLabel(self)
        self.foto_panel.setVisible(False)
        self.foto_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.foto_panel.setGeometry(243,53,1359,848)

        #Video panel  
        self.video_panel = QtGui.QLabel(self)
        self.video_panel.setVisible(False)
        self.video_panel.setStyleSheet("QLabel {background:#1F2327; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.video_panel.setGeometry(243,53,1359,848)


        #Cam panel  
        self.cam_panel = QtGui.QLabel(self)
        self.cam_panel.setVisible(False)
        self.cam_panel.setStyleSheet("QLabel {background:#1F2327; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.cam_panel.setGeometry(243,53,1359,848)  



