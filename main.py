from db_connect import con
    
cur = con.cursor()   
cur.execute('INSERT INTO user(id,Name,Firstname,Gmail,Password) VALUES (1212,"Saha","Daviov","davidsa32@gmail.com","hfy4g3")') 
   

con.commit()
    
#app = QtGui.QApplication(sys.argv)
#qb = Qlogin()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(buttonClicked()))
#sys.exit(app.exec_())