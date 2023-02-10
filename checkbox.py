from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QCheckBox, QLabel
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

        self.v1 = QCheckBox("C dasturlash tili", self)
        self.v1.setFont(QFont("times", 20))
        self.v1.move(100, 100)

        self.v2 = QCheckBox("Python dasturlash tili", self)
        self.v2.setFont(QFont("times", 20))
        self.v2.move(100, 150)

        self.v3 = QCheckBox("C dasturlash tili", self)
        self.v3.setFont(QFont("times", 20))
        self.v3.move(100, 200)

        self.v4 = QCheckBox("C dasturlash tili", self)
        self.v4.setFont(QFont("times", 20))
        self.v4.move(100, 250)

        ok = QPushButton("ok", self)
        ok.setFont(QFont("Times", 20))
        ok.move(50, 300)
        ok.clicked.connect(self.Ok)

    def Ok(self):
        self.savol.setText("Men quyidagi tillarini bilaman:\n")
        if self.v1.isChecked():
            self.savol.setText(self.savol.text() + "\t" +
                               self.v1.text() + "\n")

        if self.v2.isChecked():
            self.savol.setText(self.savol.text() + "\t" +
                               self.v2.text() + "\n")

        if self.v3.isChecked():
            self.savol.setText(self.savol.text() + "\t" +
                               self.v3.text() + "\n")

        if self.v4.isChecked():
            self.savol.setText(self.savol.text() + "\t" +
                               self.v4.text() + "\n")

        if not (self.v1.isChecked()) and not (self.v2.isChecked()) and not (self.v3.isChecked()) and not (self.v4.isChecked()):
            self.savol.setText("Mem hech narsa bilmayman")

        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()

        self.savol.adjustSize()


win = Window()
win.show()
sys.exit(app.exec_())
