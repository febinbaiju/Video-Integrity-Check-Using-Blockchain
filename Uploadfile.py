from PyQt5 import QtWidgets, uic
import sys
from Settings import *
from sha import hmacsha_file
from app import *

class Ui4(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui4, self).__init__()
        uic.loadUi('uploadfile.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'pbChoose2')
        self.button.clicked.connect(self.openFileChooser)

        self.exitButton = self.findChild(QtWidgets.QPushButton,'pbExit3')
        self.exitButton.clicked.connect(self.close)
        self.show()
    
    def openFileChooser(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","AVI Files (*.avi)", options=options)
        if fileName:
            self.filelabel = self.findChild(QtWidgets.QLabel,'lblfilename2')
            flag = False
            block = Blockchain()
            hashes = block.getHashes()
            for key in block.getKeys():
                check = hmacsha_file(fileName,key)
                if check in hashes:
                    flag = True
                    break
            if flag:
                self.filelabel.setText("VIDEO VERIFIED")
            else:
                self.filelabel.setText("TAMPERED VIDEO")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui4()
    app.exec_()