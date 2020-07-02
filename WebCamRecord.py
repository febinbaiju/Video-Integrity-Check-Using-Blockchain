from PyQt5 import QtWidgets, uic
import sys
import cv2
import calendar
import time
from PyQt5.QtWidgets import  QApplication,QWidget, QLabel
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon,QImage, QPixmap
from Settings import *
from sha import *
from app import *
from eccencrypt import get_encrypted_key

Recording = True

filepath = None

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        global Recording,OUTPUT_FILE_NAME,filepath
        cap = cv2.VideoCapture(0)
        # Get the Default resolutions
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        
        # Define the codec and filename.
        filename = str(calendar.timegm(time.gmtime()))+".avi"
        filepath = OUTPUT_FILE_NAME+filename
        out = cv2.VideoWriter(filepath,cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

        while True:
            if not Recording:
                cap.release()
                out.release()
                del cap
                del out
                h_filename = filename
                h_filepath = filepath
                ecc_encryption = get_encrypted_key()
                h_pubkey = ecc_encryption[0]
                h_key = ecc_encryption[1]
                print("KEY USED: ",h_key)
                h_file = hmacsha_file(filepath,h_key)
                block = Blockchain() #Blockchain implementation
                block.add(h_filename,h_filepath,h_pubkey,h_file)
                break
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

counter = 0
class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2,self).__init__()
        uic.loadUi('capturewindow.ui', self)
        self.resize(900,600)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label.resize(640, 480)
        self.stopbutton = self.findChild(QtWidgets.QPushButton,'pbStopCapture')
        self.stopbutton.move(420,440)
        self.stopbutton.clicked.connect(self.closeFunc)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()
        self.close()

    def closeFunc(self):
        global Recording
        Recording = False
        self.close()
        


    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))



if __name__ == '__main__':
    Recording = True
    app = QtWidgets.QApplication(sys.argv)
    window = Ui2()
    app.exec_()