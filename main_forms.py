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
        menu.setStyleSheet("QLabel {background:#808080; border: 1px solid #00FF00; border-radius: 10px; padding-left: 10px; margin: 5px}")
        menu.resize(250, 900)
       
        menu.setGeometry(0,0,250,900)

        style_button = "QPushButton {background:#696969; border-radius: 10px; border: 1px solid #D2691E;}"

        cam_button = QtGui.QPushButton('CAM', menu)
        cam_button.setStyleSheet(style_button)
        cam_button.setGeometry(25,100,200,100)




        video_button = QtGui.QPushButton('VIDEO', menu)
        video_button.setStyleSheet(style_button)
        video_button.setGeometry(25,250,200,100)



        foto_button = QtGui.QPushButton('FOTO', menu)
        foto_button.setStyleSheet(style_button)
        foto_button.setGeometry(25,400,200,100)




        db_button = QtGui.QPushButton('DB', menu)
        db_button.setStyleSheet(style_button)
        db_button.setGeometry(25,550,200,100)
        


        settings_button = QtGui.QPushButton('SETTINGS', menu)
        settings_button.setStyleSheet(style_button)
        settings_button.setGeometry(25,700,200,100)



        

        #grid = QtGui.QGridLayout()
        #self.setLayout(grid)
        #grid.addWidget(menu,1,1)

        
        #self.setFixedSize(400,600)


        
        
        

       


        



app = QtGui.QApplication(sys.argv)
qb = QMain()

qb.show()
sys.exit(app.exec_())
