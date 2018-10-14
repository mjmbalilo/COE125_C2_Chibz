# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PassengerWindow(object):
    def setupUi(self, Passenger, passengerInfo):
        self.passengerTxtUi = {}
        ###################################################################### 
        Passenger.setObjectName("Passenger")
        Passenger.resize(560, 670)
        Passenger.setMinimumSize(QtCore.QSize(560, 670))

        ######################################################################     
        self.grdOuter = QtWidgets.QGridLayout(Passenger)
        self.scrlOuter = QtWidgets.QScrollArea(Passenger)
        self.scrlOuterContents = QtWidgets.QWidget()
        self.formOuter = QtWidgets.QFormLayout(self.scrlOuterContents)

        i = 1
        for age in passengerInfo:
            if(int(passengerInfo[age]) > 0):
                self.GenerateForm(str(age), int(passengerInfo[age]))
                self.formOuter.setWidget(i, QtWidgets.QFormLayout.FieldRole, self.gb)
                i += 1


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
        #self.btnAddPassenger.clicked.connect(self.PassengerInfo)

        self.retranslateUi(Passenger)
        QtCore.QMetaObject.connectSlotsByName(Passenger)

    def retranslateUi(self, Passenger):
        _translate = QtCore.QCoreApplication.translate
        Passenger.setWindowTitle(_translate("Passenger", "Dialog"))
        self.btnAddPassenger.setText(_translate("Passenger", "Add Passenger(s)"))

    def GenerateForm(self, age, passengerNum):
        font = QtGui.QFont()
        font.setPointSize(14)
        txtUi = []
        
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
            self.cbxGender = QtWidgets.QComboBox(self.gbAge)   
            self.lblFName = QtWidgets.QLabel(self.gbAge)
            self.lblLName = QtWidgets.QLabel(self.gbAge)
            self.lblGender = QtWidgets.QLabel(self.gbAge)
            info = [self.txtFName, self.txtLName, self.cbxGender]
            txtUi.append(info)            

            #Design 
            self.gbAge.setTitle("%s %d: " %(age, x))
            self.lblFName.setText("First Name:")
            self.lblLName.setText("Last Name:")
            self.lblGender.setText("Gender:")
            self.cbxGender.addItem("Male")
            self.cbxGender.addItem("Female")
            self.grdForm.setContentsMargins(10, 10, 10, 10)
            self.grdForm.addWidget(self.lblFName, 0, 0, 1, 1)
            self.grdForm.addWidget(self.lblLName, 1, 0, 1, 1)
            self.grdForm.addWidget(self.lblGender, 2, 0, 1, 1)
            self.grdForm.addWidget(self.txtFName, 0, 2, 1, 1)
            self.grdForm.addWidget(self.txtLName, 1, 2, 1, 1)
            self.grdForm.addWidget(self.cbxGender, 2, 2, 1, 1)
            self.formInner.setWidget(x, QtWidgets.QFormLayout.FieldRole, self.gbAge)
            
        self.passengerTxtUi[age] = txtUi


    @property
    def PassengerInfo(self):
        passengerInfo = {}
        for age in self.passengerTxtUi:
            info = []
            for txtUi in self.passengerTxtUi[age]:
                txt = []
                i = 1
                for obj in txtUi:
                    if (i == 3):
                        txt.append(obj.currentText())
                    else:
                        txt.append(obj.text())
                        if(obj.text() == ''):
                            raise Exception('Please fill up all required fields!')
                    i += 1
                info.append(txt)
            passengerInfo[age] = info

        return passengerInfo
            

if __name__ == "__main__":
    import sys
    passInfo = [2, 1, 0, 0]
    app = QtWidgets.QApplication(sys.argv)
    Passenger = QtWidgets.QDialog()
    ui = Ui_PassengerWindow()
    ui.setupUi(Passenger, passInfo)
    Passenger.show()
    sys.exit(app.exec_())

