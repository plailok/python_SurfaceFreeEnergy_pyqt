from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
from v2_mainwindow import Ui_MainWindow
from SDF_dialog import Ui_Dialog
from main_calculation import Calculation
import sys


class MyWindow_v2(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow_v2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __setupUI(self):
        pass

    def __theory_button_checked(self):
        pass

    def __settings_button_checked(self):
        pass

    def __result_buttton_checked(self):
        pass

if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication([])
        application = MyWindow_v2()
        application.show()
        sys.exit(app.exec())
    except Exception as exc:
        print(f'Ooops, something going wrong... {exc}')
