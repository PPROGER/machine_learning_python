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

        FIO_label = QtGui.QLabel('Andrey Kornienko',profil_panel)
        FIO_label.setStyleSheet("QLabel {background:#808080; border: 1px solid #808080; border-radius: 1px; padding-left: 1px; margin: 6px}")
        FIO_label.setGeometry(80,0,181,60)



        
        
        



        



app = QtGui.QApplication(sys.argv)
qb = QMain()

qb.show()
sys.exit(app.exec_())
