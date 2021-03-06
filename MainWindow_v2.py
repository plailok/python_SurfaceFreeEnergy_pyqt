from datetime import datetime

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QGridLayout, QHBoxLayout,
                             QVBoxLayout, QMessageBox)
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp, QUrl
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

from result_widget import Ui_Form as result_ui
from setting_widget import Ui_Form as setting_ui
from v2_mainwindow import Ui_MainWindow
from dialog import Ui_Dialog
from config import *

from main_calculation import Calculation
import sys
import os


class MyWindow_v2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow_v2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        cur_dtime = datetime.now()
        self.fname = None
        self.current_date = str(cur_dtime.date())
        list_theory = [self.ui.theoryCombobox.itemText(i) for i in range(self.ui.theoryCombobox.count())]
        self.liquids = {item: [] for item in list_theory}
        self.current_index = 0
        self.image_index = None
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

        # action menu clicked
        self.ui.actionSave_Result.triggered.connect(self.save_result)
        self.ui.actionOpenProject.triggered.connect(self.load_result)
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionExit.triggered.connect(self.exit)

        self.ui.theoryButton.setEnabled(False)
        self.ui.theoryCombobox.setEnabled(False)
        self.ui.tempCombobox.setCurrentIndex(2)
        self.ui.theoryButton.clicked.connect(self.__theory_button_checked)
        self.ui.settingsButton.clicked.connect(self.__settings_button_checked)
        self.ui.measurmentButton.clicked.connect(self.__measurment_buttton_checked)
        self.ui.theoryCombobox.currentTextChanged.connect(self.__theory_chose)
        self.ui.tempCombobox.currentTextChanged.connect(self.__fullfill_table)

        self.settings_ui.calculateButton.clicked.connect(self.__collect_data_to_process)
        self.settings_ui.calculateButton.setEnabled(False)
        self.settings_ui.calculateButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.settings_ui.addliquidButton.clicked.connect(self.__add_liquid_button_clicked)

        self.result_ui.resultTable.setColumnCount(4)
        self.result_ui.resultTable.setHorizontalHeaderLabels(HORIZONTAL_HEADER_RESULT)
        self.result_ui.resultTable.setRowCount(5)

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
        ui = Ui_Dialog(LIQUIDS[self.ui.theoryCombobox.currentText()])
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
        self.settings_ui.gridLayout.setColumnStretch(0, 1)
        self.settings_ui.gridLayout.setColumnStretch(1, 1)
        for index, liquid in enumerate(self.liquids[self.ui.theoryCombobox.currentText()]):
            new_label = QtWidgets.QLabel(text=liquid)
            new_label.setFixedHeight(30)
            new_label.setSizePolicy(
                QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            self.liquids_inuse_list.append(new_label)
            new_lineedit = QtWidgets.QLineEdit()
            new_lineedit.textChanged.connect(self.check_all)
            self.lineedit_list.append(new_lineedit)
            new_lineedit.setAlignment(QtCore.Qt.AlignCenter)
            reg_ex = QRegExp("[0-9]+.[0-9]{,3}")
            input_validator = QRegExpValidator(reg_ex, new_lineedit)
            new_lineedit.setValidator(input_validator)
            self.settings_ui.gridLayout_2.addWidget(new_label, index, 0)
            self.settings_ui.gridLayout_2.addWidget(new_lineedit, index, 1)

    @pyqtSlot()
    def __fullfill_table(self):
        self.__clear_table_on_setting_layout()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.settings_ui.tableWidget.setSizePolicy(sizePolicy)
        self.settings_ui.tableWidget.setColumnCount(4)
        self.settings_ui.tableWidget.verticalHeader().hide()
        self.settings_ui.tableWidget.setHorizontalHeaderLabels(HORIZONTAL_HEADER_SETTING)
        self.settings_ui.tableWidget.setColumnWidth(0, 150)
        self.settings_ui.tableWidget.setColumnWidth(1, 100)
        self.settings_ui.tableWidget.setColumnWidth(2, 100)
        self.settings_ui.tableWidget.setColumnWidth(3, 100)
        if self.liquids[self.ui.theoryCombobox.currentText()]:
            liquids = self.liquids[self.ui.theoryCombobox.currentText()]
            cur_temp = self.ui.tempCombobox.currentText()[:-1]
            self.settings_ui.tableWidget.setRowCount(len(liquids))
            for index, liquid in enumerate(liquids):
                item0 = QTableWidgetItem(liquid)
                item0.setTextAlignment(QtCore.Qt.AlignCenter)
                item1 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][1]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][0]))
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item3 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][-1]))
                item3.setTextAlignment(QtCore.Qt.AlignCenter)

                self.settings_ui.tableWidget.setItem(index, 0, item0)
                self.settings_ui.tableWidget.setItem(index, 1, item1)
                self.settings_ui.tableWidget.setItem(index, 2, item2)
                self.settings_ui.tableWidget.setItem(index, 3, item3)

    @pyqtSlot()
    def __delete_widgets_on_setting_layout(self):
        for index in range(self.settings_ui.gridLayout_2.count()):
            self.settings_ui.gridLayout_2.itemAt(index).widget().deleteLater()

    @pyqtSlot()
    def __clear_table_on_setting_layout(self):
        self.settings_ui.tableWidget.clear()
        self.settings_ui.tableWidget.setRowCount(0)

    def __clear_table_on_result_layout(self):
        self.result_ui.resultTable.clear()
        self.result_ui.resultTable.setRowCount(0)

    @pyqtSlot()
    def __theory_chose(self):
        self.settings_ui.calculateButton.setStyleSheet("color: rgb(255, 0, 0);")
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
        cur_temp = self.ui.tempCombobox.currentText()[:-1]
        method = self.ui.theoryCombobox.currentText()

        for index, line in enumerate(self.lineedit_list):
            polar = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][1]
            dispersive = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][0]
            if method == 'van-Oss':
                acid = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][2]
                base = TEMPERATURE[self.liquids_inuse_list[index].text()][cur_temp][3]
                self.to_process.append(
                    (self.liquids_inuse_list[index].text(), float(line.text()), dispersive, polar, acid, base))
            elif method == 'Owens-Wendt' or method == 'Fowkes':
                self.to_process.append(
                    (self.liquids_inuse_list[index].text(), float(line.text()), dispersive, polar))
            else:
                self.to_process.append((self.liquids_inuse_list[index].text(), float(line.text()), dispersive + polar))
            self.image_index = 0 if self.image_index is None else self.image_index + 1
        self.__process()

    def __process(self):
        math = Calculation(to_process=self.to_process,
                           name=self.ui.theoryCombobox.currentText(),
                           index=self.image_index)
        try:
            math.calculate()
        except ValueError as v_error:
            self._save_to_log(v_error)
            self.__raise_error()
        else:
            self.result.append(math.result)
            self._add_to_result_table()
            self._add_plot()

    def _save_to_log(self, *args):
        with open('error.log', mode='a+', encoding='utf8') as flog:
            line = f'{datetime.now()}:{[arg for arg in args]}\n'
            flog.write(line)

    @pyqtSlot()
    def __raise_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Hello! It seems like something going wrong =( "
                    "If you need details look errors.log file in the source ")
        msg.setInformativeText("Result that we try to obtaine is bullsheety, check the data twice!")
        msg.setWindowTitle("Calculation Error")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    @pyqtSlot()
    def _add_plot(self):
        if self.ui.theoryCombobox.currentText() != 'Fowkes':
            name = self.ui.theoryCombobox.currentText()
            pixmap = QPixmap(f'result/{self.current_date}_{name}({self.image_index}).png')
            self.result_ui.plotLabel.setPixmap(pixmap)
        else:
            self.result_ui.plotLabel.setText(f'No plot for this "{self.ui.theoryCombobox.currentText()}"method!')

    @pyqtSlot()
    def _add_to_result_table(self):
        align = QtCore.Qt.AlignCenter
        if len(self.result) > self.current_index:
            new_result = self.result[-1]
            self.result_ui.resultTable.setRowCount(len(self.result)) if len(
                self.result) > 4 else self.result_ui.resultTable.setRowCount(5)
            try:
                item0 = QTableWidgetItem(str(round(new_result[0], 3)))
                item1 = QTableWidgetItem(str(round(new_result[1], 3)))
            except Exception:
                item0 = QTableWidgetItem(str(new_result[0]))
                item1 = QTableWidgetItem(str(new_result[1]))
            finally:
                item0.setTextAlignment(align)
                self.result_ui.resultTable.setItem(self.current_index, 0, item0)
                item1.setTextAlignment(align)
                self.result_ui.resultTable.setItem(self.current_index, 1, item1)
                item2 = QTableWidgetItem(str(round(new_result[2], 3)))
                item2.setTextAlignment(align)
                self.result_ui.resultTable.setItem(self.current_index, 2, item2)
                item3 = QTableWidgetItem(str(new_result[3]))
                item3.setTextAlignment(align)
                self.result_ui.resultTable.setItem(self.current_index, 3, item3)
                self.current_index += 1

    @pyqtSlot()
    def check_all(self):
        a = [line.text() for line in self.lineedit_list if line.text() != '']
        if len(a) == self.settings_ui.gridLayout_2.count() // 2:
            self.settings_ui.calculateButton.setStyleSheet("color: rgb(250, 120, 255);")
            self.settings_ui.calculateButton.setEnabled(True)
        else:
            self.settings_ui.calculateButton.setStyleSheet("color: rgb(255, 0, 0);")
            self.settings_ui.calculateButton.setEnabled(False)

    @pyqtSlot()
    def save_result(self):
        '''
        Save result of current measurment as .txt file
        '''
        home_dir = os.getcwd()
        open_dir = f'{home_dir}/result'
        if not self.fname:
            self.fname = QFileDialog.getSaveFileName(self, 'Open file', open_dir, filter='Text files (*.txt)')
        try:
            with open(self.fname[0], 'a+') as f:
                for measurment in self.result:
                    f.write('\n')
                    for value in measurment:
                        f.write(f'{str(value)},')
        except Exception as exc:
            print(exc)
            pass

    @pyqtSlot()
    def load_result(self):
        '''
        Save result of current measurment as .txt file
        '''
        result_dir = os.getcwd()
        self.fname = QFileDialog.getOpenFileNames(self, 'Open file', result_dir, filter='Text files (*.txt)')
        with open(self.fname[0][-1], 'r+') as f:
            result = [value[:-1] for value in f.readlines() if value != '\n']
            for value in result:
                to_read = value.split(sep=',')
                self.result.append(to_read) if len(to_read) == 4 else self.result.append(to_read[:-1])
        self.current_index = 0
        self.__measurment_buttton_checked()
        self.__to_table()

    def __to_table(self):
        self.result_ui.resultTable.setColumnCount(4)
        self.result_ui.resultTable.setHorizontalHeaderLabels(HORIZONTAL_HEADER_RESULT)
        self.result_ui.resultTable.setRowCount(5)
        self.result_ui.resultTable.horizontalHeader().setStretchLastSection(True)
        align = QtCore.Qt.AlignCenter
        self.result_ui.resultTable.setRowCount(len(self.result))
        for value in self.result:
            item0 = QTableWidgetItem(value[0][:4])
            item1 = QTableWidgetItem(value[1][:4])
            item2 = QTableWidgetItem(value[2][:4])
            item3 = QTableWidgetItem(value[3])

            item0.setTextAlignment(align)
            item1.setTextAlignment(align)
            item2.setTextAlignment(align)
            item3.setTextAlignment(align)

            self.result_ui.resultTable.setItem(self.current_index, 0, item0)
            self.result_ui.resultTable.setItem(self.current_index, 1, item1)
            self.result_ui.resultTable.setItem(self.current_index, 2, item2)
            self.result_ui.resultTable.setItem(self.current_index, 3, item3)
            self.current_index += 1

    @pyqtSlot()
    def new(self):
        self.__delete_widgets_on_setting_layout()
        self.__clear_table_on_setting_layout()
        self.__clear_table_on_result_layout()

        self.result_ui.resultTable.setColumnCount(4)
        self.result_ui.resultTable.setHorizontalHeaderLabels(HORIZONTAL_HEADER_RESULT)
        self.result_ui.resultTable.setRowCount(5)

        self.result_ui.plotLabel.setText('Plot will be here')

    @pyqtSlot()
    def exit(self):
        self.save_result()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow_v2()
    application.show()
    sys.exit(app.exec())
