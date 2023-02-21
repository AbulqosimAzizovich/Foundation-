from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import mysql.connector
import sys

app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Universitet"
        )
        self.win1 = Window1()
        self.SIGn = SIGN_IN()
        self.cur = self.mydb.cursor()
        self.setWindowTitle("Kirish")
        self.setGeometry(100, 100, 500, 500)
        self.start()
        self.create_table()
        self.insert_table()
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 20))
        obj.move(x, y)

    def start(self):
        self.log_in = QPushButton("Log In", self)
        self.font(self.log_in, 75, 100)

        self.sign_up = QPushButton("Sign Up", self)
        self.font(self.sign_up, 75, 150)

        self.log_in.clicked.connect(self.Log)
        self.sign_up.clicked.connect(self.Sign)

    def Log(self):
        window.hide()
        self.win1.show()

    def Sign(self):
        window.hide()
        self.SIGn.show()

    def create_table(self):
        self.cur.execute(
            'create table if not exists Kirish(Id int, Password varchar(50), Login varchar(50))')
        self.mydb.commit()

    def insert_table(self):
        self.cur.execute("insert into Kirish values (1, '12345', 'admin')")


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 500, 600)
        self.win2 = Window2()
        self.start1()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 20))
        obj.move(x, y)

    def start1(self):
        self.l1 = QLabel("Login", self)
        self.font(self.l1, 20, 50)

        self.log_in = QLineEdit(self)
        self.font(self.log_in, 170, 50)

        self.p1 = QLabel("Password", self)
        self.font(self.p1, 20, 100)

        self.password = QLineEdit(self)
        self.font(self.password, 170, 100)

        self.ok = QPushButton("Ok", self)
        self.font(self.ok, 400, 150)

        self.cancel = QPushButton("Cancel", self)
        self.font(self.cancel, 270, 150)

        self.cancel.clicked.connect(self.Cancel)
        self.ok.clicked.connect(self.Ok)

    def Cancel(self):
        window.win1.hide()
        window.show()

    def Ok(self):
        text1 = self.log_in.text()  # kiritilgan login
        text2 = self.password.text()  # kiritilgan kod
        window.cur.execute("select password from kirish")
        self.parol = window.cur.fetchall()
        window.cur.execute("select login from kirish")
        self.login = window.cur.fetchall()

        self.parol = str(self.parol)
        self.paw = str()  # Bazadagi parol
        self.login = str(self.login)
        self.lgn = str()  # Bazadagi login
        for i in self.parol:
            if i.isdigit() or i.isalpha():
                self.paw += i

        for i in self.login:
            if i.isalpha() or i.isdigit():
                self.lgn += i

        if text1 == self.lgn and text2 == self.paw:
            window.win1.hide()
            self.win2.show()

        elif text1 != self.lgn and text2 == self.paw:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Login Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()

        elif text1 == self.lgn and text2 != self.paw:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Password Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()

        elif text1 != self.lgn and text2 != self.paw:
            window.win1.hide()
            window.SIGn.show()


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Site")
        self.setGeometry(100, 100, 500, 600)

        self.start2()

    def start2(self):
        a = QLabel("Tizimga kirildi!", self)
        a.setFont(QFont("Arial Black", 25))
        a.adjustSize()


class SIGN_IN(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 500, 600)
        self.check = Check()
        self.starrrt()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 20))
        obj.move(x, y)

    def starrrt(self):
        self.la = QLabel("Login", self)
        self.font(self.la, 20, 50)

        self.pa = QLabel("Password", self)
        self.font(self.pa, 20, 100)

        self.sp = QLabel("Sponsor", self)
        self.font(self.sp, 20, 150)

        self.new_log = QLineEdit(self)
        self.font(self.new_log, 170, 50)

        self.new_pas = QLineEdit(self)
        self.font(self.new_pas, 170, 100)

        self.sponsor = QLineEdit(self)
        self.font(self.sponsor, 170, 150)

        ok1 = QPushButton("Ok", self)
        self.font(ok1, 400, 200)

        cancel1 = QPushButton("Cancel", self)
        self.font(cancel1, 270, 200)

        cancel1.clicked.connect(self.Orqaga)
        ok1.clicked.connect(self.Tamam)

    def Orqaga(self):
        window.SIGn.hide()
        window.win1.show()

    def Tamam(self):
        text = self.sponsor.text()
        window.cur.execute("select login from kirish")
        self.login = window.cur.fetchall()
        self.login = str(self.login)
        self.log = str()
        for i in self.login:
            if i.isalpha() or i.isdigit():
                self.log += i

        if text == self.log:
            window.SIGn.hide()
            self.check.show()


class Check(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 250, 600, 300)

        self.bosh()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 18))
        obj.move(x, y)

    def bosh(self):
        self.pw = QLabel("Password", self)
        self.font(self.pw, 30, 50)

        self.line_pas = QLineEdit(self)
        self.font(self.line_pas, 170, 50)

        self.ok = QPushButton("Ok", self)
        self.font(self.ok, 400, 100)

        self.cancel = QPushButton("Cancel", self)
        self.font(self.cancel, 270, 100)

        self.cancel.clicked.connect(self.Off)
        self.ok.clicked.connect(self.On)

    def Off(self):
        window.SIGn.check.hide()
        window.SIGn.show()

    def On(self):
        text = self.line_pas.text()
        pas = window.SIGn.new_pas.text()
        lgo = window.SIGn.new_log.text()
        print(pas)
        window.cur.execute("select password from kirish")
        self.parol = window.cur.fetchall()  # Bazadagi parol
        self.parol = str(self.parol)
        self.paw = str()
        for i in self.parol:
            if i.isdigit() or i.isalpha():
                self.paw += i

        if text == self.paw:
            window.cur.execute(
                "update Kirish set Password=%s, Login = %s where id = %s", (pas, lgo, 1))
            miniwindow = QMessageBox(self)
            miniwindow.setText("Muvaffaqiyatli o'zgartirildi")
            miniwindow.setText("✅✅✅✅")

            miniwindow.show()

        else:
            miniwindow = QMessageBox(self)
            miniwindow.setText("Password Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()


window = Window()
window.show()
app.exec_()
