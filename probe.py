import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi('LoginPage.ui', self)

class RegisterPage(QDialog):
    def __init__(self):
        super(RegisterPage, self).__init__()
        loadUi('RegisterPage.ui', self)


class HomePage(QDialog):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi('HomePage.ui', self)
        self.btnLoginPage.clicked.connect(self.executeLoginPage)
        self.btnRegisterPage.clicked.connect(self.executeRegisterPage)

app = QApplication(sys.argv)
widget = HomePage()
widget.show()
sys.exit(app.exec_())