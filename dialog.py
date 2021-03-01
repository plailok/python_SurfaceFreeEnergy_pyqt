from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from SDF_dialog import Ui_Dialog
import sys


class DialogWindow(QtWidgets.QDialog):

    def __init__(self, catcher):
        super(DialogWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.list_to_return = catcher
        self.ui.setupUi(self)

        self.ui.AddButton.clicked.connect(self.add_button)
        self.ui.RemoveButton.clicked.connect(self.reject)
        self.ui.OKButton.clicked.connect(self.accept)
        self.ui.CancelButton.clicked.connect(self.cancel_button)
        self.ui.allList.itemDoubleClicked.connect(self.move_to_mylist)
        self.ui.myList.itemDoubleClicked.connect(self.move_to_alllist)

        self.window()

    def add_button(self):
        if self.ui.allList.currentRow() != -1:
            # print(self.ui.allList.currentRow())
            self.move_to_mylist()
        else:
            self.ui.allList.setCurrentRow(0)
            self.move_to_mylist()

    def remove_button(self):
        if self.ui.myList.currentRow() != -1:
            # print(self.ui.myList.currentRow())
            self.move_to_alllist()
        else:
            self.ui.myList.setCurrentRow(0)
            self.move_to_alllist()

    def move_to_mylist(self):
        row = self.ui.allList.currentRow()
        self.item = self.ui.allList.takeItem(row)
        self.ui.myList.addItem(self.item)

    def move_to_alllist(self):
        row = self.ui.myList.currentRow()
        self.item = self.ui.myList.takeItem(row)
        self.ui.allList.addItem(self.item)

# try:
#     app = QtWidgets.QApplication([])
#     application = DialogWindow()
#     application.show()
#     sys.exit(app.exec())
# except Exception as exc:
#     print(f'Ooops, something going wrong... {exc}')
