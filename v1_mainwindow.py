# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 835)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Constants = QtWidgets.QGroupBox(self.centralwidget)
        self.Constants.setObjectName("Constants")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Constants)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.Constants)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Constants, 2, 0, 1, 1)
        self.ChooseTheory = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseTheory.sizePolicy().hasHeightForWidth())
        self.ChooseTheory.setSizePolicy(sizePolicy)
        self.ChooseTheory.setObjectName("ChooseTheory")
        self.pictureLabel = QtWidgets.QLabel(self.ChooseTheory)
        self.pictureLabel.setGeometry(QtCore.QRect(12, 117, 150, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureLabel.sizePolicy().hasHeightForWidth())
        self.pictureLabel.setSizePolicy(sizePolicy)
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureLabel.setObjectName("pictureLabel")
        self.theoryCombobox = QtWidgets.QComboBox(self.ChooseTheory)
        self.theoryCombobox.setGeometry(QtCore.QRect(13, 29, 251, 22))
        self.theoryCombobox.setMaxVisibleItems(4)
        self.theoryCombobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.theoryCombobox.setObjectName("theoryCombobox")
        self.theoryCombobox.addItem("")
        self.theoryCombobox.addItem("")
        self.theoryCombobox.addItem("")
        self.theoryCombobox.addItem("")
        self.theoryLabel = QtWidgets.QLabel(self.ChooseTheory)
        self.theoryLabel.setGeometry(QtCore.QRect(260, 30, 131, 16))
        self.theoryLabel.setScaledContents(True)
        self.theoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.theoryLabel.setObjectName("theoryLabel")
        self.gridLayout.addWidget(self.ChooseTheory, 0, 0, 1, 1)
        self.ProbeLiquids = QtWidgets.QGroupBox(self.centralwidget)
        self.ProbeLiquids.setObjectName("ProbeLiquids")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ProbeLiquids)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.addLiquidsButton = QtWidgets.QPushButton(self.ProbeLiquids)
        self.addLiquidsButton.setObjectName("addLiquidsButton")
        self.gridLayout_5.addWidget(self.addLiquidsButton, 0, 0, 1, 1)
        self.valuelineedit = QtWidgets.QLineEdit(self.ProbeLiquids)
        self.valuelineedit.setEnabled(False)
        self.valuelineedit.setMouseTracking(False)
        self.valuelineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.valuelineedit.setObjectName("valuelineedit")
        self.gridLayout_5.addWidget(self.valuelineedit, 0, 1, 1, 1)
        self.tempCombobox = QtWidgets.QComboBox(self.ProbeLiquids)
        self.tempCombobox.setObjectName("tempCombobox")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.gridLayout_5.addWidget(self.tempCombobox, 0, 2, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 5)
        self.gridLayout.addWidget(self.ProbeLiquids, 1, 0, 1, 1)
        self.buttonsbox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonsbox.setObjectName("buttonsbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.buttonsbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.buttonsbox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.buttonsbox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.buttonsbox, 3, 0, 1, 2)
        self.plotFrame = QtWidgets.QGroupBox(self.centralwidget)
        self.plotFrame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plotFrame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.plotFrame.setObjectName("plotFrame")
        self.gridLayout.addWidget(self.plotFrame, 0, 1, 3, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 26))
        self.menubar.setObjectName("menubar")
        self.menumain = QtWidgets.QMenu(self.menubar)
        self.menumain.setObjectName("menumain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumain.menuAction())

        self.retranslateUi(MainWindow)
        self.tempCombobox.setCurrentIndex(2)
        self.theoryCombobox.currentTextChanged['QString'].connect(self.ProbeLiquids.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Constants.setTitle(_translate("MainWindow", "Constants"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Liquids"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Polar"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Non-Polar"))
        self.ChooseTheory.setTitle(_translate("MainWindow", "Choose theory"))
        self.pictureLabel.setText(_translate("MainWindow", "Owenst-Wendt and Fowks"))
        self.theoryCombobox.setItemText(0, _translate("MainWindow", "Zisman"))
        self.theoryCombobox.setItemText(1, _translate("MainWindow", "van Oss Acid-Base"))
        self.theoryCombobox.setItemText(2, _translate("MainWindow", "Owens and Wendt"))
        self.theoryCombobox.setItemText(3, _translate("MainWindow", "Fowkes"))
        self.theoryLabel.setText(_translate("MainWindow", "Theory"))
        self.ProbeLiquids.setTitle(_translate("MainWindow", "Probe Liquids"))
        self.addLiquidsButton.setText(_translate("MainWindow", "Add Liquids"))
        self.valuelineedit.setInputMask(_translate("MainWindow", "Value"))
        self.valuelineedit.setText(_translate("MainWindow", "Value"))
        self.tempCombobox.setCurrentText(_translate("MainWindow", "25"))
        self.tempCombobox.setItemText(0, _translate("MainWindow", "23"))
        self.tempCombobox.setItemText(1, _translate("MainWindow", "24"))
        self.tempCombobox.setItemText(2, _translate("MainWindow", "25"))
        self.tempCombobox.setItemText(3, _translate("MainWindow", "26"))
        self.tempCombobox.setItemText(4, _translate("MainWindow", "27"))
        self.buttonsbox.setTitle(_translate("MainWindow", "buttons"))
        self.pushButton.setText(_translate("MainWindow", "Calibrate"))
        self.pushButton_2.setText(_translate("MainWindow", "SaveResult"))
        self.plotFrame.setTitle(_translate("MainWindow", "Results"))
        self.menumain.setTitle(_translate("MainWindow", "main"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
