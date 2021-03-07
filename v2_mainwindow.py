# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces/MainWindow_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 608)
        MainWindow.setStyleSheet("QFrame{\n"
"    background-color: rgb(120, 120, 120);\n"
"    border-radius: 25px;\n"
"}\n"
"QMainWindow{\n"
"    background-color:rgb(255,255,255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ButtonsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ButtonsFrame.setMinimumSize(QtCore.QSize(140, 480))
        self.ButtonsFrame.setMaximumSize(QtCore.QSize(200, 16377))
        self.ButtonsFrame.setStyleSheet("QPushButton {\n"
"    color: rgb(250, 120, 255);\n"
"    background-color: grey;\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 25px;\n"
"    border-color: rgb(255,120,200);\n"
"    font: bold 14px;\n"
"    min-width: 140px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}\n"
"QFrame{\n"
"    background-color: rgb(120, 120, 120);\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.ButtonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsFrame.setObjectName("ButtonsFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.ButtonsFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.settingsButton = QtWidgets.QPushButton(self.ButtonsFrame)
        self.settingsButton.setMinimumSize(QtCore.QSize(158, 120))
        self.settingsButton.setStyleSheet("")
        self.settingsButton.setCheckable(True)
        self.settingsButton.setAutoExclusive(True)
        self.settingsButton.setDefault(False)
        self.settingsButton.setFlat(False)
        self.settingsButton.setObjectName("settingsButton")
        self.gridLayout.addWidget(self.settingsButton, 1, 0, 1, 1)
        self.theoryButton = QtWidgets.QPushButton(self.ButtonsFrame)
        self.theoryButton.setMinimumSize(QtCore.QSize(158, 120))
        self.theoryButton.setStyleSheet("")
        self.theoryButton.setCheckable(True)
        self.theoryButton.setChecked(True)
        self.theoryButton.setAutoExclusive(True)
        self.theoryButton.setAutoDefault(False)
        self.theoryButton.setDefault(False)
        self.theoryButton.setFlat(False)
        self.theoryButton.setObjectName("theoryButton")
        self.gridLayout.addWidget(self.theoryButton, 0, 0, 1, 1)
        self.measurmentButton = QtWidgets.QPushButton(self.ButtonsFrame)
        self.measurmentButton.setMinimumSize(QtCore.QSize(158, 120))
        self.measurmentButton.setSizeIncrement(QtCore.QSize(100, 0))
        self.measurmentButton.setStyleSheet("")
        self.measurmentButton.setCheckable(True)
        self.measurmentButton.setAutoExclusive(True)
        self.measurmentButton.setObjectName("measurmentButton")
        self.gridLayout.addWidget(self.measurmentButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.ButtonsFrame, 0, 0, 1, 1)
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setMinimumSize(QtCore.QSize(700, 480))
        self.MainFrame.setToolTipDuration(1)
        self.MainFrame.setStyleSheet("QFrame{\n"
"    backgroundcolor: rgb(255, 255, 0)}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 5px 2px 5px 2px;\n"
"    min-width: 300px;\n"
"    font: bold, 14px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MainFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.innerMainFrame = QtWidgets.QFrame(self.MainFrame)
        self.innerMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.innerMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.innerMainFrame.setObjectName("innerMainFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.innerMainFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ctywLabel = QtWidgets.QLabel(self.innerMainFrame)
        self.ctywLabel.setStyleSheet("QLabel{\n"
"    color:rgb(250, 120, 255);\n"
"    background-color: rgb(80, 80, 80);\n"
"    min-width: 220px;\n"
"    max-width:250px;\n"
"    border-radius: 10px;\n"
"    font: bold, 14px\n"
"}")
        self.ctywLabel.setScaledContents(True)
        self.ctywLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ctywLabel.setObjectName("ctywLabel")
        self.gridLayout_4.addWidget(self.ctywLabel, 0, 0, 1, 1)
        self.theoryCombobox = QtWidgets.QComboBox(self.innerMainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theoryCombobox.sizePolicy().hasHeightForWidth())
        self.theoryCombobox.setSizePolicy(sizePolicy)
        self.theoryCombobox.setMinimumSize(QtCore.QSize(306, 30))
        self.theoryCombobox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.theoryCombobox.setAutoFillBackground(False)
        self.theoryCombobox.setStyleSheet("QFrame{\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 2px;\n"
"}\n"
"QComboBox{\n"
"    max-width:450px}\n"
"\n"
"")
        self.theoryCombobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.theoryCombobox.setObjectName("theoryCombobox")
        self.theoryCombobox.addItem("")
        self.theoryCombobox.addItem("")
        self.theoryCombobox.addItem("")
        self.gridLayout_4.addWidget(self.theoryCombobox, 0, 1, 1, 1)
        self.tempCombobox = QtWidgets.QComboBox(self.innerMainFrame)
        self.tempCombobox.setStyleSheet("QComboBox{\n"
"    min-width: 50px;\n"
"    max-width: 100px\n"
"}\n"
"QFrame{\n"
"    background-color: white;\n"
"}")
        self.tempCombobox.setObjectName("tempCombobox")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.tempCombobox.addItem("")
        self.gridLayout_4.addWidget(self.tempCombobox, 0, 3, 1, 1)
        self.theorysFrame = QtWidgets.QFrame(self.innerMainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theorysFrame.sizePolicy().hasHeightForWidth())
        self.theorysFrame.setSizePolicy(sizePolicy)
        self.theorysFrame.setStyleSheet("border-radius: 15px")
        self.theorysFrame.setObjectName("theorysFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.theorysFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4.addWidget(self.theorysFrame, 1, 0, 1, 4)
        self.tempLabel = QtWidgets.QLabel(self.innerMainFrame)
        self.tempLabel.setStyleSheet("QLabel{\n"
"    color:rgb(250, 120, 255);\n"
"    background-color: rgb(80, 80, 80);\n"
"    min-width: 240px;\n"
"    max-width:250px;\n"
"    border-radius: 10px;\n"
"    font: bold, 14px\n"
"}")
        self.tempLabel.setScaledContents(True)
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.gridLayout_4.addWidget(self.tempLabel, 0, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 4)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 10)
        self.gridLayout_3.addWidget(self.innerMainFrame, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.MainFrame, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.resultGridLayout = QtWidgets.QGridLayout()
        self.resultGridLayout.setObjectName("resultGridLayout")
        self.gridLayout_6.addLayout(self.resultGridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settingsButton.setText(_translate("MainWindow", "SETTINGS"))
        self.theoryButton.setText(_translate("MainWindow", "READ THEORY "))
        self.measurmentButton.setText(_translate("MainWindow", "MEASURMENT"))
        self.ctywLabel.setText(_translate("MainWindow", "Choose Theory You Want =>"))
        self.theoryCombobox.setItemText(0, _translate("MainWindow", "Van-Oss"))
        self.theoryCombobox.setItemText(1, _translate("MainWindow", "Zeisman"))
        self.theoryCombobox.setItemText(2, _translate("MainWindow", "Groompler"))
        self.tempCombobox.setItemText(0, _translate("MainWindow", "23"))
        self.tempCombobox.setItemText(1, _translate("MainWindow", "24"))
        self.tempCombobox.setItemText(2, _translate("MainWindow", "25"))
        self.tempCombobox.setItemText(3, _translate("MainWindow", "26"))
        self.tempCombobox.setItemText(4, _translate("MainWindow", "27"))
        self.tempCombobox.setItemText(5, _translate("MainWindow", "28"))
        self.tempLabel.setText(_translate("MainWindow", "Chose Temperature You Want =>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())