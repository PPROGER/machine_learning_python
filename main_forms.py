#!/usr/bin/python
import random
import sys
from PyQt4 import QtGui, QtCore



class QMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(150, 100, 1600,1000)
        self.setWindowTitle('Laboratory detection')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(1600,926)
        self.statusBar = QtGui.QStatusBar()
        self.statusBar.setStyleSheet("QStatusBar{background:#076CDA;border-radius: 1px; }")
        self.setStatusBar(self.statusBar)

       

       

        
        

        menu = QtGui.QLabel(self)
        menu.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        menu.resize(250, 900)
       
        menu.setGeometry(0,0,250,900)

        style_button = "QPushButton {background:transparent; border-radius: 5px; border: 2px solid #076CDA; font: 16px;outline: none; } QPushButton:hover {font: bold; border: 3px solid #076CDA;} QPushButton:focus {color:#007AFF; font-weight: bold;}"

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
        self.plugins = QtGui.QPushButton('PLUGIN',menu)
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
        self.logout_button.setStyleSheet("QPushButton {background: transparent; font: 14; outline: none;} QPushButton:hover {font: bold}")
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
        self.search_function_button.setStyleSheet("QPushButton {background:#007AFF; border: 1px solid #007AFF; border-radius: 2px;outline: none; } QPushButton:hover {background:#007AFF;font-weight: bold;}")
        self.search_function_button.setGeometry(530,13.7,100,34)

        #Сам поиск 
        lineedit = QtGui.QLineEdit(panel)
        lineedit.setCompleter(completer)
        lineedit.setStyleSheet("QLineEdit {background:#222528; border-radius: 2px; font: 18px;}")
        lineedit.setGeometry(30,13,500,35)
        lineedit.setAlignment(QtCore.Qt.AlignCenter)

        
        self.micro_function_button = QtGui.QPushButton(panel)
        self.micro_function_button.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.micro_function_button.setIcon(QtGui.QIcon('image/micro_v.png'))
        self.micro_function_button.setIconSize(QtCore.QSize(35,30))
        self.micro_function_button.setGeometry(945,13,40,40)


        self.message_function_button = QtGui.QPushButton(panel)
        self.message_function_button.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;} QPushButton:focus {background:#1F2327;}")
        self.message_function_button.setIcon(QtGui.QIcon('image/massage_function_panel.png'))
        self.message_function_button.setIconSize(QtCore.QSize(35,35))
        self.message_function_button.setGeometry(990,13,40,40)

        self.bell_function_button = QtGui.QPushButton(panel)
        self.bell_function_button.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none; }QPushButton:hover {background:#1F2327;} QPushButton:focus {background:#1F2327;}")
        self.bell_function_button.setIcon(QtGui.QIcon('image/bell_function_panel.png'))
        self.bell_function_button.setIconSize(QtCore.QSize(30,30))
        self.bell_function_button.setGeometry(1035,13,40,40)

        

        
        

        

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
        self.main_panel.setGeometry(243,53,1357,847)

        settings_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 25px;}", "QLineEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }"]


        #Фон для Face id
        bagraound_label = QtGui.QLabel(self.main_panel)
        bagraound_label.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        bagraound_label.setGeometry(10,10,1339,380)

        #Регистрация Фейс айди
        label_registartion = QtGui.QLabel("Registration Face ID:",self.main_panel)
        label_registartion.setStyleSheet(settings_style_css[0])
        label_registartion.setGeometry(10,10,300,50)
        self.face_registration = QtGui.QPushButton("Registartion",self.main_panel)
        self.face_registration.setIcon(QtGui.QIcon('image/faceID_registration'))
        self.face_registration.setIconSize(QtCore.QSize(50,50))
        self.face_registration.setStyleSheet("QPushButton {background:transparent; border-radius: 10px; border: 2px solid #076CDA; font: 20px;}")
        self.face_registration.setGeometry(40,70,250,50)
        
        #Использовать Face id для входа в БД
        label_db = QtGui.QLabel("Use Face ID to enter the database:",self.main_panel)
        label_db.setStyleSheet(settings_style_css[0])
        label_db.setGeometry(10,150,410,50)
        

        yes_label_db = QtGui.QLabel("Yes",self.main_panel)
        yes_label_db.setStyleSheet(settings_style_css[0])
        yes_label_db.setGeometry(15,210,80,30)

        self.db_faceid_button = QtGui.QPushButton(self.main_panel)
        self.db_faceid_button.setIcon(QtGui.QIcon('image/0.png'))
        self.db_faceid_button.setIconSize(QtCore.QSize(70,70))
        self.db_faceid_button.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; outline: none; }")
        self.db_faceid_button.setGeometry(100,210,70,35)

        false_label_db = QtGui.QLabel("False",self.main_panel)
        false_label_db.setStyleSheet(settings_style_css[0])
        false_label_db.setGeometry(170,205,100,40)
        
        
        #Использование фейс айди для входа в приложение
        label_log = QtGui.QLabel("Using face id to enter the application:",self.main_panel)
        label_log.setStyleSheet(settings_style_css[0])
        label_log.setGeometry(10,260,440,50)
        
        yes_label_log = QtGui.QLabel("Yes",self.main_panel)
        yes_label_log.setStyleSheet(settings_style_css[0])
        yes_label_log.setGeometry(15,320,80,30)

        self.log_button_face = QtGui.QPushButton(self.main_panel)
        self.log_button_face.setIcon(QtGui.QIcon('image/0.png'))
        self.log_button_face.setIconSize(QtCore.QSize(70,70))
        self.log_button_face.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; outline: none; }")
        self.log_button_face.setGeometry(100,320,70,35)

        false_label_log = QtGui.QLabel("False",self.main_panel)
        false_label_log.setStyleSheet(settings_style_css[0])
        false_label_log.setGeometry(170,315,100,40)       
        
        #Фон для системных настроек 
        system_label = QtGui.QLabel(self.main_panel)
        system_label.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        system_label.setGeometry(10,392,664.5,445)

        #Светлая тема или темная
        label_theme = QtGui.QLabel("Theme:",system_label)
        label_theme.setStyleSheet(settings_style_css[0])
        label_theme.setGeometry(10,10,150,30)
        black_tema = QtGui.QLabel("Dark",system_label)
        black_tema.setStyleSheet(settings_style_css[0])
        black_tema.setGeometry(15,50,80,30)

        self.tema_button = QtGui.QPushButton(system_label)
        self.tema_button.setIcon(QtGui.QIcon('image/0.png'))
        self.tema_button.setIconSize(QtCore.QSize(70,70))
        self.tema_button.setStyleSheet("QPushButton {background:transparent; border-radius: 16px; outline: none; }")
        self.tema_button.setGeometry(110,50,70,35)

        theme_tema = QtGui.QLabel("Light",system_label)
        theme_tema.setStyleSheet(settings_style_css[0])
        theme_tema.setGeometry(176,45,90,40)

        #Язык системы 
        label_language = QtGui.QLabel("Language:",system_label)
        label_language.setStyleSheet(settings_style_css[0])
        label_language.setGeometry(15,100,150,50)

        self.combo_language = QtGui.QComboBox(system_label)
        self.combo_language.addItems(["English language", "Ukrainian language"])
        self.combo_language.setStyleSheet("QComboBox {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 18px; }")
        self.combo_language.setGeometry(168,113,250,30)

        #Фон для технічної підтримки
        label_tehn = QtGui.QLabel(self.main_panel)
        label_tehn.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}") 
        label_tehn.setGeometry(676,392,672,445)
        
        label_podderjka = QtGui.QLabel("Technical support:",label_tehn)
        label_podderjka.setStyleSheet(settings_style_css[0])
        label_podderjka.setGeometry(1,1,250,50)
        label_mail_tehn = QtGui.QLabel("Gmail:",label_tehn)
        label_mail_tehn.setStyleSheet(settings_style_css[0])
        label_mail_tehn.setGeometry(20,52,100,50)
        
        self.mail_edit_tehn = QtGui.QLineEdit(label_tehn)
        self.mail_edit_tehn.setStyleSheet(settings_style_css[1])
        self.mail_edit_tehn.setGeometry(130,63,400,30)

        label_text = QtGui.QLabel("Message:",label_tehn)
        label_text.setStyleSheet(settings_style_css[0])
        label_text.setGeometry(20,110,150,50)

        self.message_edit = QtGui.QTextEdit(label_tehn)
        self.message_edit.setStyleSheet("QTextEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }")
        self.message_edit.setGeometry(40,170,605,200)

        self.enter_button = QtGui.QPushButton('Send a message', label_tehn)
        self.enter_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.enter_button.setGeometry(450,380,200,50)

        

        #DB panel  
        self.db_panel = QtGui.QLabel(self)
        self.db_panel.setVisible(False)
        self.db_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.db_panel.setGeometry(243,53,1357,847)
        
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
        self.log_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;}")
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
        self.db_panel_function.setGeometry(243,53,1357,847)

        db_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 25px;}", "QLineEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }"]

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
        label_znach.setStyleSheet(db_style_css[0])
        label_znach.setGeometry(725,20,200,50)

        self.poiskEdit = QtGui.QLineEdit(self.table_user_panel)
        self.poiskEdit.setStyleSheet(db_style_css[1])
        self.poiskEdit.setGeometry(770,90,450,35)
        self.poiskEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.poisk_button = QtGui.QPushButton('Search', self.table_user_panel)
        self.poisk_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;} QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.poisk_button.setGeometry(1150,150,160,50)


        label_image = QtGui.QLabel(self.table_user_panel)
        pixmap = QtGui.QPixmap('image/line.png')
        label_image.setPixmap(pixmap)
        label_image.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        label_image.setGeometry(715,200,600,50)

        #Добавление данных в таблицу user
        label_name = QtGui.QLabel("Name:",self.table_user_panel)
        label_name.setStyleSheet(db_style_css[0])
        label_name.setGeometry(725,250,150,50)

        self.nameEdit = QtGui.QLineEdit(self.table_user_panel)
        self.nameEdit.setStyleSheet(db_style_css[1])
        self.nameEdit.setGeometry(880,258,300,30)
        self.nameEdit.setAlignment(QtCore.Qt.AlignCenter)


        label_lastname = QtGui.QLabel("Lastname:",self.table_user_panel)
        label_lastname.setStyleSheet(db_style_css[0])
        label_lastname.setGeometry(725,310,150,50)

        self.lastnameEdit = QtGui.QLineEdit(self.table_user_panel)
        self.lastnameEdit.setStyleSheet(db_style_css[1])
        self.lastnameEdit.setGeometry(880,318,300,30)
        self.lastnameEdit.setAlignment(QtCore.Qt.AlignCenter)

        label_gmail = QtGui.QLabel("Gmail:",self.table_user_panel)
        label_gmail.setStyleSheet(db_style_css[0])
        label_gmail.setGeometry(725,370,150,50)

        self.gmailEdit = QtGui.QLineEdit(self.table_user_panel)
        self.gmailEdit.setStyleSheet(db_style_css[1])
        self.gmailEdit.setGeometry(880,378,300,30)
        self.gmailEdit.setAlignment(QtCore.Qt.AlignCenter)

        label_password = QtGui.QLabel("Password:",self.table_user_panel)
        label_password.setStyleSheet(db_style_css[0])
        label_password.setGeometry(725,430,150,50)

        self.passEdit = QtGui.QLineEdit(self.table_user_panel)
        self.passEdit.setStyleSheet(db_style_css[1])
        self.passEdit.setGeometry(880,438,300,30)
        self.passEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.add_button = QtGui.QPushButton('Add data', self.table_user_panel)
        self.add_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;} QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.add_button.setGeometry(1150,500,160,50)


        label_image1 = QtGui.QLabel(self.table_user_panel)
        pixmap1 = QtGui.QPixmap('image/line.png')
        label_image1.setPixmap(pixmap1)
        label_image1.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        label_image1.setGeometry(715,550,600,50)

        #Удаление с таблицы user
        label_znach_del = QtGui.QLabel("Enter value:",self.table_user_panel)
        label_znach_del.setStyleSheet(db_style_css[0])
        label_znach_del.setGeometry(725,600,170,50)

        self.delEdit = QtGui.QLineEdit(self.table_user_panel)
        self.delEdit.setStyleSheet(db_style_css[1])
        self.delEdit.setGeometry(900,608,350,35)
        self.delEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.del_button = QtGui.QPushButton('Delete', self.table_user_panel)
        self.del_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;} QPushButton:hover {background:#076CDA;font-weight: bold;}")
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
        self.foto_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; margin: 5px}")
        self.foto_panel.setGeometry(243,53,1357,847)

        foto_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 25px;}", "QLineEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }"]
        #Панель для функционала для распознование обьктов на фото 
        panel_foto_detection = QtGui.QLabel(self.foto_panel)


        label_foto_model = QtGui.QLabel("Model Path:",panel_foto_detection)
        label_foto_model.setStyleSheet(foto_style_css[0])
        label_foto_model.setGeometry(10,20,150,50)
        

        self.foto_modelEdit = QtGui.QLineEdit(panel_foto_detection)
        self.foto_modelEdit.setStyleSheet(foto_style_css[1])
        self.foto_modelEdit.setGeometry(200,28,1050,35)
        self.foto_modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_modelEdit.setText("/home/pproger/Desktop/yolo-object-detection/yolo-coco")

        self.file_open_button_f1 = QtGui.QPushButton(panel_foto_detection)
        self.file_open_button_f1.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_f1.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_f1.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_f1.setGeometry(1260,24,40,40)

        label_foto_image = QtGui.QLabel("Input_image:",panel_foto_detection)
        label_foto_image .setStyleSheet(foto_style_css[0])
        label_foto_image .setGeometry(10,100,165,50)

        self.foto_imageEdit = QtGui.QLineEdit(panel_foto_detection)
        self.foto_imageEdit.setStyleSheet(foto_style_css[1])
        self.foto_imageEdit.setGeometry(200,108,1050,35)
        self.foto_imageEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_imageEdit.setText("/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/images/dining_table.jpg")

        self.file_open_button_f2 = QtGui.QPushButton(panel_foto_detection)
        self.file_open_button_f2.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_f2.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_f2.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_f2.setGeometry(1260,104,40,40)

        label_foto_image_out = QtGui.QLabel("Output_image:",panel_foto_detection)
        label_foto_image_out .setStyleSheet(foto_style_css[0])
        label_foto_image_out.setGeometry(10,180,190,50)

        self.foto_image_outEdit = QtGui.QLineEdit(panel_foto_detection)
        self.foto_image_outEdit.setStyleSheet(foto_style_css[1])
        self.foto_image_outEdit.setGeometry(200,188,1050,35)
        self.foto_image_outEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_image_outEdit.setText("/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/output/imagenew.jpg")

        self.file_open_button_f3 = QtGui.QPushButton(panel_foto_detection)
        self.file_open_button_f3.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_f3.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_f3.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_f3.setGeometry(1260,184,40,40)

        self.foto_detection_button = QtGui.QPushButton('Detection Object', panel_foto_detection)
        self.foto_detection_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.foto_detection_button.setGeometry(760,250,540,50)

        label_foto_model = QtGui.QLabel("Object:",panel_foto_detection)
        label_foto_model.setStyleSheet(foto_style_css[0])
        label_foto_model.setGeometry(10,290,100,50)

        self.object_list_foto_1 = QtGui.QPlainTextEdit(panel_foto_detection)
        self.object_list_foto_1.setStyleSheet("QPlainTextEdit {background:#222528;color:#FBFBFC; border: 2px solid #222528; font: 20px}")
        self.object_list_foto_1.setGeometry(10,350,1208,390)
        #self.object_list_foto.setPlainText(":13298123")

        style_panel_foto = "QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#222528;}"
        self.folder_open_button = QtGui.QPushButton(panel_foto_detection)
        self.folder_open_button.setStyleSheet(style_panel_foto)
        self.folder_open_button.setIcon(QtGui.QIcon('image/folder_open.png'))
        self.folder_open_button.setIconSize(QtCore.QSize(72,72))
        self.folder_open_button.setGeometry(1235,340,72,72)

        self.folder_dowladon_button = QtGui.QPushButton(panel_foto_detection)
        self.folder_dowladon_button.setStyleSheet(style_panel_foto)
        self.folder_dowladon_button.setIcon(QtGui.QIcon('image/folder_dowladon.png'))
        self.folder_dowladon_button.setIconSize(QtCore.QSize(72,72))
        self.folder_dowladon_button.setGeometry(1235,420,72,72)

        self.folder_db_save_button = QtGui.QPushButton(panel_foto_detection)
        self.folder_db_save_button.setStyleSheet(style_panel_foto)
        self.folder_db_save_button.setIcon(QtGui.QIcon('image/folder_db_save.png'))
        self.folder_db_save_button.setIconSize(QtCore.QSize(55,55))
        self.folder_db_save_button.setGeometry(1235,500,72,72)

        self.folder_file_save_button = QtGui.QPushButton(panel_foto_detection)
        self.folder_file_save_button.setStyleSheet(style_panel_foto)
        self.folder_file_save_button.setIcon(QtGui.QIcon('image/folder_file_save.png'))
        self.folder_file_save_button.setIconSize(QtCore.QSize(72,72))
        self.folder_file_save_button.setGeometry(1235,580,72,72)

        self.prikrep_file_button = QtGui.QPushButton(panel_foto_detection)
        self.prikrep_file_button.setStyleSheet(style_panel_foto)
        self.prikrep_file_button.setIcon(QtGui.QIcon('image/graph.png'))
        self.prikrep_file_button.setIconSize(QtCore.QSize(62,72))
        self.prikrep_file_button.setGeometry(1235,660,72,72)

        # tool box
        tool_box = QtGui.QToolBox()
        tool_box.setStyleSheet("QToolBox {background:#292E33; border-radius: 5px}")

        # items
        tool_box.addItem(panel_foto_detection,
                         'Detection Object to Foto')
        tool_box.addItem(QtGui.QPlainTextEdit('Text 2'),
                         'Page 2')
       
        
        vlayout = QtGui.QVBoxLayout(self.foto_panel)
        vlayout.addWidget(tool_box)
        self.foto_panel.setLayout(vlayout)


        #Video panel  
        self.video_panel = QtGui.QLabel(self)
        self.video_panel.setVisible(False)
        self.video_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.video_panel.setGeometry(243,53,1357,847)


        label_video_model = QtGui.QLabel("Model Path:",self.video_panel)
        label_video_model.setStyleSheet(foto_style_css[0])
        label_video_model.setGeometry(10,20,170,50)
        

        self.video_modelEdit = QtGui.QLineEdit(self.video_panel)
        self.video_modelEdit.setStyleSheet(foto_style_css[1])
        self.video_modelEdit.setGeometry(210,28,1050,35)
        self.video_modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.video_modelEdit.setText("/home/pproger/Desktop/machine_learning_python/video_obcject/yolo-coco")

        self.file_open_button_v1 = QtGui.QPushButton(self.video_panel)
        self.file_open_button_v1.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_v1.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_v1.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_v1.setGeometry(1280,24,40,40)

        label_video_image = QtGui.QLabel("Input_video:",self.video_panel)
        label_video_image .setStyleSheet(foto_style_css[0])
        label_video_image .setGeometry(10,100,190,50)

        self.video_inputEdit = QtGui.QLineEdit(self.video_panel)
        self.video_inputEdit.setStyleSheet(foto_style_css[1])
        self.video_inputEdit.setGeometry(210,108,1050,35)
        self.video_inputEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.video_inputEdit.setText("/home/pproger/Desktop/machine_learning_python/video_obcject/videos/overpass.mp4")

        self.file_open_button_v2 = QtGui.QPushButton(self.video_panel)
        self.file_open_button_v2.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_v2.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_v2.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_v2.setGeometry(1280,104,40,40)

        label_video_image_out = QtGui.QLabel("Output_video:",self.video_panel)
        label_video_image_out .setStyleSheet(foto_style_css[0])
        label_video_image_out.setGeometry(10,180,200,50)

        self.video_outEdit = QtGui.QLineEdit(self.video_panel)
        self.video_outEdit.setStyleSheet(foto_style_css[1])
        self.video_outEdit.setGeometry(210,188,1050,35)
        self.video_outEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.video_outEdit.setText("/home/pproger/Desktop/machine_learning_python/video_obcject/output/overpass.avi")

        self.file_open_button_v3 = QtGui.QPushButton(self.video_panel)
        self.file_open_button_v3.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_v3.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_v3.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_v3.setGeometry(1280,184,40,40)

        label_frames_per_second = QtGui.QLabel("Frames_per_second:",self.video_panel)
        label_frames_per_second.setStyleSheet(foto_style_css[0])
        label_frames_per_second.setGeometry(10,260,270,50)

        self.frames_per_secondEdit = QtGui.QLineEdit(self.video_panel)
        self.frames_per_secondEdit.setStyleSheet(foto_style_css[1])
        self.frames_per_secondEdit.setGeometry(280,268,400,35)
        self.frames_per_secondEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.frames_per_secondEdit.setText("30")

        self.video_detection_button = QtGui.QPushButton('Detection Object', self.video_panel)
        self.video_detection_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.video_detection_button.setGeometry(760,260,550,50)


        label_foto_model = QtGui.QLabel("Neural Network Process:",self.video_panel)
        label_foto_model.setStyleSheet(foto_style_css[0])
        label_foto_model.setGeometry(10,330,350,50)

        
        self.object_list_video = QtGui.QPlainTextEdit(self.video_panel)
        self.object_list_video.setStyleSheet("QPlainTextEdit {background:#222528;color:#FBFBFC; border: 2px solid #222528; font: 20px}")
        self.object_list_video.setGeometry(30,400,1208,420)

        self.openfolder_video_button = QtGui.QPushButton(self.video_panel)
        self.openfolder_video_button.setStyleSheet(style_panel_foto)
        self.openfolder_video_button.setIcon(QtGui.QIcon('image/folder_open.png'))
        self.openfolder_video_button.setIconSize(QtCore.QSize(72,72))
        self.openfolder_video_button.setGeometry(1250,400,72,72)

        self.folder_dowladonVideo_button = QtGui.QPushButton(self.video_panel)
        self.folder_dowladonVideo_button.setStyleSheet(style_panel_foto)
        self.folder_dowladonVideo_button.setIcon(QtGui.QIcon('image/folder_dowladon.png'))
        self.folder_dowladonVideo_button.setIconSize(QtCore.QSize(72,72))
        self.folder_dowladonVideo_button.setGeometry(1250,485,72,72)

        self.open_video_button_input = QtGui.QPushButton(self.video_panel)
        self.open_video_button_input.setStyleSheet(style_panel_foto)
        self.open_video_button_input.setIcon(QtGui.QIcon('image/open_video_output.png'))
        self.open_video_button_input.setIconSize(QtCore.QSize(72,72))
        self.open_video_button_input.setGeometry(1250,570,72,72)

        self.open_video_button_output = QtGui.QPushButton(self.video_panel)
        self.open_video_button_output.setStyleSheet(style_panel_foto)
        self.open_video_button_output.setIcon(QtGui.QIcon('image/open_video_input.png'))
        self.open_video_button_output.setIconSize(QtCore.QSize(72,72))
        self.open_video_button_output.setGeometry(1250,655,72,72)





        #Cam panel  
        self.cam_panel = QtGui.QLabel(self)
        self.cam_panel.setVisible(False)
        self.cam_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.cam_panel.setGeometry(243,53,1357,847)  

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
        self.putyEdit.setGeometry(155,108,450,35)
        self.putyEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.putyEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/dataset/")
        
        self.file_open_button_cam1 = QtGui.QPushButton(self.cam_panel)
        self.file_open_button_cam1.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_cam1.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_cam1.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_cam1.setGeometry(615,104,40,40)

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
        self.Face_dataset_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
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
        self.path_trainingEdit.setGeometry(200,298,790,35)
        self.path_trainingEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.path_trainingEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/dataset")

        self.file_open_button_cam2 = QtGui.QPushButton(self.cam_panel)
        self.file_open_button_cam2.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_cam2.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_cam2.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_cam2.setGeometry(1000,294,40,40)

        label_model = QtGui.QLabel("Save the model into:",self.cam_panel)
        label_model.setStyleSheet(str_style_css[0])
        label_model.setGeometry(10,370,260,50)

        self.modelEdit = QtGui.QLineEdit(self.cam_panel)
        self.modelEdit.setStyleSheet(str_style_css[1])
        self.modelEdit.setGeometry(280,378,710,35)
        self.modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modelEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/trainer/trainer.yml")

        self.file_open_button_cam3 = QtGui.QPushButton(self.cam_panel)
        self.file_open_button_cam3.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_cam3.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_cam3.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_cam3.setGeometry(1000,374,40,40)

        self.Face_training_button = QtGui.QPushButton('Face training', self.cam_panel)
        self.Face_training_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
        self.Face_training_button.setGeometry(500,450,540,50)

        #Распознование лица
        label_path_model = QtGui.QLabel("Path to training:",self.cam_panel)
        label_path_model.setStyleSheet(str_style_css[0])
        label_path_model.setGeometry(10,560,237,50)

        self.path_modelEdit = QtGui.QLineEdit(self.cam_panel)
        self.path_modelEdit.setStyleSheet(str_style_css[1])
        self.path_modelEdit.setGeometry(230,568,760,35)
        self.path_modelEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.path_modelEdit.setText("/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/trainer/trainer.yml")

        self.file_open_button_cam4 = QtGui.QPushButton(self.cam_panel)
        self.file_open_button_cam4.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_cam4.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_cam4.setIconSize(QtCore.QSize(45,45))
        self.file_open_button_cam4.setGeometry(1000,564,40,40)

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
        self.Face_recognition_button.setStyleSheet("QPushButton {background:#076CDA; border-radius: 5px; border: 2px solid #076CDA; font: 20px;outline: none; } QPushButton:hover {background:#076CDA;font-weight: bold;}")
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
        

    
        
        layout = QtGui.QVBoxLayout(self.tree_panel)
        layout.addWidget(self.treeView)


        #StatusBar настройкa
        self.label_status_message = QtGui.QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t         Successfully work all the functions")
        label_layout_version = QtGui.QLabel("  Version 1.1.0")
        
        
        
        self.connect_function_button = QtGui.QPushButton()
        self.connect_function_button.setStyleSheet("QPushButton {background:#076CDA; border: 1px solid #076CDA;outline: none;} QPushButton:hover {background:#1F8AD2}")
        self.connect_function_button.setIcon(QtGui.QIcon('image/connect.png'))
        self.connect_function_button.setIconSize(QtCore.QSize(20,20))
        
       
        self.statusBar.addWidget(label_layout_version)
        self.statusBar.addWidget(self.connect_function_button)

        self.statusBar.addWidget(self.label_status_message)

        #Plagins panel  
        self.Plagins_panel = QtGui.QLabel(self)
        self.Plagins_panel.setVisible(False)
        self.Plagins_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 5px; padding-left: 10px; margin: 5px}")
        self.Plagins_panel.setGeometry(243,53,1357,847)

        #Cловарь для поиска плагина
        model_plag = QtGui.QStringListModel()
        model_plag.setStringList(['Face ID', 'Face', 'fluorography', 'foto detection', 'video detection','removal of unnecessary objects from a photo', 'del','removal of excess objects','voice assistant','Voice','Assistant','with black and white photos in color','photos in color'])

        completer_plag = QtGui.QCompleter()
        completer_plag.setModel(model_plag)

        
        
        #Сам поиск 
        self.lineedit_plagin = QtGui.QLineEdit(self.Plagins_panel)
        self.lineedit_plagin.setCompleter(completer_plag)
        self.lineedit_plagin.setStyleSheet("QLineEdit {background:#222528; border-radius: 10px; font: 18px;}")
        self.lineedit_plagin.setGeometry(27,30,1300,45)
        self.lineedit_plagin.setAlignment(QtCore.Qt.AlignCenter)

        self.scrollArea = QtGui.QScrollArea(self.Plagins_panel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setGeometry(27,100,1300,720)
        self.verticalLayoutScroll = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)

        

       
        #Плагин Face ID
        self.plagins_function_face = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_face.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_face.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_face)

        image_plugins_face = QtGui.QLabel(self.plagins_function_face)
        pixmap1 = QtGui.QPixmap('image/face_plugins.png')
        image_plugins_face.setPixmap(pixmap1)
        image_plugins_face.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_face.setGeometry(5,5,95,90)

        plugin_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 20px;}", "QLineEdit {background:#222528;color:#FBFBFC; font: 16px; border: 2px solid #222528; font: 20px; }"]
        text_plugin_label_face = QtGui.QLabel('Face ID - a scanner of the three-dimensional shape of a person’s face. Used to identify a person.',self.plagins_function_face)
        text_plugin_label_face.setStyleSheet(plugin_style_css[0])
        text_plugin_label_face.setGeometry(120,5,900,90)

        self.plugins_face = QtGui.QPushButton('Add plugin',self.plagins_function_face)
        self.plugins_face.setStyleSheet(style_button)
        self.plugins_face.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_face.setIconSize(QtCore.QSize(30,30))
        self.plugins_face.setGeometry(1050,20,200,60)

        #Плагин Идентификации боле ли человек на туберкулез
        self.plagins_function_flugo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_flugo.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_flugo.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_flugo)

        image_plugins_flugo = QtGui.QLabel(self.plagins_function_flugo)
        pixmap2 = QtGui.QPixmap('image/flugo1.png')
        image_plugins_flugo.setPixmap(pixmap2)
        image_plugins_flugo.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_flugo.setGeometry(5,5,95,90)

        
        text_plugin_label_flugo = QtGui.QLabel('Fluorography is an X-ray examination that involves photographing an image of a fluorescent screen.',self.plagins_function_flugo)
        text_plugin_label_flugo.setStyleSheet(plugin_style_css[0])
        text_plugin_label_flugo.setGeometry(120,5,900,90)

        self.plugins_flugo = QtGui.QPushButton('Add plugin',self.plagins_function_flugo)
        self.plugins_flugo.setStyleSheet(style_button)
        self.plugins_flugo.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_flugo.setIconSize(QtCore.QSize(30,30))
        self.plugins_flugo.setGeometry(1050,20,200,60)


        #Плагин переобразование с чорнобелой фотографии в цветную
        self.plagins_function_foto = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_foto.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_foto.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_foto)

        image_plugins_foto = QtGui.QLabel(self.plagins_function_foto)
        pixmap3 = QtGui.QPixmap('image/foto_plagin.png')
        image_plugins_foto.setPixmap(pixmap3)
        image_plugins_foto.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_foto.setGeometry(5,5,95,90)

        
        text_plugin_label_foto = QtGui.QLabel('Automatically convert a black and white photo into a color photo using a neural network.',self.plagins_function_foto)
        text_plugin_label_foto.setStyleSheet(plugin_style_css[0])
        text_plugin_label_foto.setGeometry(120,5,900,90)

        self.plugins_foto = QtGui.QPushButton('Add plugin',self.plagins_function_foto)
        self.plugins_foto.setStyleSheet(style_button)
        self.plugins_foto.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_foto.setIconSize(QtCore.QSize(30,30))
        self.plugins_foto.setGeometry(1050,20,200,60)



        #Плагин удаления не нужных элементов с фото
        self.plagins_function_foto_del = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_foto_del.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_foto_del.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_foto_del)

        image_plugins_foto_del = QtGui.QLabel(self.plagins_function_foto_del)
        pixmap4 = QtGui.QPixmap('image/foto_del_im.png')
        image_plugins_foto_del.setPixmap(pixmap4)
        image_plugins_foto_del.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_foto_del.setGeometry(5,5,95,90)

        
        text_plugin_label_foto_del = QtGui.QLabel('Automatic removal of unnecessary elements from the photo.',self.plagins_function_foto_del)
        text_plugin_label_foto_del.setStyleSheet(plugin_style_css[0])
        text_plugin_label_foto_del.setGeometry(120,5,900,90)

        self.plugins_foto_del = QtGui.QPushButton('Add plugin',self.plagins_function_foto_del)
        self.plugins_foto_del.setStyleSheet(style_button)
        self.plugins_foto_del.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_foto_del.setIconSize(QtCore.QSize(30,30))
        self.plugins_foto_del.setGeometry(1050,20,200,60)



        #Плагин обнаружение обьктов на фото 
        self.plagins_function_foto_detection = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_foto_detection.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_foto_detection.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_foto_detection)

        image_plugins_foto_detection = QtGui.QLabel(self.plagins_function_foto_detection)
        pixmap5 = QtGui.QPixmap('image/plagin_foto_detection.png')
        image_plugins_foto_detection.setPixmap(pixmap5)
        image_plugins_foto_detection.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_foto_detection.setGeometry(5,5,95,90)

        
        text_plugin_label_foto_detection = QtGui.QLabel('Detecting objects in a photo using a neural network.',self.plagins_function_foto_detection)
        text_plugin_label_foto_detection.setStyleSheet(plugin_style_css[0])
        text_plugin_label_foto_detection.setGeometry(120,5,900,90)

        self.plugins_foto_detection = QtGui.QPushButton('Add plugin',self.plagins_function_foto_detection)
        self.plugins_foto_detection.setStyleSheet(style_button)
        self.plugins_foto_detection.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_foto_detection.setIconSize(QtCore.QSize(30,30))
        self.plugins_foto_detection.setGeometry(1050,20,200,60)


        #Плагин обнаружение обьктов на видео
        self.plagins_function_video_detection = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_video_detection.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_video_detection.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_video_detection)

        image_plugins_video_detection = QtGui.QLabel(self.plagins_function_video_detection)
        pixmap6 = QtGui.QPixmap('image/plugin_video_detection.png')
        image_plugins_video_detection.setPixmap(pixmap6)
        image_plugins_video_detection.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_video_detection.setGeometry(5,5,95,90)

        
        text_plugin_label_video_detection = QtGui.QLabel('Detecting objects in a video using a neural network.',self.plagins_function_video_detection)
        text_plugin_label_video_detection.setStyleSheet(plugin_style_css[0])
        text_plugin_label_video_detection.setGeometry(120,5,900,90)

        self.plugins_video_detection = QtGui.QPushButton('Add plugin',self.plagins_function_video_detection)
        self.plugins_video_detection.setStyleSheet(style_button)
        self.plugins_video_detection.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_video_detection.setIconSize(QtCore.QSize(30,30))
        self.plugins_video_detection.setGeometry(1050,20,200,60)


        #Плагин голосовой асистент
        self.plagins_function_voice = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.plagins_function_voice.setStyleSheet("QLabel {background:#292E33; border: 1px solid #1F2327; border-radius: 2px;} QLabel:hover {border: 4px solid #1F2327;}")
        self.plagins_function_voice.setMinimumHeight(100)

       

        self.verticalLayoutScroll.addWidget(self.plagins_function_voice)

        image_plugins_voice = QtGui.QLabel(self.plagins_function_voice)
        pixmap7 = QtGui.QPixmap('image/plugin_micro.png')
        image_plugins_voice.setPixmap(pixmap7)
        image_plugins_voice.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33;}")
        image_plugins_voice.setGeometry(5,5,95,90)

        
        text_plugin_label_voice = QtGui.QLabel('Voice assistant for computer control.',self.plagins_function_voice)
        text_plugin_label_voice.setStyleSheet(plugin_style_css[0])
        text_plugin_label_voice.setGeometry(120,5,900,90)

        self.plugins_voice = QtGui.QPushButton('Add plugin',self.plagins_function_voice)
        self.plugins_voice.setStyleSheet(style_button)
        self.plugins_voice.setIcon(QtGui.QIcon('image/add_plugin.png'))
        self.plugins_voice.setIconSize(QtCore.QSize(30,30))
        self.plugins_voice.setGeometry(1050,20,200,60)



        

        #Voise Assistant panel  
        self.voise_assistant_panel = QtGui.QLabel(self)
        #self.voise_assistant_panel.setVisible(False)
        self.voise_assistant_panel.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; border-radius: 5px;  margin: 5px}")
        self.voise_assistant_panel.setGeometry(243,53,1357,847)

        self.label_fon_assistant = QtGui.QLabel(self.voise_assistant_panel)
        self.label_fon_assistant.setStyleSheet("QLabel {background:#1F2327; border: 1px solid #1F2327; border-radius: 10px;  margin: 5px}")
        self.label_fon_assistant.setGeometry(77,700,1200,100)

        self.microfon_function_button = QtGui.QPushButton(self.label_fon_assistant)
        self.microfon_function_button.setStyleSheet("QPushButton {background:#1F2327; border: 1px solid #1F2327;outline: none;} QPushButton:hover {background:#1F2327; border: 2px solid #292E33}")
        self.microfon_function_button.setIcon(QtGui.QIcon('image/mic.png'))
        self.microfon_function_button.setIconSize(QtCore.QSize(72,72))
        self.microfon_function_button.setGeometry(560,20,72,72)

        self.assistant_list = QtGui.QPlainTextEdit(self.voise_assistant_panel)
        self.assistant_list.setStyleSheet("QPlainTextEdit {background:#1F2327; color:#FBFBFC; border: 2px solid #1F2327; border-radius: 5px; font: 20px}")
        self.assistant_list.setGeometry(77,50,1200,590)





        #Панель конекта с базой данных
        self.connect_db_panel = QtGui.QLabel(self)
        self.connect_db_panel.setVisible(False)
        self.connect_db_panel.setStyleSheet("QLabel {background:#292E33; border: 2px solid #1F2327; border-radius: 5px; margin: 5px}")
        self.connect_db_panel.setGeometry(105,618,400,300)

        self.exit_connect_db_button = QtGui.QPushButton(self.connect_db_panel)
        self.exit_connect_db_button.setStyleSheet(style_panel_foto)
        self.exit_connect_db_button.setIcon(QtGui.QIcon('image/close.png'))
        self.exit_connect_db_button.setIconSize(QtCore.QSize(22,22))
        self.exit_connect_db_button.setGeometry(365,15,20,20)

        self.been_label_ = QtGui.QLabel("Database Connection",self.connect_db_panel)
        self.been_label_.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; font:20px; color: #6D6F72;}")
        self.been_label_.setGeometry(10,10,250,40)

        connect_style_css = ["QLabel {background:#292E33; border: 1px solid #292E33; color: #6D6F72; font: 18px;}", "QLineEdit {background:#222528;color:#FBFBFC; border: 2px solid #222528; font: 16px; }"]
        label_path_training = QtGui.QLabel("Database path:",self.connect_db_panel)
        label_path_training.setStyleSheet(connect_style_css[0])
        label_path_training.setGeometry(10,60,150,50)

        self.path_trainingEdit = QtGui.QLineEdit(self.connect_db_panel)
        self.path_trainingEdit.setStyleSheet(connect_style_css[1])
        self.path_trainingEdit.setGeometry(150,75,180,25)
        self.path_trainingEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.path_trainingEdit.setText("logo.db")

        self.file_open_button_db = QtGui.QPushButton(self.connect_db_panel)
        self.file_open_button_db.setStyleSheet("QPushButton {background:#292E33; border: 1px solid #292E33;outline: none;} QPushButton:hover {background:#1F2327;}")
        self.file_open_button_db.setIcon(QtGui.QIcon('image/file_open_dialog.png'))
        self.file_open_button_db.setIconSize(QtCore.QSize(35,35))
        self.file_open_button_db.setGeometry(345,68,40,40)

        self.connect_panel_button = QtGui.QPushButton("Restart",self.connect_db_panel)
        self.connect_panel_button.setStyleSheet("QPushButton {background:#007AFF; border: 1px solid #007AFF; border-radius: 2px;outline: none; } QPushButton:hover {background:#007AFF;font-weight: bold;}")
        self.connect_panel_button.setGeometry(15,130,360,34)

        self.check_label_ = QtGui.QLabel("Successful Connection",self.connect_db_panel)
        self.check_label_.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; font:20px; color: green}")
        self.check_label_.setGeometry(90,200,250,40)

        

        #Панель уведомлений
        self.been_panel = QtGui.QLabel(self)
        self.been_panel.setVisible(False)
        self.been_panel.setStyleSheet("QLabel {background:#292E33; border: 2px solid #1F2327; border-radius: 5px; margin: 5px}")
        self.been_panel.setGeometry(1270,50,300,500)

        self.exit_been_button = QtGui.QPushButton(self.been_panel)
        self.exit_been_button.setStyleSheet(style_panel_foto)
        self.exit_been_button.setIcon(QtGui.QIcon('image/close.png'))
        self.exit_been_button.setIconSize(QtCore.QSize(22,22))
        self.exit_been_button.setGeometry(265,15,20,20)

        self.been_label_ = QtGui.QLabel("Notification",self.been_panel)
        self.been_label_.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; font:20px; color: #6D6F72;}")
        self.been_label_.setGeometry(10,10,200,40)

        self.listWidget_u = QtGui.QListWidget(self.been_panel)
        self.listWidget_u.setStyleSheet("QListWidget {background:#292E33;border: 1px solid #292E33; font:16px}")
	
        #Resize width and height
        self.listWidget_u.setGeometry(10,50,280,410)
	 
        self.been_clear_button = QtGui.QPushButton("Сlear Notifications",self.been_panel)
        self.been_clear_button.setStyleSheet("QPushButton {background:#007AFF; border: 1px solid #007AFF; border-radius: 2px;outline: none; } QPushButton:hover {background:#007AFF;font-weight: bold;}")
        self.been_clear_button.setGeometry(10,465,280,25) 


        #Панель сообщений
        self.message_fun_panel = QtGui.QLabel(self)
        self.message_fun_panel.setVisible(False)
        self.message_fun_panel.setStyleSheet("QLabel {background:#292E33; border: 2px solid #1F2327; border-radius: 5px; margin: 5px}")
        self.message_fun_panel.setGeometry(775,50,500,400)

        self.exit_message_fun_button = QtGui.QPushButton(self.message_fun_panel)
        self.exit_message_fun_button.setStyleSheet(style_panel_foto)
        self.exit_message_fun_button.setIcon(QtGui.QIcon('image/close.png'))
        self.exit_message_fun_button.setIconSize(QtCore.QSize(22,22))
        self.exit_message_fun_button.setGeometry(465,15,20,20)

        self.message_label_ = QtGui.QLabel("Message",self.message_fun_panel)
        self.message_label_.setStyleSheet("QLabel {background:#292E33; border: 1px solid #292E33; font:20px; color: #6D6F72;}")
        self.message_label_.setGeometry(10,10,100,40)   

        self.listWidget = QtGui.QListWidget(self.message_fun_panel)
        self.listWidget.setStyleSheet("QListWidget {background:#292E33;border: 1px solid #292E33; font:17px;}")
	
        #Resize width and height
        self.listWidget.setGeometry(10,50,480,305)
	
        
        

        self.message_clear_button = QtGui.QPushButton("Clear Message",self.message_fun_panel)
        self.message_clear_button.setStyleSheet("QPushButton {background:#007AFF; border: 1px solid #007AFF; border-radius: 2px;outline: none; } QPushButton:hover {background:#007AFF;font-weight: bold;}")
        self.message_clear_button.setGeometry(10,360,480,30)

"""
app = QtGui.QApplication(sys.argv)
qb = QMain()

qb.show()
sys.exit(app.exec_())
"""



        
        




       
       
       



       

