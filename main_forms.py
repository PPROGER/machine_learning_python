#!/usr/bin/python
import random
import sys
from PyQt4 import QtGui, QtCore
from menu_tree import Window




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
        
        #Cловарь для поиска
        model = QtGui.QStringListModel()
        model.setStringList(['Face ID', 'Face', 'in', 'my', 'dictionary'])

        completer = QtGui.QCompleter()
        completer.setModel(model)

        #Кнопка поиска
        self.search_function_button = QtGui.QPushButton(" Search",panel)
        self.search_function_button.setStyleSheet("QPushButton {background:#007AFF; border: 1px solid #007AFF; border-radius: 0px}")
        self.search_function_button.setGeometry(530,13.7,100,34)

        #Сам поиск 
        lineedit = QtGui.QLineEdit(panel)
        lineedit.setCompleter(completer)
        lineedit.setStyleSheet("QLineEdit {background:#222528; border-radius: 0px; font: 18px;}")
        lineedit.setGeometry(30,13,500,35)
        lineedit.setAlignment(QtCore.Qt.AlignCenter)

        


        self.message_function_button = QtGui.QPushButton(panel)
        self.message_function_button.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;}")
        self.message_function_button.setIcon(QtGui.QIcon('image/massage_function_panel.png'))
        self.message_function_button.setIconSize(QtCore.QSize(30,35))
        self.message_function_button.setGeometry(980,13,40,40)

        self.bell_function_button = QtGui.QPushButton(panel)
        self.bell_function_button.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;}")
        self.bell_function_button.setIcon(QtGui.QIcon('image/bell_function_panel.png'))
        self.bell_function_button.setIconSize(QtCore.QSize(30,30))
        self.bell_function_button.setGeometry(1030,13,40,40)

        

        
        

        

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
        self.db_panel.setVisible(False)
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
        #self.cam_panel.setVisible(False)
        self.cam_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.cam_panel.setGeometry(243,53,1359,848)  

        #Создание кадров
        str_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 25px;}", "QLineEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }"]

        label_cam = QtGui.QLabel("Camera:",self.cam_panel)
        label_cam.setStyleSheet(str_style_css[0])
        label_cam.setGeometry(10,20,120,50)
        

        self.camEdit = QtGui.QLineEdit(self.cam_panel)
        self.camEdit.setStyleSheet(str_style_css[1])
        self.camEdit.setGeometry(145,28,200,35)
        self.camEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.camEdit.setText("0")

        label_width = QtGui.QLabel("Width:",self.cam_panel)
        label_width.setStyleSheet(str_style_css[0])
        label_width.setGeometry(370,20,120,50)

        self.widthEdit = QtGui.QLineEdit(self.cam_panel)
        self.widthEdit.setStyleSheet(str_style_css[1])
        self.widthEdit.setGeometry(490,28,200,35)
        self.widthEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.widthEdit.setText("640")

        label_height = QtGui.QLabel("Height:",self.cam_panel)
        label_height.setStyleSheet(str_style_css[0])
        label_height.setGeometry(715,20,120,50)

        self.heightEdit = QtGui.QLineEdit(self.cam_panel)
        self.heightEdit.setStyleSheet(str_style_css[1])
        self.heightEdit.setGeometry(840,28,200,35)
        self.heightEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.heightEdit.setText("480")

        label_puty = QtGui.QLabel("File path:",self.cam_panel)
        label_puty.setStyleSheet(str_style_css[0])
        label_puty.setGeometry(10,100,140,50)

        self.putyEdit = QtGui.QLineEdit(self.cam_panel)
        self.putyEdit.setStyleSheet(str_style_css[1])
        self.putyEdit.setGeometry(155,108,500,35)
        self.putyEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.putyEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/dataset/")
        

        label_object_number = QtGui.QLabel("Object number:",self.cam_panel)
        label_object_number.setStyleSheet(str_style_css[0])
        label_object_number.setGeometry(675,100,200,50)

        self.object_numberEdit = QtGui.QLineEdit(self.cam_panel)
        self.object_numberEdit.setStyleSheet(str_style_css[1])
        self.object_numberEdit.setGeometry(890,108,150,35)
        self.object_numberEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.object_numberEdit.setText("1")

        label_frames = QtGui.QLabel("Number of frames:",self.cam_panel)
        label_frames.setStyleSheet(str_style_css[0])
        label_frames.setGeometry(10,180,237,50)

        self.framesEdit = QtGui.QLineEdit(self.cam_panel)
        self.framesEdit.setStyleSheet(str_style_css[1])
        self.framesEdit.setGeometry(265,188,160,35)
        self.framesEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.framesEdit.setText("30")


        self.Face_dataset_button = QtGui.QPushButton('Face dataset', self.cam_panel)
        self.Face_dataset_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;}")
        self.Face_dataset_button.setGeometry(500,180,540,50)

        #line_label_cam1 = QtGui.QLabel(self.cam_panel)
        #line_label_cam1.setStyleSheet("QLabel {background: #34393D}")
        #line_label_cam1.setGeometry(0,300,1055,3)

    
        line_label_cam2 = QtGui.QLabel(self.cam_panel)
        line_label_cam2.setStyleSheet("QLabel {background: #34393D}")
        line_label_cam2.setGeometry(1093,0,3,847)

        #Тренировка распознования
        label_path_training = QtGui.QLabel("Path dataset:",self.cam_panel)
        label_path_training.setStyleSheet(str_style_css[0])
        label_path_training.setGeometry(10,290,237,50)

        self.path_trainingEdit = QtGui.QLineEdit(self.cam_panel)
        self.path_trainingEdit.setStyleSheet(str_style_css[1])
        self.path_trainingEdit.setGeometry(200,298,840,35)
        self.path_trainingEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.path_trainingEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/dataset")

        label_model = QtGui.QLabel("Save the model into:",self.cam_panel)
        label_model.setStyleSheet(str_style_css[0])
        label_model.setGeometry(10,370,260,50)

        self.modelEdit = QtGui.QLineEdit(self.cam_panel)
        self.modelEdit.setStyleSheet(str_style_css[1])
        self.modelEdit.setGeometry(280,378,760,35)
        self.modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modelEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/trainer/trainer.yml")

        self.Face_training_button = QtGui.QPushButton('Face training', self.cam_panel)
        self.Face_training_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;}")
        self.Face_training_button.setGeometry(500,450,540,50)

        #Распознование лица
        label_path_model = QtGui.QLabel("Path to training:",self.cam_panel)
        label_path_model.setStyleSheet(str_style_css[0])
        label_path_model.setGeometry(10,560,237,50)

        self.path_modelEdit = QtGui.QLineEdit(self.cam_panel)
        self.path_modelEdit.setStyleSheet(str_style_css[1])
        self.path_modelEdit.setGeometry(230,568,810,35)
        self.path_modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.path_modelEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/trainer/trainer.yml")

        label_object_name = QtGui.QLabel("Object name:",self.cam_panel)
        label_object_name.setStyleSheet(str_style_css[0])
        label_object_name.setGeometry(10,640,237,50)

        self.object_nameEdit = QtGui.QLineEdit(self.cam_panel)
        self.object_nameEdit.setStyleSheet(str_style_css[1])
        self.object_nameEdit.setGeometry(200,648,250,35)
        self.object_nameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.object_nameEdit.setText("Andrey")

        label_object_number_recognition = QtGui.QLabel("Object number:",self.cam_panel)
        label_object_number_recognition.setStyleSheet(str_style_css[0])
        label_object_number_recognition.setGeometry(475,640,200,50)

        self.object_number_recognitionEdit = QtGui.QLineEdit(self.cam_panel)
        self.object_number_recognitionEdit.setStyleSheet(str_style_css[1])
        self.object_number_recognitionEdit.setGeometry(690,648,120,35)
        self.object_number_recognitionEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.object_number_recognitionEdit.setText("1")

        self.Face_recognition_button = QtGui.QPushButton('Face training', self.cam_panel)
        self.Face_recognition_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;}")
        self.Face_recognition_button.setGeometry(500,720,540,50)

        self.check_button_add_object_db = QtGui.QCheckBox("Add object to db",self.cam_panel)
        self.check_button_add_object_db.setStyleSheet("QCheckBox {background:#292E33; font: 20px}")
        self.check_button_add_object_db.setChecked(False)
        self.check_button_add_object_db.setGeometry(850,640,200,50)

        style_object_label = "QLabel {background:#292E33; border: 1px solid #292E33; color: white; font: 14px;}"

        #Tree panel  
        self.tree_panel = QtGui.QLabel(self.cam_panel)
        #self.cam_panel.setVisible(False)
        self.tree_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px;}")
        self.tree_panel.setGeometry(1100,10,250,830)
    

        self.treeView = QtGui.QTreeView()
        self.treeView.setStyleSheet("QTreeView {background:#292E33;border: 1px solid #292E33}")
        

        def openMenu(self, position):
    
            indexes = self.treeView.selectedIndexes()
            if len(indexes) > 0:
        
                level = 0
                index = indexes[0]
                while index.parent().isValid():
                    index = index.parent()
                    level += 1
        
            menu = QtGui.QMenu()
            if level == 0:
                menu.addAction(self.tr("Edit person"))
            elif level == 1:
                menu.addAction(self.tr("Edit object/container"))
            elif level == 2:
                menu.addAction(self.tr("Edit object"))
        
            menu.exec_(self.treeView.viewport().mapToGlobal(position))

        data = [("Alice", [("Keys", []),("Purse", [("Cellphone", [])])]),("Bob", [("Wallet", [("Credit card", []),("Money", [])])])]

        def addItems(parent, elements):
    
            for text, children in elements:
                item = QtGui.QStandardItem(text)
                parent.appendRow(item)
                if children:
                    addItems(item, children)

        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(openMenu)

        model = QtGui.QStandardItemModel()
        addItems(model, data)
        self.treeView.setModel(model)
        
        model.setHorizontalHeaderLabels([self.tr("Object")])
        
        layout = QtGui.QVBoxLayout(self.tree_panel)
        layout.addWidget(self.treeView)
        
        



        #self.count_object_label = QtGui.QLabel("Number of objects:",self.cam_panel)
        #self.count_object_label.setStyleSheet(style_object_label)
        #self.count_object_label.setGeometry(1100,10,200,30)

        #self.name_object_label = QtGui.QLabel("Object names:",self.cam_panel)
       # self.name_object_label.setStyleSheet(style_object_label)
        #self.name_object_label.setGeometry(1100,40,150,100)
        

        


   
        
        






        
        




       
       
       



       

