import sys
import random
from PyQt4 import QtGui, QtCore
import cv2
import dlib
from skimage import io
from scipy.spatial import distance



from db_connect import con
from login import Qlogin
from registration import QRegistration
from recovery import QRecovery
from face_id.cam import Cam
from face_id.face_detector import Face_detector


    
   


def log_avtorization():
    log_number = False
    cur = con.cursor()
    if(qb.loginEdit.text()!= "" and qb.passwordEdit.text() != ""):
        for row in cur.execute('SELECT Gmail,Password FROM user'):
            if(str(row[0]) == qb.loginEdit.text() and str(row[1]) == qb.passwordEdit.text()):
                qb.loginEdit.setText('')
                qb.passwordEdit.setText('')
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
                log_number = True
                forms_registration.show()
            
            
            
        if(log_number == False):
            QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login and password")       
              
    con.commit()

def faceid_avtorization():
    Cam()
    evklid_znach = Face_detector()
    if(float(evklid_znach) < 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
    elif(float(evklid_znach) > 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register through Face ID!")
        


def Registration_show():
    forms_registration.show()

def Recovery_show():
    forms_recovery.show()

def Registration_user():
    cur = con.cursor()
    if(forms_registration.nameEdit.text() !="" and forms_registration.firstnameEdit.text() != "" and forms_registration.mailEdit.text() != "" and forms_registration.passwordEdit.text() != ""):
        cur.execute('INSERT INTO user (id,Name,Firstname,Gmail,Password) VALUES (?,?,?,?,?)',(random.randint(1111,9999),forms_registration.nameEdit.text(),forms_registration.firstnameEdit.text(),forms_registration.mailEdit.text(),forms_registration.passwordEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nregistration!")
        forms_registration.nameEdit.setText("")
        forms_registration.firstnameEdit.setText("")
        forms_registration.mailEdit.setText("")
        forms_registration.passwordEdit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login, name and password")

    con.commit()    

def Recovery_user():
    cur = con.cursor()
    if(forms_recovery.firstnameEdit.text() != "" and forms_recovery.mailEdit.text() != "" and forms_recovery.passwordEdit.text() != ""):
        for row in cur.execute('SELECT Firstname,Gmail FROM user WHERE Firstname = ? and Gmail = ?',(forms_recovery.firstnameEdit.text(),forms_recovery.mailEdit.text())):
            if(str(row[0]) == forms_recovery.firstnameEdit.text() and str(row[1]) == forms_recovery.mailEdit.text() and str[2] == forms_recovery.passwordEdit.text()):
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","successfully changed password")

 
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter firstname, login and password")

    con.commit()
app = QtGui.QApplication(sys.argv)
qb = Qlogin()
forms_registration = QRegistration()
forms_recovery = QRecovery()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(log_avtorization))
qb.log_button.clicked.connect(log_avtorization)
qb.face_button.clicked.connect(faceid_avtorization)
qb.registration_button.clicked.connect(Registration_show)
qb.vostanovlenie_button.clicked.connect(Recovery_show)
forms_registration.registration_button.clicked.connect(Registration_user)
forms_recovery.registration_button.clicked.connect(Recovery_user)





qb.show()
sys.exit(app.exec_())




