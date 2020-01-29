#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore




class QMain(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(200, 200, 1600,900)
        self.setWindowTitle('Main')
        self.setWindowIcon(QtGui.QIcon('image/web.png'))
        #self.setFixedSize(400,600)


        
        
        

       


        



app = QtGui.QApplication(sys.argv)
qb = QMain()

qb.show()
sys.exit(app.exec_())
