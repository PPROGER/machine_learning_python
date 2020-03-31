#!/usr/bin/python

#Форма для голосовго помощника доработать 

import sys
from PyQt4 import QtGui, QtCore





class QVoice(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 400, 900)
        self.setWindowTitle('Voice Assistant')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        self.setFixedSize(400,900)
        #Картинка User
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/voice_bac.png')
        label_image.setPixmap(pixmap)
        #label_image.setStyleSheet("QLabel {background: rgba(255, 85, 127, 80);}")
        label_image.setGeometry(0,0,400,900)
        text_label = QtGui.QLabel("Hi", self)
        text_label.setStyleSheet("QLabel {background: transparent; color: black; font: 25px}")
        text_label.setGeometry(50, 150, 100,50)
        


app = QtGui.QApplication(sys.argv)
qb = QVoice()

qb.show()
sys.exit(app.exec_())
       


        


 
