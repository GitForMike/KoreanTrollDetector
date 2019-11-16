import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from EvilTest import EvilTest as ET


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KoreanTrollDetector")
        self.setGeometry(300, 300, 300, 400)
        self.le = QLineEdit(self)
        self.le.move(20,20)
        btn1 = QPushButton("악플 판단!", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)
        self.lb = QLabel(self)
        self.lb.move(20,100)
        #le.textChanged.connect(lb.setText)
       
    def btn1_clicked(self):
        #QMessageBox.about(self, "message", "clicked")
        self.lb.setText("Processing...")
        self.lb.setText(ET.test("test"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()