from PyQt5 import QtWidgets, uic
import sys
from Settings import *
from sha import hmacsha_file
from app import *
import os
from eccencrypt import get_encrypted_key

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
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","AVI Files (*.avi)", options=options)
        if filePath:
            self.filelabel = self.findChild(QtWidgets.QLabel,'lblfilename2')
            self.filelabel.setText("Processing...")
            print("Processing....")
            h_filename = os.path.basename(filePath)
            h_filepath = filePath
            ecc_encryption = get_encrypted_key()
            h_pubkey = ecc_encryption[0]
            h_key = ecc_encryption[1]
            print("KEY USED: ", h_key[0:15])
            h_file = hmacsha_file(filePath, h_key)
            block = Blockchain()  # Blockchain implementation
            block.add(h_filename, h_filepath, h_pubkey, h_file)
            self.filelabel.setText("Added to Records...")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui4()
    app.exec_()