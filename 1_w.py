from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        self.setGeometry(100, 100, 500, 500)
        self.win2 = Window2()
        self.start1()

    def start1(self):
        Sign_in = QPushButton("sign in", self)
        Sign_in.setFont(QFont("Times", 20))
        Sign_in.setGeometry(100, 100, 120, 50)

        Sign_up = QPushButton("sign up", self)
        Sign_up.setFont(QFont("Times", 20))
        Sign_up.setGeometry(300, 100, 120, 50)

        Sign_up.clicked.connect(self.run1)

    def run1(self):
        self.win2.show()


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("second window")
        self.setGeometry(100, 100, 500, 500)
        self.start2()

    def start2(self):
        back = QPushButton("Back", self)
        back.setFont(QFont("Times", 20))
        back.setGeometry(300, 100, 120, 50)
        back.clicked.connect(self.run2)

    def run2(self):
        self.hide()


win1 = Window1()
win1.show()
sys.exit(app.exec_())
