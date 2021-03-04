from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
from v2_mainwindow import Ui_MainWindow
from SDF_dialog import Ui_Dialog
from main_calculation import Calculation
import sys


class MyWindow_v2(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow_v2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__setupUI()
        self.web = QWebView(self.ui.theorysFrame)
        self.web.setHtml('/Refractive index - Wikipedia.html')

    def __setupUI(self):
        self.ui.theoryButton.setEnabled(False)
        self.ui.theoryButton.clicked.connect(self.__theory_button_checked)
        self.ui.settingsButton.clicked.connect(self.__settings_button_checked)
        self.ui.measurmentButton.clicked.connect(self.__measurment_buttton_checked)

    def __theory_button_checked(self):
        print('Theory button checked')
        self.ui.theoryButton.setEnabled(False)
        self.ui.settingsButton.setEnabled(True)
        self.ui.measurmentButton.setEnabled(True)

    def __settings_button_checked(self):
        print('Settings button checked')
        self.ui.theoryButton.setEnabled(True)
        self.ui.settingsButton.setEnabled(False)
        self.ui.measurmentButton.setEnabled(True)

    def __measurment_buttton_checked(self):
        print('Measurment button checked')
        self.ui.theoryButton.setEnabled(True)
        self.ui.settingsButton.setEnabled(True)
        self.ui.measurmentButton.setEnabled(False)

    def __theory_chose(self):
        print('Theory had been changed')
        print(f'Current theory - {self.ui.theoryCombobox.currentText()}')


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication([])
        application = MyWindow_v2()
        application.show()
        sys.exit(app.exec())
    except Exception as exc:
        print(f'Ooops, something going wrong... {exc}')
