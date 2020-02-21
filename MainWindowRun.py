from PyQt5 import QtWidgets, uic
from WebCamRecord import Ui2
import sys
from Settings import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pbStartVideoCapture')
        self.button.clicked.connect(self.openCaptureWindow)

        self.exitButton = self.findChild(QtWidgets.QPushButton,'pbExit')
        self.exitButton.clicked.connect(self.close)
        self.show()
    
    def openCaptureWindow(self):
        self.w = Ui2()
        self.w.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()