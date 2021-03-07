# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QTextBrowser
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp, QUrl
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

from result_widget import Ui_Form as result_ui
from setting_widget import Ui_Form as setting_ui
from v2_mainwindow import Ui_MainWindow
from dialog import Ui_Dialog

from main_calculation import Calculation
import sys

LIQUIDS = ['Water', 'Formamide', 'Ethylene Glycole', '\u03B1-bromnaphtalene']
HORIZONTAL_HEADER = ['Liquid', 'Polar', 'Dispersive']
TEMPERATURE = {'Water': {'21': ('w111', 111),
                         '22': ('w222', 222),
                         '23': ('w333', 333),
                         '24': ('w444', 444),
                         '25': (26.4, 46.4),
                         '26': ('w666', 666)},
               'Formamide': {'21': ('f111', 111),
                             '22': ('f222', 222),
                             '23': ('f333', 333),
                             '24': ('f444', 444),
                             '25': (22.4, 34.6),
                             '26': ('f666', 666)},
               'Ethylene Glycole': {'21': ('e111', 111),
                                    '22': ('e222', 222),
                                    '23': ('e333', 333),
                                    '24': ('e444', 444),
                                    '25': (26.4, 21.3),
                                    '26': ('e666', 666)},
               '\u03B1-bromnaphtalene': {'21': ('a111', 111),
                                         '22': ('a222', 222),
                                         '23': ('a333', 333),
                                         '24': ('a444', 444),
                                         '25': (44.4, 0),
                                         '26': ('a666', 666)}}


class MyWindow_v2(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow_v2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.liquids = {}
        self.line = None
        self.__setupUI()

    @pyqtSlot()
    def __setupUI(self):
        # add WebView widget
        self.web = QWebView()
        self.web.setUrl(QUrl(theory))
        self.ui.gridLayout_5.addWidget(self.web)

        # add setting widget
        self.Form = QtWidgets.QWidget()
        self.settings_ui = setting_ui()
        self.settings_ui.setupUi(self.Form)
        self.ui.gridLayout_5.addWidget(self.Form)
        self.Form.close()

        # add result widget
        self.Result = QtWidgets.QWidget()
        self.result_ui = result_ui()
        self.result_ui.setupUi(self.Result)
        self.ui.resultGridLayout.addWidget(self.Result)
        self.Result.close()

        self.ui.theoryButton.setEnabled(False)
        self.ui.theoryCombobox.setEnabled(False)
        self.settings_ui.pushButton.clicked.connect(self._add_liquid_button_clicked)
        self.ui.theoryButton.clicked.connect(self.__theory_button_checked)
        self.ui.settingsButton.clicked.connect(self.__settings_button_checked)
        self.ui.measurmentButton.clicked.connect(self.__measurment_buttton_checked)
        self.ui.theoryCombobox.currentTextChanged.connect(self.__theory_chose)

    @pyqtSlot()
    def __theory_button_checked(self):
        self.Form.close()
        self.Result.close()
        self.web.show()
        self.resize(1246, 564)
        self.ui.theoryCombobox.setEnabled(False)
        self.ui.theoryButton.setEnabled(False)
        self.ui.settingsButton.setEnabled(True)
        self.ui.measurmentButton.setEnabled(True)

    @pyqtSlot()
    def __settings_button_checked(self):
        self.Form.close()
        self.Result.close()
        # TODO Исправить этот костыль (web.show() => web.close())
        self.web.show()
        self.resize(1246, 564)
        self.web.close()
        self.Form.show()
        self.ui.theoryCombobox.setEnabled(True)
        self.ui.theoryButton.setEnabled(True)
        self.ui.settingsButton.setEnabled(False)
        self.ui.measurmentButton.setEnabled(True)

    @pyqtSlot()
    def __measurment_buttton_checked(self):
        self.web.close()
        self.Form.show()
        self.Result.show()
        self.ui.theoryCombobox.setEnabled(True)
        self.ui.theoryButton.setEnabled(True)
        self.ui.settingsButton.setEnabled(True)
        self.ui.measurmentButton.setEnabled(False)

    @pyqtSlot()
    def _add_liquid_button_clicked(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog(LIQUIDS)
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            self.liquids[self.ui.theoryCombobox.currentText()] = []
            for index in range(ui.myList.count()):
                self.liquids[self.ui.theoryCombobox.currentText()].append(ui.myList.item(index).text())

            self.__create_input_bar()
            self.__fullfill_table()
        else:
            pass

    @pyqtSlot()
    def __create_input_bar(self):
        self.settings_ui.gridLayout_2.setColumnStretch(0, 5)
        self.settings_ui.gridLayout_2.setColumnStretch(1, 2)
        for index, liquid in enumerate(self.liquids[self.ui.theoryCombobox.currentText()]):
            new_label = QtWidgets.QLabel(text=liquid)
            new_label.setFixedHeight(30)
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            new_lineedit = QtWidgets.QLineEdit()
            new_lineedit.setAlignment(QtCore.Qt.AlignCenter)
            reg_ex = QRegExp("[0-9]+.[0-9]{,3}")
            input_validator = QRegExpValidator(reg_ex, new_lineedit)
            new_lineedit.setValidator(input_validator)
            self.settings_ui.gridLayout_2.addWidget(new_label, index, 0)
            self.settings_ui.gridLayout_2.addWidget(new_lineedit, index, 1)

    @pyqtSlot()
    def __fullfill_table(self):
        self.settings_ui.tableWidget.setColumnCount(3)
        self.settings_ui.tableWidget.verticalHeader().hide()
        self.settings_ui.tableWidget.setHorizontalHeaderLabels(HORIZONTAL_HEADER)
        self.settings_ui.tableWidget.setColumnWidth(0, 260)
        if self.liquids[self.ui.theoryCombobox.currentText()]:
            liquids = self.liquids[self.ui.theoryCombobox.currentText()]
            cur_temp = self.ui.tempCombobox.currentText()
            self.settings_ui.tableWidget.setRowCount(len(liquids))
            for index, liquid in enumerate(liquids):
                item0 = QTableWidgetItem(liquid)
                item0.setTextAlignment(QtCore.Qt.AlignCenter)
                item1 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][0]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][1]))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)

                self.settings_ui.tableWidget.setItem(index, 0, item0)
                self.settings_ui.tableWidget.setItem(index, 1, item1)
                self.settings_ui.tableWidget.setItem(index, 2, item2)

    @pyqtSlot()
    def __theory_chose(self):
        print('Theory had been changed')
        print(f'Current theory - {self.ui.theoryCombobox.currentText()}')
        if not self.liquids[self.ui.theoryCombobox.currentText()]:
            print('no such information')
        else:
            print(self.liquids[self.ui.theoryCombobox.currentText()])


if __name__ == '__main__':
    theory = '''https://www.ossila.com/pages/a-guide-to-surface-energy#:~:text=One%20of%20the%20most%20basic,
    Zisman%20model%2C%20published%20in%201964.&text=This%20model%20assumes%20that%20the,as%20the%20critical%20surface%20tension'''
    try:
        app = QtWidgets.QApplication([])
        application = MyWindow_v2()
        application.show()
        sys.exit(app.exec())
    except Exception as exc:
        print(f'Ooops, something going wrong... {exc}')
