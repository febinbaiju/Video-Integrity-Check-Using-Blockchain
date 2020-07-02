from PyQt5 import QtWidgets, uic
import sys
from Settings import *
from WebCamRecord import Ui2
from Verification import Ui3


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pbStartVideoCapture')
        self.button.clicked.connect(self.openCaptureWindow)

        self.button = self.findChild(QtWidgets.QPushButton, 'pbVerification')
        self.button.clicked.connect(self.openVerificationWindow)

        self.exitButton = self.findChild(QtWidgets.QPushButton,'pbExit')
        self.exitButton.clicked.connect(self.close)
        self.show()
    
    def openCaptureWindow(self):
        self.FT = Ui2()
        self.FT.show()

    def openVerificationWindow(self):
        self.FT = Ui3()
        self.FT.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()