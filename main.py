import sys
import random
from PyQt4 import QtGui, QtCore
import cv2
import dlib
from skimage import io
from scipy.spatial import distance
from datetime import datetime



from db_connect import con
from login import Qlogin
from registration import QRegistration
from recovery import QRecovery
from main_forms import QMain
from face_id.cam import Cam
from face_id.face_detector import Face_detector
from face_id.cam_registartion import Cam_registration


    
id_code = 0
#Поле ID пользователя
def log_avtorization():
    log_number = False
    cur = con.cursor()
    if(qb.loginEdit.text()!= "" and qb.passwordEdit.text() != ""):
        for row in cur.execute('SELECT Gmail,Password,id FROM user'):
            if(str(row[0]) == qb.loginEdit.text() and str(row[1]) == qb.passwordEdit.text()):
                global id_code
                id_code = str(row[2])
                qb.loginEdit.setText('')
                qb.passwordEdit.setText('')
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
                log_number = True
                load_main_forms()
                main_forms.show()
            
            
            
        if(log_number == False):
            QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login and password")       
              
    con.commit()

def faceid_avtorization():
    Cam()
    evklid_znach = Face_detector()
    if(float(evklid_znach) < 0.6):
        #QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
        main_forms.show()
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
            if(str(row[0]) == forms_recovery.firstnameEdit.text() and str(row[1]) == forms_recovery.mailEdit.text()):
                cur.execute('UPDATE user SET Password = ? WHERE Firstname = ? and Gmail = ?',(forms_recovery.passwordEdit.text(),forms_recovery.firstnameEdit.text(),forms_recovery.mailEdit.text()))
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","successfully changed password")
                forms_recovery.firstnameEdit.setText("")
                forms_recovery.mailEdit.setText("")
                forms_recovery.passwordEdit.setText("")
       

 
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter firstname, login and password")

    con.commit()




def Cam_function():
    main_forms.cam_panel.setVisible(True)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)  


def Vidoe_function():
    main_forms.video_panel.setVisible(True)
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False) 

def Foto_function():
    main_forms.foto_panel.setVisible(True)
    main_forms.video_panel.setVisible(False)
    main_forms.cam_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False) 

def Db_function():
    main_forms.db_panel.setVisible(True)
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.main_panel.setVisible(False) 

def Settings_function():
    main_forms.main_panel.setVisible(True) 
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
     

def Log_func_db():
    if(main_forms.loginEdit.text() == "123" and main_forms.passwordEdit.text() == "123"):

        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
        main_forms.db_panel.setVisible(False)
        main_forms.db_panel_function.setVisible(True)
        main_forms.loginEdit.setText("")
        main_forms.passwordEdit.setText("")
        DateTime()
        Load_data()

    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login and password") 


def Tema_Function():
    pass


def Message_function():
    cur = con.cursor()
    if(main_forms.mail_edit_tehn.text() !="" and main_forms.message_edit.toPlainText() != ""):
        cur.execute('INSERT INTO message (id_user,email,text) VALUES (?,?,?)',(id_code,main_forms.mail_edit_tehn.text(),main_forms.message_edit.toPlainText()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Message sent!")
        main_forms.mail_edit_tehn.setText("")
        main_forms.message_edit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message", "enter mail and message!")

    con.commit()    

#Регистрация Face_id
def Registration_face():
    Cam_registration()

def load_main_forms():
    cur = con.cursor()
    for row in cur.execute('SELECT Name,Firstname FROM user WHERE id = ? and id = ?',(id_code,id_code)):
        main_forms.FIO_label.setText(str(row[0]) + " " + str(row[1]))
    con.commit()


def Face_avtorization_db():
    Cam()
    evklid_znach = Face_detector()
    if(float(evklid_znach) < 0.6):
        #QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
        main_forms.db_panel.setVisible(False)
        main_forms.db_panel_function.setVisible(True)
        DateTime()
        Load_data()
    elif(float(evklid_znach) > 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register through Face ID!")


#Функция для вывода даты и времени
def DateTime():
    now = datetime.now()
    main_forms.label_datatime.setText(now.strftime("%x"))

#Функция загрузки данных из бд в таблицу
def Load_data():
    cur = con.cursor()
    for id_, Name, Firstname, Gmail, Password in con.execute("SELECT id, Name, Firstname, Gmail, Password FROM user"):
        row = main_forms.table_widget.rowCount()
        main_forms.table_widget.setRowCount(row + 1)

        main_forms.table_widget.setItem(row, 0, QtGui.QTableWidgetItem(str(id_)))
        main_forms.table_widget.setItem(row, 1, QtGui.QTableWidgetItem(Name))
        main_forms.table_widget.setItem(row, 2, QtGui.QTableWidgetItem(Firstname))
        main_forms.table_widget.setItem(row, 3, QtGui.QTableWidgetItem(Gmail))
        main_forms.table_widget.setItem(row, 4, QtGui.QTableWidgetItem(Password))
    con.commit()

#Функция удаление строк с таблицы на форме
def Delete_row_table():

    main_forms.table_widget.clearContents()
    main_forms.table_widget.setRowCount(0)
    


def Search_user():
    if(main_forms.poiskEdit.text() != ""):
        Delete_row_table()
        cur = con.cursor()
        for id_, Name, Firstname, Gmail, Password in con.execute("SELECT id, Name, Firstname, Gmail, Password FROM user WHERE id Like ? or Name Like ? or Firstname Like ? or Gmail Like ? or Password Like ?",(main_forms.poiskEdit.text(),main_forms.poiskEdit.text(),main_forms.poiskEdit.text(),main_forms.poiskEdit.text(),main_forms.poiskEdit.text())):
            row = main_forms.table_widget.rowCount()
            main_forms.table_widget.setRowCount(row + 1)

            main_forms.table_widget.setItem(row, 0, QtGui.QTableWidgetItem(str(id_)))
            main_forms.table_widget.setItem(row, 1, QtGui.QTableWidgetItem(Name))
            main_forms.table_widget.setItem(row, 2, QtGui.QTableWidgetItem(Firstname))
            main_forms.table_widget.setItem(row, 3, QtGui.QTableWidgetItem(Gmail))
            main_forms.table_widget.setItem(row, 4, QtGui.QTableWidgetItem(Password))
        con.commit()
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message", "enter value!")

def Add_user():
    cur = con.cursor()
    if(main_forms.nameEdit.text() !="" and main_forms.lastnameEdit.text() != "" and main_forms.gmailEdit.text() != "" and main_forms.passEdit.text() != ""):
        cur.execute('INSERT INTO user (id,Name,Firstname,Gmail,Password) VALUES (?,?,?,?,?)',(random.randint(1111,9999),main_forms.nameEdit.text(),main_forms.lastnameEdit.text(),main_forms.gmailEdit.text(),main_forms.passEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nregistration!")
        main_forms.nameEdit.setText("")
        main_forms.lastnameEdit.setText("")
        main_forms.gmailEdit.setText("")
        main_forms.passEdit.setText("")
        Delete_row_table()
        Load_data()
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter data")

    con.commit()

def Delete_user():
    cur = con.cursor()
    if(main_forms.delEdit.text() != ""):
        cur.execute("DELETE FROM user WHERE id Like ? or Name Like ? or Firstname Like ? or Gmail Like ? or Password Like ?",(main_forms.delEdit.text(),main_forms.delEdit.text(),main_forms.delEdit.text(),main_forms.delEdit.text(),main_forms.delEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\delete!")
        main_forms.delEdit.setText("")
        Delete_row_table()
        Load_data()
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter value")
    con.commit()

#Основная программа 
app = QtGui.QApplication(sys.argv)
qb = Qlogin()
forms_registration = QRegistration()
forms_recovery = QRecovery()
main_forms = QMain()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(log_avtorization))
qb.log_button.clicked.connect(log_avtorization)
qb.face_button.clicked.connect(faceid_avtorization)
qb.registration_button.clicked.connect(Registration_show)
qb.vostanovlenie_button.clicked.connect(Recovery_show)
forms_registration.registration_button.clicked.connect(Registration_user)
forms_recovery.registration_button.clicked.connect(Recovery_user)
main_forms.cam_button.clicked.connect(Cam_function)
main_forms.video_button.clicked.connect(Vidoe_function)
main_forms.foto_button.clicked.connect(Foto_function)
main_forms.db_button.clicked.connect(Db_function)
main_forms.settings_button.clicked.connect(Settings_function)
main_forms.log_button.clicked.connect(Log_func_db)
main_forms.tema_button.clicked.connect(Tema_Function)
main_forms.enter_button.clicked.connect(Message_function)
main_forms.face_registration.clicked.connect(Registration_face)
main_forms.face_button.clicked.connect(Face_avtorization_db)
main_forms.poisk_button.clicked.connect(Search_user)
main_forms.add_button.clicked.connect(Add_user)
main_forms.del_button.clicked.connect(Delete_user)




qb.show()
sys.exit(app.exec_())




