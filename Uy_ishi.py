from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys
import mysql.connector

app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Telegram"
        )

        self.cur = self.mydb.cursor()
        self.setWindowTitle("Window 1")
        self.setGeometry(270, 250, 500, 500)
        self.win1 = Window1()
        self.create_table()
        self.insert_table()
        self.start()
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 18))
        obj.move(x, y)

    def start(self):

        self.log = QLineEdit(self)
        self.font(self.log, 100, 100)
        self.log.setPlaceholderText("Login")
        self.log.adjustSize()

        self.pasw = QLineEdit(self)
        self.font(self.pasw, 100, 150)
        self.pasw.setPlaceholderText("Password")
        self.pasw.adjustSize()

        self.ok = QPushButton("Ok", self)
        self.font(self.ok, 200, 200)
        self.ok.adjustSize()

        self.ok.clicked.connect(self.Ok)

    def create_table(self):
        self.cur.execute(
            "create table if not exists Whatsapp(Login varchar(50), Parol varchar(50), Inchat text, Outchat text)")

    def insert_table(self):
        self.cur.executemany(
            'insert into Whatsapp values(%s, %s, %s, %s)', [("admin", "12345", "", "",),
                                                            ("user", "54321", "", "")])
        self.mydb.commit()

    def Ok(self):
        Log = self.log.text()
        Par = self.pasw.text()

        self.cur.execute("select * from Whatsapp")
        text = self.cur.fetchall()

        if (Log == text[0][0] and Par == text[0][1]) or (Log == text[1][0] and Par == text[1][1]):
            window.hide()
            self.win1.show()

        elif (Log != text[0][0] and Par == text[0][1]) or (Log != text[1][0] and Par == text[1][1]):
            miniwindow = QMessageBox(self)
            miniwindow.setText("Login Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()

        elif (Log == text[0][0] and Par != text[0][1]) or (Log == text[1][0] and Par != text[1][1]):
            miniwindow = QMessageBox(self)
            miniwindow.setText("Password Error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()

        elif Log == "" and Par == "":
            miniwindow = QMessageBox(self)
            miniwindow.setText("Hech narsa kiritilmagan!")
            miniwindow.setIcon(QMessageBox.Information)
            miniwindow.show()

        elif (Log != text[0][0] and Par != text[0][1]) or (Log != text[1][0] and Par != text[1][1]):
            miniwindow = QMessageBox(self)
            miniwindow.setText("Login and password error!")
            miniwindow.setIcon(QMessageBox.Critical)
            miniwindow.show()


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 2")
        self.setGeometry(270, 250, 700, 700)

        self.start2()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 18))
        obj.move(x, y)

    def start2(self):
        self.whom = QLineEdit(self)
        self.font(self.whom, 20, 50)
        self.whom.setPlaceholderText("Whom")
        self.whom.adjustSize()

        self.text_edt1 = QTextEdit(self)
        self.font(self.text_edt1, 0, 100)
        self.text_edt1.setPlaceholderText("Input")
        self.text_edt1.adjustSize()

        self.text_edt2 = QTextEdit(self)
        self.font(self.text_edt2, 300, 100)
        self.text_edt2.setPlaceholderText("Output")
        self.text_edt2.adjustSize()

        self.label = QLabel("salom", self)
        self.font(self.label, 300, 100)
        self.label.hide()

        self.send = QPushButton("Send", self)
        self.font(self.send, 25, 300)
        self.send.adjustSize()

        self.back = QPushButton("Back", self)
        self.back.move(0, 0)
        self.back.adjustSize()

        self.back.clicked.connect(self.Back)
        self.send.clicked.connect(self.Send)

    def Send(self):
        text = self.text_edt1.toPlainText()
        window.cur.execute("select * from Whatsapp")
        self.data = window.cur.fetchall()
        user = self.whom.text()
        if user == self.data[0][0]:

            sender = self.data[1][0]
            str1 = self.data[0][2]
            inchat = str1 + text
            outchat = str1 + text
            print(type(str1))
            window.cur.execute(
                "update Whatsapp set Inchat = %s where Login like %s ", (inchat, sender))
            window.cur.execute(
                "update Whatsapp set Outchat = %s where Login like %s ", (outchat, user))
            window.mydb.commit()

        elif user == self.data[1][0]:
            sender = self.data[0][0]
            str1 = self.data[1][2]
            inchat = text + str1
            outchat = text + str1
            window.cur.execute(
                "update Whatsapp set Inchat = %s where Login like %s ", (inchat, sender))
            window.cur.execute(
                "update Whatsapp set Outchat = %s where Login like %s ", (outchat, user))
            window.mydb.commit()

        window.cur.execute("select * from Whatsapp")
        self.data = window.cur.fetchall()
        print(self.data)

    def Back(self):
        self.whom.clear()
        self.text_edt1.clear()
        self.text_edt2.clear()
        window.win1.hide()
        window.log.clear()
        window.pasw.clear()
        window.show()


window = Window()
window.show()
app.exec_()
