# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Passenger(object):
    def setupUi(self, Passenger):

        ###################################################################### 
        Passenger.setObjectName("Passenger")
        Passenger.resize(560, 670)
        Passenger.setMinimumSize(QtCore.QSize(560, 670))

        ######################################################################     
        self.grdOuter = QtWidgets.QGridLayout(Passenger)
        self.scrlOuter = QtWidgets.QScrollArea(Passenger)
        self.scrlOuterContents = QtWidgets.QWidget()
        self.formOuter = QtWidgets.QFormLayout(self.scrlOuterContents)

        self.GenerateForm("Adult", 5)
        self.formOuter.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gb)
        self.GenerateForm("Infant", 3)
        self.formOuter.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gb)
        self.GenerateForm("Child", 3)
        self.formOuter.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gb)


        self.scrlOuter.setEnabled(True)
        self.scrlOuter.setWidgetResizable(True)
        self.grdOuter.setContentsMargins(0, 0, 0, 15)
        self.scrlOuter.setWidget(self.scrlOuterContents)
        self.grdOuter.addWidget(self.scrlOuter, 0, 0, 1, 1)
        
        ###################################################################### 
        self.btnAddPassenger = QtWidgets.QPushButton(Passenger)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAddPassenger.setFont(font)
        self.grdOuter.addWidget(self.btnAddPassenger, 1, 0, 1, 1)
        self.btnAddPassenger.clicked.connect(self.MessageBox)

        self.retranslateUi(Passenger)
        QtCore.QMetaObject.connectSlotsByName(Passenger)

    def retranslateUi(self, Passenger):
        _translate = QtCore.QCoreApplication.translate
        Passenger.setWindowTitle(_translate("Passenger", "Dialog"))
        self.btnAddPassenger.setText(_translate("Passenger", "Add Passenger(s)"))

    def GenerateForm(self, age, passengerNum):
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FName = []
        self.LName = []
        self.Gender = []
        
        self.gb = QtWidgets.QGroupBox(self.scrlOuterContents)        
        self.grdInner = QtWidgets.QGridLayout(self.gb)
        self.scrlInner = QtWidgets.QScrollArea(self.gb)
        self.scrlInnerContents = QtWidgets.QWidget()

        self.gb.setTitle("%s(s):" %age) 
        self.gb.setFont(font)
        self.grdInner.setContentsMargins(0, 0, 0, 0)
        self.grdInner.addWidget(self.scrlInner, 0, 0, 1, 1)
        self.scrlInner.setWidgetResizable(True)
        self.scrlInner.setWidget(self.scrlInnerContents)
        self.formInner = QtWidgets.QFormLayout(self.scrlInnerContents)
        for x in range(1, passengerNum + 1):
            #Initialize
            self.gbAge = QtWidgets.QGroupBox(self.scrlInnerContents)
            self.grdForm = QtWidgets.QGridLayout(self.gbAge)          
            self.txtFName = QtWidgets.QLineEdit(self.gbAge)
            self.txtLName = QtWidgets.QLineEdit(self.gbAge)
            self.txtGender = QtWidgets.QLineEdit(self.gbAge)   
            self.lblFName = QtWidgets.QLabel(self.gbAge)
            self.lblLName = QtWidgets.QLabel(self.gbAge)
            self.lblGender = QtWidgets.QLabel(self.gbAge)
            self.FName.append(self.txtFName)
            self.LName.append(self.txtLName)
            self.Gender.append(self.txtGender)
            

            #Design 
            self.gbAge.setTitle("%s %d: " %(age, x))
            self.lblFName.setText("First Name:")
            self.lblLName.setText("Last Name:")
            self.lblGender.setText("Gender:")
            self.grdForm.setContentsMargins(10, 10, 10, 10)
            self.grdForm.addWidget(self.lblFName, 0, 0, 1, 1)
            self.grdForm.addWidget(self.lblLName, 1, 0, 1, 1)
            self.grdForm.addWidget(self.lblGender, 2, 0, 1, 1)
            self.grdForm.addWidget(self.txtFName, 0, 2, 1, 1)
            self.grdForm.addWidget(self.txtLName, 1, 2, 1, 1)
            self.grdForm.addWidget(self.txtGender, 2, 2, 1, 1)
            self.formInner.setWidget(x, QtWidgets.QFormLayout.FieldRole, self.gbAge)

    def MessageBox(self):
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setText(self.FName[0].text())
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Passenger = QtWidgets.QDialog()
    ui = Ui_Passenger()
    ui.setupUi(Passenger)
    Passenger.show()
    sys.exit(app.exec_())

