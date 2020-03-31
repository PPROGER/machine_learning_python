#!/usr/bin/python


import sys
from PyQt4 import QtGui, QtCore





class QLoad(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(550, 320, 852, 480)
        
        self.setFixedSize(852, 480)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        label_image = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('image/maket1.jpg')
        label_image.setPixmap(pixmap)
        label_image.setGeometry(0,0,852, 480)
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(0, 400, 852, 30)



       


        


 
