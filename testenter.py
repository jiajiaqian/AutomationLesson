from PyQt5 import QtWidgets
from test import Ui_MainWindow

import datetime

import logging
import logging.handlers

from threading import Timer
import numpy as np

from sklearn.externals import joblib

import time

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)
        #self.new.pushButton.clicked.connect(self.myPrint)   #槽函数不用加括号
        #self.new.pushButton_3.clicked.connect(self.timeStart)   #槽函数不用加括号

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

