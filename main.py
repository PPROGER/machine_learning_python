import sys
import os
import time
import shutil
from PIL import Image
import random
from PyQt4 import QtGui, QtCore
import cv2
import dlib
from skimage import io
from scipy.spatial import distance
from datetime import datetime
import numpy
import speech_recognition as sr
import platform



from db_connect import con
from login import Qlogin
from main_forms import QMain
from face_id.cam import Cam
from face_id.face_detector import Face_detector
from face_id.cam_registartion import Cam_registration
from load_form import QLoad
from FacialRecognitionProject.face_dataset import Face_datasets
from FacialRecognitionProject.face_training import Face_trainings
from FacialRecognitionProject.face_recognition import Face_recognitions
from FirstDetectionFoto.FirstDetection import FirstDetection
from video_obcject.main_video import Detection_object_video
from VoiceCommands.voice_commands import listen


    
id_code = 0
button_check = [True, True, True]
assistent_check = True
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
                qb.close()
            
            
            
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
        global id_code
        id_code = 4345;
        load_main_forms()
        main_forms.show()
        qb.close()
    elif(float(evklid_znach) > 0.6):
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please try again or register through Face ID!")
        

def Recovery_show():
    qb.panel_login_registration.setVisible(False)
    qb.panel_recovery.setVisible(True)

def Show_log_reg():
    qb.panel_recovery.setVisible(False)
    qb.panel_login_registration.setVisible(True)
    
def Registration_user():
    cur = con.cursor()
    if(qb.nameEdit.text() !="" and qb.firstnameEdit.text() != "" and qb.mailEdit.text() != "" and qb.password_Edit.text() != ""):
        cur.execute('INSERT INTO user (id,Name,Firstname,Gmail,Password) VALUES (?,?,?,?,?)',(random.randint(1111,9999),qb.nameEdit.text(),qb.firstnameEdit.text(),qb.mailEdit.text(),qb.password_Edit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nregistration!")
        qb.nameEdit.setText("")
        qb.firstnameEdit.setText("")
        qb.mailEdit.setText("")
        qb.password_Edit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login, name and password")

    con.commit()    

def Recovery_user():
    cur = con.cursor()
    if(qb.firstname__Edit.text() != "" and qb.mail__Edit.text() != "" and qb.password__Edit.text() != ""):
        for row in cur.execute('SELECT Firstname,Gmail FROM user WHERE Firstname = ? and Gmail = ?',(qb.firstname__Edit.text(),qb.mail__Edit.text())):
            if(str(row[0]) == qb.firstname__Edit.text() and str(row[1]) == qb.mail__Edit.text()):
                cur.execute('UPDATE user SET Password = ? WHERE Firstname = ? and Gmail = ?',(qb.password__Edit.text(),qb.firstname__Edit.text(),qb.mail__Edit.text()))
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","successfully changed password")
                qb.firstname__Edit.setText("")
                qb.mail__Edit.setText("")
                qb.password__Edit.setText("")
            else:
                QtGui.QMessageBox.about(QtGui.QWidget(),"Message","not user ")

       

 
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
    main_forms.Plagins_panel.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
    
    Load_cam_panel()  


def Vidoe_function():
    main_forms.video_panel.setVisible(True)
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
    

def Foto_function():
    main_forms.foto_panel.setVisible(True)
    main_forms.video_panel.setVisible(False)
    main_forms.cam_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
   
    

def Db_function():
    main_forms.db_panel.setVisible(True)
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.main_panel.setVisible(False)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
    

def Settings_function():
    main_forms.main_panel.setVisible(True) 
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
   
     
def Plugins_function():
    main_forms.Plagins_panel.setVisible(True)
    main_forms.main_panel.setVisible(False) 
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.doc_panel.setVisible(False)
   

def Voise_assistant():
    
    main_forms.voise_assistant_panel.setVisible(True)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.main_panel.setVisible(False) 
    main_forms.cam_panel.setVisible(False)
    main_forms.foto_panel.setVisible(False)
    main_forms.video_panel.setVisible(False)
    main_forms.db_panel.setVisible(False)
    main_forms.db_panel_function.setVisible(False)
    main_forms.doc_panel.setVisible(False)
 

def Help_panel():
    main_forms.doc_panel.setVisible(True)
    main_forms.voise_assistant_panel.setVisible(False)
    main_forms.Plagins_panel.setVisible(False)
    main_forms.main_panel.setVisible(False) 
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
        Load_data_object_db()

    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter login and password") 

#Функция для смены темы 
def Tema_Function():
    if(button_check[2] == True):
        main_forms.tema_button.setIcon(QtGui.QIcon('image/1.png'))
        main_forms.tema_button.setIconSize(QtCore.QSize(70,70))
        button_check[2] = False
    elif(button_check[2] == False):
        main_forms.tema_button.setIcon(QtGui.QIcon('image/0.png'))
        main_forms.tema_button.setIconSize(QtCore.QSize(70,70))
        button_check[2] = True
#Функция для включения функции входа в бд по Face id или выключение этой функции
def DB_faceid_button():
    if(button_check[0] == True):
        main_forms.db_faceid_button.setIcon(QtGui.QIcon('image/1.png'))
        main_forms.db_faceid_button.setIconSize(QtCore.QSize(70,70))
        button_check[0] = False
    elif(button_check[0] == False):
        main_forms.db_faceid_button.setIcon(QtGui.QIcon('image/0.png'))
        main_forms.db_faceid_button.setIconSize(QtCore.QSize(70,70))
        button_check[0] = True
#Функция для включения функции входа в приложение по Face id или выключение этой функции
def Log_button_face():
    if(button_check[1] == True):
        main_forms.log_button_face.setIcon(QtGui.QIcon('image/1.png'))
        main_forms.log_button_face.setIconSize(QtCore.QSize(70,70))
        button_check[1] = False
    elif(button_check[1] == False):
        main_forms.log_button_face.setIcon(QtGui.QIcon('image/0.png'))
        main_forms.log_button_face.setIconSize(QtCore.QSize(70,70))
        button_check[1] = True

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
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","register Face ID successfully")

def load_main_forms():
    cur = con.cursor()
    Message_Load()
    for row in cur.execute('SELECT Name,Firstname FROM user WHERE id = ? and id = ?',(id_code,id_code)):
        main_forms.FIO_label.setText(str(row[0]) + " " + str(row[1]))
    con.commit()
    Load_cam_panel()
    Uvedomlenie_Load()
    
    


def Face_avtorization_db():
    Cam()
    evklid_znach = Face_detector()
    if(float(evklid_znach) < 0.6):
        #QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")
        main_forms.db_panel.setVisible(False)
        main_forms.db_panel_function.setVisible(True)
        DateTime()
        Load_data()
        Load_data_object_db()
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
        main_forms.poiskEdit.setText("")
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

# Функционал для таблицы object
def Load_data_object_db():
    for id_, nazva, text_object in con.execute("SELECT id, nazva_image, object FROM foto_log"):
        row = main_forms.table_widget_object.rowCount()
        main_forms.table_widget_object.setRowCount(row + 1)

        main_forms.table_widget_object.setItem(row, 0, QtGui.QTableWidgetItem(str(id_)))
        main_forms.table_widget_object.setItem(row, 1, QtGui.QTableWidgetItem(nazva))
        main_forms.table_widget_object.setItem(row, 2, QtGui.QTableWidgetItem(text_object))
    con.commit()

#Функция удаление строк с таблицы на форме
def Delete_row_table_object():

    main_forms.table_widget_object.clearContents()
    main_forms.table_widget_object.setRowCount(0)
    


def Search_table_object():
    if(main_forms.poisk_objectEdit.text() != ""):
        Delete_row_table_object()
        for id_, nazva, text_object in con.execute("SELECT id, nazva_image, object FROM foto_log WHERE id = ? or nazva_image = ? or object = ?",(main_forms.poisk_objectEdit.text(),main_forms.poisk_objectEdit.text(),main_forms.poisk_objectEdit.text())):
            row = main_forms.table_widget_object.rowCount()
            main_forms.table_widget_object.setRowCount(row + 1)

            main_forms.table_widget_object.setItem(row, 0, QtGui.QTableWidgetItem(str(id_)))
            main_forms.table_widget_object.setItem(row, 1, QtGui.QTableWidgetItem(nazva))
            main_forms.table_widget_object.setItem(row, 2, QtGui.QTableWidgetItem(text_object))
        con.commit()
        main_forms.poisk_objectEdit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message", "enter value!")


def Add_teble_object():
    if(main_forms.imageObjectEdit.text() !="" and main_forms.object_textEdit.text() != ""):
        cur = con.cursor()
        cur.execute('INSERT INTO foto_log (id,nazva_image,object) VALUES (?,?,?)',(random.randint(1111,9999),main_forms.imageObjectEdit.text(),main_forms.object_textEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nregistration!")
        main_forms.imageObjectEdit.setText("")
        main_forms.object_textEdit.setText("")
        Delete_row_table_object()
        Load_data_object_db()
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter data")

    con.commit()

def Delete_table_object():
    if(main_forms.del_object_textEdit.text() != ""):
        cur = con.cursor()
        cur.execute("DELETE FROM foto_log WHERE id = ? or nazva_image = ? or object = ?",(main_forms.del_object_textEdit.text(),main_forms.del_object_textEdit.text(),main_forms.del_object_textEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\delete!")
        main_forms.del_object_textEdit.setText("")
        Delete_row_table_object()
        Load_data_object_db()
        main_forms.del_object_textEdit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","please enter value")
    con.commit()

def Progress_load():
    completed = 0

    while completed < 100:
        completed += 0.0001
        load_form.progress.setValue(completed)

def Logout_forms():
    main_forms.close()
    qb.show()

#Создание кадров об обьекте
def Face_dataset():
    if(main_forms.camEdit.text() != "" and main_forms.widthEdit.text != "" and main_forms.heightEdit.text() != "" and main_forms.object_numberEdit.text() and main_forms.putyEdit.text() != "" and main_forms.framesEdit.text() != ""):
        Face_datasets(main_forms.camEdit.text(),main_forms.widthEdit.text(), main_forms.heightEdit.text(), main_forms.object_numberEdit.text(), main_forms.putyEdit.text(), main_forms.framesEdit.text())

#Тренировка распознования 
def Face_training():
    if(main_forms.path_trainingEdits.text() != "" and main_forms.modelEdits.text() != ""):
        Face_trainings(main_forms.path_trainingEdits.text(), main_forms.modelEdits.text())

#Распознование лица
def Face_recognition():
    if((main_forms.check_button_add_object_db.isChecked() == True) and main_forms.object_number_recognitionEdit.text() != "" and main_forms.object_nameEdit.text() != ""):
        cur = con.cursor()
        cur.execute('INSERT INTO face_recognition (id, Name) VALUES (?,?)',(main_forms.object_number_recognitionEdit.text(), main_forms.object_nameEdit.text()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Message ok!")
        
        con.commit()

    if(main_forms.path_modelEdit.text() != ""):
        mas_object = []
        cur = con.cursor()
        for row in cur.execute('SELECT id,Name FROM face_recognition'):
            mas_object.append(row[1])
            
            
                     
    con.commit()
    Face_recognitions(main_forms.path_modelEdit.text(),mas_object)
    

# Панель данных в функции ижентификации обьектов по камере
def Load_cam_panel():
    data = data = [('Number of objects',[]), ('Bob', [('Wallet', [('Credit card', []), ('Money', [])])])]
    mas_object = []
    cur = con.cursor()
    for row in cur.execute('SELECT id,Name FROM face_recognition'):
        mas_object.append(row[1])
                          
    con.commit()
    
    data[0][1].append((str(len(mas_object)-1) + ' Objects',[]))

    
    for i in range(1,len(mas_object)):
        data[0][1][0][1].append((str(mas_object[i]),[]))

    

    main_forms.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    main_forms.treeView.customContextMenuRequested.connect(openMenu)

    model = QtGui.QStandardItemModel()
    
    addItems(model, data)
    main_forms.treeView.setModel(model)
        
    model.setHorizontalHeaderLabels([main_forms.tr("Object")])
    

   
def openMenu(self, position):

    indexes = main_forms.treeView.selectedIndexes()
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
        
    menu.exec_(main_forms.treeView.viewport().mapToGlobal(position))

def addItems(parent, elements):
    
    for text, children in elements:
        item = QtGui.QStandardItem(text)
        parent.appendRow(item)
        if children:
            addItems(item, children)



def Foto_detection():
    
    if(main_forms.foto_modelEdit.text() != "" and main_forms.foto_imageEdit.text() != "" and main_forms.foto_image_outEdit.text() != ""):
        obj_str = ""
        detections = FirstDetection(main_forms.foto_modelEdit.text(), main_forms.foto_imageEdit.text(), main_forms.foto_image_outEdit.text())
        
        for i in range(len(detections)):
            obj_str += detections[i] + "\n" 
            
        main_forms.object_list_foto_1.insertPlainText(obj_str)
        main_forms.label_status_message.setText("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t         Processing.....")
        main_forms.label_status_message.setText("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Successful recognition of objects in the photo")
        
        

        
def Folder_Open():
    QtGui.QFileDialog.getExistingDirectory(main_forms,'Open Folder','/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto')            
            

def Folder_Dowladon():
    if(main_forms.foto_imageEdit.text() != "" and main_forms.foto_image_outEdit.text() != ""):
        os.system("mkdir /home/pproger/Desktop/Copy_foto_detection")
        shutil.copy2(main_forms.foto_imageEdit.text(), r'/home/pproger/Desktop/Copy_foto_detection/image_input_copy.jpeg')
        shutil.copy2(main_forms.foto_image_outEdit.text(), r'/home/pproger/Desktop/Copy_foto_detection/image_output_copy.jpeg')
        QtGui.QFileDialog.getExistingDirectory(main_forms,'Open copy file','/home/pproger/Desktop/Copy_foto_detection')


def folder_db_save():
    if(main_forms.object_list_foto_1.toPlainText()!= "" and main_forms.foto_image_outEdit.text() != ""):
        cur = con.cursor()
        cur.execute('INSERT INTO foto_log (id,nazva_image, object) VALUES (?,?,?)',(random.randint(100,1000),main_forms.foto_image_outEdit.text(), main_forms.object_list_foto_1.toPlainText()))
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Message ok!")
        con.commit()
       
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Detection object to foto!")

#Cохрание в файл данных после идентификации обьектов
def File_save_foto():
    if(main_forms.object_list_foto_1.toPlainText()!= "" and main_forms.foto_image_outEdit.text() != ""):
        my_file = open("/home/pproger/Desktop/file.txt", "w")
        my_file.write(str(main_forms.foto_image_outEdit.text() + "\n" + main_forms.object_list_foto_1.toPlainText()))
        my_file.close()
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Message ok!")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Detection object to foto!")

# Метод для звкрытия панель с подключением к БД
def Exit_panel_connect_db():
    main_forms.connect_db_panel.setVisible(False)

# Метод для открытия панель с подключением к БД
def Connect_function():
    main_forms.connect_db_panel.setVisible(True)

def Load_command_voice():
    list_vopros = []
    list_otvet = []
    for vopros,otvet in con.execute("SELECT vopros, otvet FROM voice_assistant"):
        list_vopros.append(str(vopros))
        list_otvet.append(str(otvet))
    return list_vopros, list_otvet      

def voice_vopros():
    text_voprosa, text_otveta = Load_command_voice()
    otvet_bool = True
    os.system("echo «Говорите» | RHVoice-test -p anna")
    comand_text_vopros = listen()
    if(comand_text_vopros == "сколько время" or comand_text_vopros == "время"):
        os.system("echo «Cейчас "+str(datetime.strftime(datetime.now(), "%H:%M:%S"))+"» | RHVoice-test -p anna")
    elif(comand_text_vopros == "какая операционная система" or comand_text_vopros == "какая ос" or comand_text_vopros== "что за ос" or comand_text_vopros == "операционная система"):
        os.system("echo «Операционная система "+str(platform.system())+"» | RHVoice-test -p anna")
        main_forms.assistant_list.appendPlainText("Операционная система "+str(platform.system()))
    else:
        for i in range(len(text_voprosa)):
            if(text_voprosa[i] == comand_text_vopros):
                os.system("echo "+text_otveta[i]+" | RHVoice-test -p anna")
                otvet_bool = False
                main_forms.assistant_list.appendPlainText("Вы сказали: " + str(comand_text_vopros) + "?\n    Ответ: " +str(text_otveta[i]))
        if(otvet_bool == True):
            os.system("echo «Не знаю, может подскажешь?» | RHVoice-test -p anna")
            comand_text_otvet = listen()
            cur = con.cursor()
            cur.execute('INSERT INTO voice_assistant (vopros, otvet) VALUES (?,?)',(str(comand_text_vopros),str(comand_text_otvet)))
            con.commit()
            os.system("echo «Запомнила» | RHVoice-test -p anna")
            text_voprosa, text_otveta = Load_command_voice()
            voice_vopros()

# Метод для голосового асистента
def Microfon_assistant():
    global assistent_check
    if(assistent_check == True):
        os.system("echo «Привет я голосовой ассистент Таня! Что вам угодно?» | RHVoice-test -p anna")
        assistent_check = False
    voice_vopros()
     
    

# Метод обнаружение обьктов на видео
def Video_detection():
    if(main_forms.video_modelEdit.text() != "" and main_forms.video_inputEdit.text() != "" and main_forms.video_outEdit.text() != "" and main_forms.frames_per_secondEdit.text() != ""):
        main_forms.object_list_video.setPlainText("[INFO] The process of work of a neural network for recognition of objects has begun!!!")
        time.sleep(1)
        Detection_object_video(main_forms.video_modelEdit.text(),main_forms.video_inputEdit.text(),main_forms.video_outEdit.text(), main_forms.frames_per_secondEdit.text())
        main_forms.object_list_video.setPlainText("[INFO] Successfully completed the process of work of a neural network for object recognition!!!")
    else:
        main_forms.object_list_video.setPlainText("[WARNING] Fill in all the fields!!!")

# Метод для открытие панели для входящих писем
def Message_function_s():
    main_forms.message_fun_panel.setVisible(True)
    main_forms.been_panel.setVisible(False)

# Метод для открытия панели для входящих уведомлений
def Bell_function():
    main_forms.been_panel.setVisible(True)
    main_forms.message_fun_panel.setVisible(False)

# Метод для закрытия панели уведомлений
def Exit_Been():
    main_forms.been_panel.setVisible(False)

#Метод для закрытиня панели сообщений
def Exit_message_fun():
    main_forms.message_fun_panel.setVisible(False)

#Открытие файлов для ввода панели Видео
def File_open_s_v1():
    filenamev1 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.video_modelEdit.setText(str(filenamev1))
    

def File_open_s_v2():
    filenamev2 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.video_inputEdit.setText(str(filenamev2))
    

def File_open_s_v3():
    filenamev3 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.video_outEdit.setText(str(filenamev3))
    

#Открытие файла панели конекта с бд
def File_open_s_db():
    filenamedb = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.path_trainingEdit.setText(str(filenamedb))

#Открытие файла в панели фото
def File_open_s_f1():
    filename1 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.foto_modelEdit.setText(str(filename1))

def File_open_s_f2():
    filename2 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.foto_imageEdit.setText(str(filename2))

def File_open_s_f3():
    filenamef3 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.foto_image_outEdit.setText(str(filenamef3))

#Открытие файлов в панели камера
def File_open_s_cam1():
    filenamecam1 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.putyEdit.setText(str(filenamecam1))

def File_open_s_cam2():
    filenamecam2 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.path_trainingEdit.setText(str(filenamecam2))    

def File_open_s_cam3():
    filenamecam3 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.modelEdit.setText(str(filenamecam3))

def File_open_s_cam4():
    filenamecam4 = QtGui.QFileDialog.getOpenFileName(main_forms,'Open File', '/')
    main_forms.path_modelEdit.setText(str(filenamecam4))

# Открытие каталогу с файлами с проектом
def OpenFolder_Video():
    QtGui.QFileDialog.getExistingDirectory(main_forms,'Open Folder','/home/pproger/Desktop/machine_learning_python/video_obcject') 

#Сохрание видео файлов на робочий стол 
def Folder_DowladonVideo_button():
    if(main_forms.foto_imageEdit.text() != "" and main_forms.foto_image_outEdit.text() != ""):
        os.system("mkdir /home/pproger/Desktop/Copy_Video_detection")
        shutil.copy2(main_forms.video_inputEdit.text(), r'/home/pproger/Desktop/Copy_Video_detection/video_input_copy.mp4')
        shutil.copy2(main_forms.video_outEdit.text(), r'/home/pproger/Desktop/Copy_Video_detection/video_output_copy.avi')
        QtGui.QFileDialog.getExistingDirectory(main_forms,'Open copy file','/home/pproger/Desktop/Copy_Video_detection')

#Загрузка уведомлений с бд
def Uvedomlenie_Load():
    for texts, Data_time in con.execute("SELECT texts, Data_time FROM uvedomlenie WHERE id_user = ? and id_user = ?",(id_code,id_code)):
        main_forms.listWidget_u.addItem(str(Data_time) + "\n" + str(texts))   
   
    con.commit()

#Загрузка уведомлений с бд
def Message_Load():
    for texts, Data_time in con.execute("SELECT texts, Date_time FROM message_admin WHERE id_user = ? and id_user = ?",(id_code,id_code)):
        main_forms.listWidget.addItem(str(Data_time) + "\n" + str(texts))   
   
    con.commit()

# Удаление уведомлений 
def Been_clear():
    cur = con.cursor()
    cur.execute("DELETE FROM uvedomlenie ")
    con.commit()
    main_forms.listWidget_u.clear()

# Удаление сообшений с панели
def Message_clear():
    cur = con.cursor()
    cur.execute("DELETE FROM message_admin  ")
    con.commit()
    main_forms.listWidget.clear()

# Конект с бд
def Connect_db_check():
    if(con):
        main_forms.check_label_.setText("Successful Connection")
    else:
        main_forms.check_label_.setText("No Connection")


# Сохранение плагина Face_id
def Plugins_face():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/Face_id.zip', r'/home/pproger/Desktop/Face_id.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Сохранение плагина распазнование болен ли человек на туберкулез
def Plugins_flugo():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/fluorography-detection-of-a-disease-using-a-neural-network.zip', r'/home/pproger/Desktop/fluorography-detection-of-a-disease-using-a-neural-network.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Сохранение плагина для фото переобразование с чорно-белого в цветную
def Plugins_foto():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/Colorful_Image_Colorization.zip', r'/home/pproger/Desktop/Colorful_Image_Colorization.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Плагин для удаление с фото лишних элементов
def Plugins_foto_del():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/opencv-inpainting.zip', r'/home/pproger/Desktop/opencv-inpainting.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Плагин для обнаружения обьектов на фото
def Plugins_foto_detection():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/plagin_foto_detection.zip', r'/home/pproger/Desktop/plagin_foto_detection.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Плагин для обнаружения обьектов на видео
def Plugins_Video_Detection():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/plagin_video_detection.zip', r'/home/pproger/Desktop/plagin_video_detection.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Плагин голосовой ассистент
def Plugins_voice():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/voice_assistant.zip', r'/home/pproger/Desktop/voice_assistant.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Плагин контроля дистанции между людьми
def Plugins_pandemic():
    shutil.copy2(r'/home/pproger/Desktop/machine_learning_python/plugins/social-distance-detector.zip', r'/home/pproger/Desktop/social-distance-detector.zip')
    QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Successfully saved to the desktop!")

# Голосовые команды
def Micro_function():
    os.system("echo «Что сделать?» | RHVoice-test -p anna")
    cmd = listen()
    if(cmd == "открой голосового ассистента" or cmd == "открой ассистента" or cmd == "ассистент" or cmd == "голосового ассистента"):
        Voise_assistant()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "открой панель фото" or cmd == "панель фото"):
        Foto_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "открой панель видео" or cmd == "панель видео"):
        Vidoe_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "открой панель камера" or cmd == "панель камера"):
        Cam_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "открой панель база данных" or cmd == "панель база данных"):
        Db_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "открой панель плагин" or cmd == "панель плагин"):
        Plugins_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    elif(cmd == "что ты умеешь" or cmd == "твои команды"):
        os.system("echo «Открой голосового ассистента, открой панель фото, открой панель видео, открой панель камера, открой панель база данных, открой панель плагин» | RHVoice-test -p anna")
    elif(cmd == "закрой главное окно"):
        Logout_forms()
    elif(cmd == "открой панель настройки"):
        Settings_function()
        os.system("echo «Хорошо» | RHVoice-test -p anna")
    else:
        os.system("echo «Не поняла повторите команду, вы сказали "+ cmd +"» | RHVoice-test -p anna")
# Открытие видео которое было загружено для обробки        
def Open_Video_Input():
    os.system("mpv " + str(main_forms.video_inputEdit.text()))

# Открытие видео которое было после обработки нейронной сетью
def Open_Video_Output():
    os.system("mpv " + str(main_forms.video_outEdit.text()))

def Github_open():
    os.system("firefox https://github.com/PPROGER/machine_learning_python")

# Функция для поиска в приложении
def Search_Function():
    if(main_forms.lineedit.text() != ""):
        if(main_forms.lineedit.text() == "Face ID" or main_forms.lineedit.text() == "face" or main_forms.lineedit.text() == "registration Face ID"):
            Settings_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "Foto" or main_forms.lineedit.text() == "foto"):
            Foto_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "Video" or main_forms.lineedit.text() == "video"):
            Vidoe_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "Cam" or main_forms.lineedit.text() == "cam"):
            Cam_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "settings"):
            Settings_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "db"):
            Db_function()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "help"):
            Help_panel()
            main_forms.lineedit.setText("")
        elif(main_forms.lineedit.text() == "voice assistant"):
            Voise_assistant()
            main_forms.lineedit.setText("")
    else:
        QtGui.QMessageBox.about(QtGui.QWidget(),"Message","Enter value!")


#Основная программа 
app = QtGui.QApplication(sys.argv)
load_form = QLoad()
qb = Qlogin()
main_forms = QMain()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(log_avtorization))
qb.log_button.clicked.connect(log_avtorization)
qb.face_button.clicked.connect(faceid_avtorization)
qb.registration_button.clicked.connect(Registration_user)
qb.vostanovlenie_button.clicked.connect(Recovery_show)
qb.log_r_button.clicked.connect(Show_log_reg)
qb.recovey_button_.clicked.connect(Recovery_user)
main_forms.cam_button.clicked.connect(Cam_function)
main_forms.video_button.clicked.connect(Vidoe_function)
main_forms.foto_button.clicked.connect(Foto_function)
main_forms.db_button.clicked.connect(Db_function)
main_forms.settings_button.clicked.connect(Settings_function)
main_forms.help.clicked.connect(Help_panel)
main_forms.log_button.clicked.connect(Log_func_db)
main_forms.tema_button.clicked.connect(Tema_Function)
main_forms.db_faceid_button.clicked.connect(DB_faceid_button)
main_forms.log_button_face.clicked.connect(Log_button_face)
main_forms.enter_button.clicked.connect(Message_function)
main_forms.face_registration.clicked.connect(Registration_face)
main_forms.face_button.clicked.connect(Face_avtorization_db)
main_forms.poisk_button.clicked.connect(Search_user)
main_forms.add_button.clicked.connect(Add_user)
main_forms.del_button.clicked.connect(Delete_user)
main_forms.voise.clicked.connect(Voise_assistant)
main_forms.logout_button.clicked.connect(Logout_forms)
main_forms.Face_dataset_button.clicked.connect(Face_dataset)
main_forms.Face_training_button.clicked.connect(Face_training)
main_forms.Face_recognition_button.clicked.connect(Face_recognition)
main_forms.foto_detection_button.clicked.connect(Foto_detection)
main_forms.folder_open_button.clicked.connect(Folder_Open)
main_forms.folder_dowladon_button.clicked.connect(Folder_Dowladon)
main_forms.folder_db_save_button.clicked.connect(folder_db_save)
main_forms.folder_file_save_button.clicked.connect(File_save_foto)
main_forms.exit_connect_db_button.clicked.connect(Exit_panel_connect_db)
main_forms.connect_function_button.clicked.connect(Connect_function)
main_forms.plugins.clicked.connect(Plugins_function)
main_forms.microfon_function_button.clicked.connect(Microfon_assistant)
main_forms.video_detection_button.clicked.connect(Video_detection)
main_forms.message_function_button.clicked.connect(Message_function_s)
main_forms.bell_function_button.clicked.connect(Bell_function)
main_forms.exit_been_button.clicked.connect(Exit_Been)
main_forms.exit_message_fun_button.clicked.connect(Exit_message_fun)
main_forms.file_open_button_v1.clicked.connect(File_open_s_v1)
main_forms.file_open_button_v2.clicked.connect(File_open_s_v2)
main_forms.file_open_button_v3.clicked.connect(File_open_s_v3)
main_forms.file_open_button_db.clicked.connect(File_open_s_db)
main_forms.file_open_button_f1.clicked.connect(File_open_s_f1)
main_forms.file_open_button_f2.clicked.connect(File_open_s_f2)
main_forms.file_open_button_f3.clicked.connect(File_open_s_f3)
main_forms.file_open_button_cam1.clicked.connect(File_open_s_cam1)
main_forms.file_open_button_cam2.clicked.connect(File_open_s_cam2)
main_forms.file_open_button_cam3.clicked.connect(File_open_s_cam3)
main_forms.file_open_button_cam4.clicked.connect(File_open_s_cam4)
main_forms.openfolder_video_button.clicked.connect(OpenFolder_Video)
main_forms.folder_dowladonVideo_button.clicked.connect(Folder_DowladonVideo_button)
main_forms.been_clear_button.clicked.connect(Been_clear)
main_forms.message_clear_button.clicked.connect(Message_clear)
main_forms.connect_panel_button.clicked.connect(Connect_db_check)
main_forms.plugins_flugo.clicked.connect(Plugins_flugo)
main_forms.plugins_foto.clicked.connect(Plugins_foto)
main_forms.plugins_foto_del.clicked.connect(Plugins_foto_del)
main_forms.plugins_face.clicked.connect(Plugins_face)
main_forms.plugins_foto_detection.clicked.connect(Plugins_foto_detection)
main_forms.plugins_video_detection.clicked.connect(Plugins_Video_Detection)
main_forms.plugins_voice.clicked.connect(Plugins_voice)
main_forms.plugins_pandemic.clicked.connect(Plugins_pandemic)
main_forms.micro_function_button.clicked.connect(Micro_function)
main_forms.open_video_button_input.clicked.connect(Open_Video_Input)
main_forms.open_video_button_output.clicked.connect(Open_Video_Output)
main_forms.poisk_object_button.clicked.connect(Search_table_object)
main_forms.add_objectText_button.clicked.connect(Add_teble_object)
main_forms.del_objectTextbutton.clicked.connect(Delete_table_object)
main_forms.search_function_button.clicked.connect(Search_Function)
main_forms.github_function_button.clicked.connect(Github_open)


load_form.show()
Progress_load()
load_form.close()
qb.show()
sys.exit(app.exec_())




