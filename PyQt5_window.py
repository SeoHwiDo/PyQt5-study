
import sys
from PyQt5.QtWidgets import *

class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.setGeometry(300,300,300,400)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=EmptyWindow()
    window.show()
    app.exec_()

