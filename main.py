import sys
from PyQt4 import QtGui, QtCore
from db_connect import con
from login import Qlogin

    
   





    

def log_avtorization():
    cur = con.cursor()
    for row in cur.execute('SELECT Gmail,Password FROM user'):
        if(str(row[0]) == qb.loginEdit.text() and str(row[1]) == qb.passwordEdit.text()):
            qb.loginEdit.setText('')
            qb.passwordEdit.setText('')
            QtGui.QMessageBox.about(QtGui.QWidget(),"Message","You have successfully\nlogged in!")

    
    
    
    con.commit()

    
app = QtGui.QApplication(sys.argv)
qb = Qlogin()
#QtGui.QWidget.connect(qb.log_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT(log_avtorization))
qb.log_button.clicked.connect(log_avtorization)

qb.show()
sys.exit(app.exec_())



