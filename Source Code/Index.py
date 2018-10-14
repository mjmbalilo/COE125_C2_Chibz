# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers import Ui_Controllers

def main():
    uiCtr = Ui_Controllers()
    app = QtWidgets.QApplication(sys.argv)
    uiCtr.Login()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
