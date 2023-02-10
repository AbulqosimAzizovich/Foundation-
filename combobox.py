from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QCheckBox, QLabel, QComboBox, QMessageBox
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.start()

    def start(self):
        self.savol = QLabel("Qaysi dasturlash tillarini bilasiz?", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)
        self.savol.adjustSize()

        self.combo = QComboBox(self)
        self.combo.addItems(
            ["", "Flutter", "Fronted", "Java Spring", "Golang", "Node Js + VueJs", ".Net"])
        self.combo.setFont(QFont("Times", 20))
        self.combo.move(100, 100)

        ok = QPushButton("ok", self)
        ok.setFont(QFont("Times", 20))
        ok.move(50, 300)
        ok.clicked.connect(self.Ok)

    def Ok(self):
        win = QMessageBox(self)
        win.setFont(QFont("Times", 20))
        if self.combo.currentText() == "":
            win.setText("Siz yo'nalish tanlamadingiz")
            win.show()
        else:
            win.setText("Siz" + self.combo.currentText() +
                        "Yo'nalishini tanladingiz")
            win.show()


win = Window()
win.show()
sys.exit(app.exec_())
