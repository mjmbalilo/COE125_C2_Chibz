# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ryu\Desktop\Airline Reservation System\UI\signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(662, 430)
        self.verticalLayoutWidget = QtWidgets.QWidget(SignupWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 281, 380))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtFN = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtFN.setFont(font)
        self.txtFN.setObjectName("txtFN")
        self.verticalLayout.addWidget(self.txtFN)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtLN = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtLN.setFont(font)
        self.txtLN.setObjectName("txtLN")
        self.verticalLayout.addWidget(self.txtLN)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.txtEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.verticalLayout.addWidget(self.txtEmail)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txtUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.verticalLayout.addWidget(self.txtUsername)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txtPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.verticalLayout.addWidget(self.txtPassword)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.txtConfirmPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtConfirmPassword.setFont(font)
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPassword.setObjectName("txtConfirmPassword")
        self.verticalLayout.addWidget(self.txtConfirmPassword)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SignupWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 20, 281, 287))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.txtAddress1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtAddress1.setFont(font)
        self.txtAddress1.setObjectName("txtAddress1")
        self.verticalLayout_2.addWidget(self.txtAddress1)
        self.txtAddress2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtAddress2.setFont(font)
        self.txtAddress2.setObjectName("txtAddress2")
        self.verticalLayout_2.addWidget(self.txtAddress2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.dateBirth = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateBirth.setFont(font)
        self.dateBirth.setObjectName("dateBirth")
        self.verticalLayout_2.addWidget(self.dateBirth)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.cbGender = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbGender.setFont(font)
        self.cbGender.setObjectName("cbGender")
        self.cbGender.addItem("")
        self.cbGender.addItem("")
        self.verticalLayout_2.addWidget(self.cbGender)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.txtContactNum = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtContactNum.setFont(font)
        self.txtContactNum.setObjectName("txtContactNum")
        self.verticalLayout_2.addWidget(self.txtContactNum)
        self.btnSignUp = QtWidgets.QPushButton(SignupWindow)
        self.btnSignUp.setGeometry(QtCore.QRect(340, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setObjectName("btnSignUp")
        self.btnCancel = QtWidgets.QPushButton(SignupWindow)
        self.btnCancel.setGeometry(QtCore.QRect(490, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "Customer Sign Up"))
        self.label.setText(_translate("SignupWindow", "First Name:"))
        self.label_2.setText(_translate("SignupWindow", "Last Name:"))
        self.label_8.setText(_translate("SignupWindow", "Email Address:"))
        self.label_3.setText(_translate("SignupWindow", "Username:"))
        self.label_4.setText(_translate("SignupWindow", "Password:"))
        self.label_10.setText(_translate("SignupWindow", "Confirm Password:"))
        self.label_9.setText(_translate("SignupWindow", "Address:"))
        self.label_5.setText(_translate("SignupWindow", "Date of Birth:"))
        self.label_7.setText(_translate("SignupWindow", "Gender:"))
        self.cbGender.setCurrentText(_translate("SignupWindow", "Male"))
        self.cbGender.setItemText(0, _translate("SignupWindow", "Male"))
        self.cbGender.setItemText(1, _translate("SignupWindow", "Female"))
        self.label_6.setText(_translate("SignupWindow", "Contact Number:"))
        self.btnSignUp.setText(_translate("SignupWindow", "Sign Up"))
        self.btnCancel.setText(_translate("SignupWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QDialog()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec_())

