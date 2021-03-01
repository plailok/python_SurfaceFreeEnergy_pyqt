from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, QRegExp
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
from v1_mainwindow import Ui_MainWindow
from SDF_dialog import Ui_Dialog
from main_calculation import Calculation
import sys

HELP = []
LIQUIDS = ['Water', 'Formamide', 'Ethylene Glycole', '\u03B1-bromnaphtalene']
POSSIBLE_TEMPERATURES = ['21', '22', '23', '24', '25', '26']
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


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.liquids = {}
        self.line = None
        self.set_theory_combobox()
        # self.build_input_frame()
        self.ui.addLiquidsButton.clicked.connect(self.add_new_liquids)
        self.ui.pushButton.clicked.connect(self.store_result)

    def __create_stable_widgets(self):

        '''
        Create widget for future use
        '''
        self.add_button = QtWidgets.QPushButton(self.ui.ProbeLiquids)
        self.add_button.setText('Add Liquids')
        self.add_button.clicked.connect(self.add_new_liquids)

        self.lineedit = QtWidgets.QLineEdit(self.ui.ProbeLiquids)
        self.lineedit.setEnabled(False)
        self.lineedit.setText('Value')
        self.lineedit.setAlignment(Qt.AlignCenter)

        self.temperature_combobox = QtWidgets.QComboBox(self.ui.ProbeLiquids)
        self.temperature_combobox.addItems(POSSIBLE_TEMPERATURES)
        self.temperature_combobox.setCurrentIndex(2)

    def set_theory_combobox(self):
        self.combobox_changed()
        self.ui.theoryCombobox.currentTextChanged.connect(self.combobox_changed)

    def combobox_changed(self):
        pixmap = QPixmap(f'equation{self.ui.theoryCombobox.currentIndex()}.png')
        self.ui.pictureLabel.setPixmap(pixmap)

    @pyqtSlot()
    def store_result(self):
        self.result = []
        for line in self.line:
            params = TEMPERATURE[line[0].text()][self.ui.tempCombobox.currentText()]
            self.result.append((line[0].text(), line[1].text(), params[0], params[1]))
        self.calc = Calculation(to_process=self.result)
        self.calc.calculate()

    # def build_input_frame(self):
    #     list = ['Liquid', 'Polar', 'Non-Polar']
    #     for i in range(3):
    #         item = QTableWidgetItem(list[i])
    #         print(item)
    #         self.ui.tableWidget.setItem(0, i, item)

    @pyqtSlot()
    def add_new_liquids(self):
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
    def __fullfill_table(self):
        if self.liquids[self.ui.theoryCombobox.currentText()]:
            cur_temp = self.ui.tempCombobox.currentText()
            self.ui.tableWidget.setRowCount(len(self.liquids[self.ui.theoryCombobox.currentText()]))
            for index, liquid in enumerate(self.liquids[self.ui.theoryCombobox.currentText()]):
                item0 = QTableWidgetItem(liquid)
                item1 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][0]))
                item2 = QTableWidgetItem(str(TEMPERATURE[liquid][cur_temp][1]))
                self.ui.tableWidget.setItem(index, 0, item0)
                self.ui.tableWidget.setItem(index, 1, item1)
                self.ui.tableWidget.setItem(index, 2, item2)

    @pyqtSlot()
    def __create_input_bar(self):
        self.probe = []
        self.inputs = []
        if self.line is None:
            # line[i][0] - name of liquid
            # line[i][1] - value from user
            self.line = []
        else:
            self.clearLayout(self.ui.gridLayout_5)
        for index, liquid in enumerate(self.liquids[self.ui.theoryCombobox.currentText()]):
            new_label = QtWidgets.QLabel(self.ui.ProbeLiquids)
            new_input = QtWidgets.QLineEdit(self.ui.ProbeLiquids)
            reg_ex = QRegExp("[0-9]+.[0-9]{,3}")
            input_validator = QRegExpValidator(reg_ex, new_input)
            new_input.setValidator(input_validator)
            self.line.append((new_label, new_input))
            new_label.setObjectName(liquid)
            new_input.setObjectName(f'{liquid}{index}')
            new_label.setText(liquid)
            self.probe.append((new_label.text(), new_input.text()))
            new_label.setAlignment(Qt.AlignCenter)
        for index, item in enumerate(self.line):
            self.ui.gridLayout_5.addWidget(item[0], index + 1, 0, 1, 1)
            self.ui.gridLayout_5.addWidget(item[1], index + 1, 1, 1, 1)

    @pyqtSlot()
    def remove_line(self):
        self.ui.gridLayout_5.getItemPosition()
        pass

    @pyqtSlot()
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.__create_stable_widgets()
        self.ui.gridLayout_5.addWidget(self.add_button, 0, 0, 1, 1)
        self.ui.gridLayout_5.addWidget(self.lineedit, 0, 1, 1, 1)
        self.ui.gridLayout_5.addWidget(self.temperature_combobox, 0, 2, 1, 1)

    def add_to_table(self):
        pass

    def click_start(self):
        pass

    def click_save_result(self):
        pass

    def click_save_plot(self):
        pass


try:
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
except Exception as exc:
    print(f'Ooops, something going wrong... {exc}')
