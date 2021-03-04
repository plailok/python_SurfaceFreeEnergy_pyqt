# #!/usr/bin/python

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser


#
#
# class MyBrowser(QWebPage):
#     ''' Settings for the browser.'''
#
#     def userAgentForUrl(self, url):
#         ''' Returns a User Agent that will be seen by the website. '''
#         return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
#
#
# class Browser(QWebView):
#     def __init__(self):
#         # QWebView
#         self.view = QWebView.__init__(self)
#         # self.view.setPage(MyBrowser())
#         self.setWindowTitle('Loading...')
#         self.titleChanged.connect(self.adjustTitle)
#         # super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&amp;)"), self.adjustTitle)
#
#     def load(self, url):
#         self.setUrl(QUrl(url))
#
#     def adjustTitle(self):
#         self.setWindowTitle(self.title())
#
#     def disableJS(self):
#         settings = QWebSettings.globalSettings()
#         settings.setAttribute(QWebSettings.JavascriptEnabled, False)
#
#
# app = QApplication(sys.argv)
# view = Browser()
# view.showMaximized()
# view.load("https://www.kruss-scientific.com/en/know-how/glossary/oss-and-good-method")
# app.exec_()

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.loadPage()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')
        self.show()

    def loadPage(self):
        with open('theories/Refractive index - Wikipedia.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
