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

THEORY = '''https://www.ossila.com/pages/a-guide-to-surface-energy#:~:text=One%20of%20the%20most%20basic, 
Zisman%20model%2C%20published%20in%201964.&text=This%20model%20assumes%20that%20the,
as%20the%20critical%20surface%20tension '''
LIQUIDS = ['Water', 'Formamide', 'Ethylene Glycole', '\u03B1-bromnaphtalene']
HORIZONTAL_HEADER_SETTING = ['Liquid', 'Polar', 'Dispersive']
HORIZONTAL_HEADER_RESULT = ['Dispersive', 'Polar', 'Total', 'Method']

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
        self.curent_index = 0
        self.line = None
        self.__setupUI()
        self.result = []

    @pyqtSlot()
    def __setupUI(self):
        # add WebView widget
        self.web = QWebView()
        self.web.setUrl(QUrl(THEORY))
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
        self.ui.theoryButton.clicked.connect(self.__theory_button_checked)
        self.ui.settingsButton.clicked.connect(self.__settings_button_checked)
        self.ui.measurmentButton.clicked.connect(self.__measurment_buttton_checked)
        self.ui.theoryCombobox.currentTextChanged.connect(self.__theory_chose)

        self.settings_ui.calculateButton.clicked.connect(self.__collect_data_to_process)
        self.settings_ui.calculateButton.setEnabled(False)
        self.settings_ui.addliquidButton.clicked.connect(self.__add_liquid_button_clicked)

        self.result_ui.resultTabel.setColumnCount(4)
        self.result_ui.resultTabel.setHorizontalHeaderLabels(HORIZONTAL_HEADER_RESULT)
        self.result_ui.resultTabel.setRowCount(5)

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
    def __add_liquid_button_clicked(self):
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
        self.lineedit_list = []
        self.liquids_inuse_list = []
        self.__delete_widgets_on_setting_layout()
        self.settings_ui.liquidsGridLayout.setColumnStretch(0, 5)
        self.settings_ui.liquidsGridLayout.setColumnStretch(1, 2)
        for index, liquid in enumerate(self.liquids[self.ui.theoryCombobox.currentText()]):
            new_label = QtWidgets.QLabel(text=liquid)
            self.liquids_inuse_list.append(new_label)
            new_label.setFixedHeight(30)
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            new_lineedit = QtWidgets.QLineEdit()
            new_lineedit.editingFinished.connect(self.check_all)
            self.lineedit_list.append(new_lineedit)
            new_lineedit.setAlignment(QtCore.Qt.AlignCenter)
            reg_ex = QRegExp("[0-9]+.[0-9]{,3}")
            input_validator = QRegExpValidator(reg_ex, new_lineedit)
            new_lineedit.setValidator(input_validator)
            self.settings_ui.liquidsGridLayout.addWidget(new_label, index, 0)
            self.settings_ui.liquidsGridLayout.addWidget(new_lineedit, index, 1)

    @pyqtSlot()
    def __fullfill_table(self):
        self.__clear_table_on_setting_layout()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.settings_ui.tableWidget.setSizePolicy(sizePolicy)
        self.settings_ui.tableWidget.setColumnCount(3)
        self.settings_ui.tableWidget.verticalHeader().hide()
        self.settings_ui.tableWidget.setHorizontalHeaderLabels(HORIZONTAL_HEADER_SETTING)
        self.settings_ui.tableWidget.setColumnWidth(0, 260)
        if self.liquids[self.ui.theoryCombobox.currentText()]:
            liquids = self.liquids[self.ui.theoryCombobox.currentText()]
            cur_temp = self.ui.tempCombobox.currentText()
            self.settings_ui.tableWidget.setRowCount(len(liquids))
            for index, liquid in enumerate(liquids):
                item0 = QTableWidgetItem(liquid)
                item0.setTextAlignment(QtCore.Qt.AlignCenter)
                item1 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][1]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][0]))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)

                self.settings_ui.tableWidget.setItem(index, 0, item0)
                self.settings_ui.tableWidget.setItem(index, 1, item1)
                self.settings_ui.tableWidget.setItem(index, 2, item2)

    @pyqtSlot()
    def __delete_widgets_on_setting_layout(self):
        for index in range(self.settings_ui.liquidsGridLayout.count()):
            self.settings_ui.liquidsGridLayout.itemAt(index).widget().deleteLater()

    @pyqtSlot()
    def __clear_table_on_setting_layout(self):
        self.settings_ui.tableWidget.clear()
        self.settings_ui.tableWidget.setRowCount(0)

    @pyqtSlot()
    def __theory_chose(self):
        try:
            self.liquids[self.ui.theoryCombobox.currentText()]
        except Exception:
            self.liquids[self.ui.theoryCombobox.currentText()] = []
        finally:
            self.__delete_widgets_on_setting_layout()
            self.__clear_table_on_setting_layout()
            self.__create_input_bar()
            self.__fullfill_table()

    def __collect_data_to_process(self):
        self.to_process = []
        cur_temp = self.ui.tempCombobox.currentText()
        for index, line in enumerate(self.lineedit_list):
            polar = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][1]
            dispersive = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][0]
            self.to_process.append((self.liquids_inuse_list[index].text(), float(line.text()), dispersive, polar))
        self.math = Calculation(self.to_process)
        self.math.calculate()
        self.result.append(self.math.result)
        print(self.to_process)
        self._add_to_result_table()
        self._add_plot()

    def _add_plot(self):
        pixmap = QPixmap('result_plot.png')
        self.result_ui.plotLabel.setPixmap(pixmap)

    def _add_to_result_table(self):
        if len(self.result) > self.curent_index:
            new_result = self.result[-1]
            print(new_result)
            item0 = QTableWidgetItem(str(round(new_result[0], 3)))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            self.result_ui.resultTabel.setItem(self.curent_index, 0, item0)
            item1 = QTableWidgetItem(str(round(new_result[1], 3)))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            self.result_ui.resultTabel.setItem(self.curent_index, 1, item1)
            item2 = QTableWidgetItem(str(round(new_result[2], 3)))
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            self.result_ui.resultTabel.setItem(self.curent_index, 2, item2)
            item3 = QTableWidgetItem(self.ui.theoryCombobox.currentText())
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            self.result_ui.resultTabel.setItem(self.curent_index, 3, item3)
            self.curent_index += 1

    def check_all(self):
        print(self.curent)
        current = 0
        for line in self.lineedit_list:
            if line.text() != '':
                current += 1
        if current == len(self.lineedit_list):
            self.settings_ui.calculateButton.setEnabled(True)
        else:
            self.settings_ui.calculateButton.setEnabled(False)


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication([])
        application = MyWindow_v2()
        application.show()
        sys.exit(app.exec())
    except Exception as exc:
        print(f'Ooops, something going wrong... {exc}')
