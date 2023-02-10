from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)
login1 = "admin"
parol1 = "12345"


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kirish")
        self.setGeometry(100, 100, 500, 600)

        self.win1 = Window1()
        self.win2 = Window2()

        self.start()

    def start(self):
        self.login = "admin"
        self.parol = "12345"

        self.log_in = QLabel("Login: ", self)
        self.log_in.setFont(QFont("Times", 15))
        self.log_in.move(0, 50)

        self.password = QLabel("Password: ", self)
        self.password.setFont(QFont("Times", 15))
        self.password.setGeometry(0, 100, 150, 50)

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.move(150, 50)

        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(150, 110)

        self.sign_in = QPushButton("Sign In", self)
        self.sign_in.setFont(QFont("times", 10))
        self.sign_in.setGeometry(100, 200, 70, 50)

        self.sign_up = QPushButton("Sign Up", self)
        self.sign_up.setFont(QFont("times", 10))
        self.sign_up.setGeometry(200, 200, 70, 50)

        self.sign_up.clicked.connect(self.Up)
        self.sign_in.clicked.connect(self.In)

    def Up(self):
        self.win1.show()

    def In(self):
        text = self.line_edit1.text()
        text1 = self.line_edit2.text()

        if text == self.login and text1 == self.parol:
            self.win2.show()
        elif text != self.login and text1 == self.parol:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Login Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()
        elif text == self.login and text1 != self.parol:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Password Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()
        elif text != self.login and text1 != self.parol:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Kiritilgan login va parol xato!!!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registered")
        self.setGeometry(100, 100, 500, 600)
        self.start1()
        self.LOGIN = login1
        self.PAROL = parol1

    def Font(self, obj, x, y):
        obj.setFont(QFont("Times", 15))
        obj.move(x, y)

    def start1(self):
        self.name = QLabel("Name: ", self)
        self.Font(self.name, 0, 50)

        self.age = QLabel("Age: ", self)
        self.Font(self.age, 0, 100)

        self.new = QLabel("Login:", self)
        self.Font(self.new, 0, 150)

        self.newpass = QLabel("Code: ", self)
        self.Font(self.newpass, 0, 200)

        self.registry = QPushButton("Registry", self)
        self.Font(self.registry, 100, 300)

        self.Back = QPushButton("Back", self)
        self.Font(self.Back, 200, 300)

        self.edit1 = QLineEdit(self)
        self.Font(self.edit1, 100, 50)

        self.edit2 = QLineEdit(self)
        self.Font(self.edit2, 100, 100)

        self.edit3 = QLineEdit(self)
        self.Font(self.edit3, 100, 150)

        self.edit4 = QLineEdit(self)
        self.Font(self.edit4, 100, 200)

        self.registry.clicked.connect(self.Registry)

    def Registry(self):

        self.log1 = self.edit3.text()
        self.pas1 = self.edit4.text()
        print(win1.login, win1.parol)
        win1.login = self.log1
        win1.parol = self.pas1


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Site")
        self.setGeometry(100, 100, 500, 600)

        self.start2()

    def start2(self):
        a = QLabel("Najot ta'limga xush kelibsiz!", self)
        a.setFont(QFont("Arial Black", 25))
        a.adjustSize()


win1 = Window()
win1.show()
sys.exit(app.exec_())
