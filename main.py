import sys
from PyQt4 import QtGui, QtCore
import cv2
import dlib
from skimage import io
from scipy.spatial import distance


from db_connect import con
from login import Qlogin
from recovery import QRecovery
from face_id.cam import Cam
from face_id.face_detector import Face_detector

    
   


def log_avtorization():
    log_number = False
    cur = con.cursor()
    for row in cur.execute('SELECT Gmail,Password FROM user'):
        if(str(row[0]) == qb.loginEdit.text() and str(row[1]) == qb.passwordEdit.text()):
            qb.loginEdit.setText('')
            qb.passwordEdit.setText('')
            QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
            log_number = True
    if(log_number == False):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register")

            
              
    con.commit()

def faceid_avtorization():
    Cam()
    evklid_znach = Face_detector()
    if(float(evklid_znach) < 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
    elif(float(evklid_znach) > 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register through Face ID!")
        









app = QtGui.QApplication(sys.argv)
qb = Qlogin()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(log_avtorization))
qb.log_button.clicked.connect(log_avtorization)
qb.face_button.clicked.connect(faceid_avtorization)

qb.show()
sys.exit(app.exec_())



