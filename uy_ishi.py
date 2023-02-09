"1-masala"

# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
# from PyQt5.QtWidgets import QLabel, QRadioButton, QPushButton
# from PyQt5.QtGui import QFont
# import sys

# app = QApplication(sys.argv)


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TEST")
#         self.setGeometry(100, 100, 500, 500)
#         self.window2 = Window2()
#         self.start()

#     def start(self):
#         self.ball = 0

#         self.s1 = QLabel("1.  1+1=?", self)
#         self.s1.setFont(QFont("Times", 18))
#         self.s1.move(20, 20)

#         self.r1 = QRadioButton("A) 3", self)
#         self.r1.setFont(QFont("Times", 18))
#         self.r1.move(20, 60)

#         self.r2 = QRadioButton("B) 2", self)
#         self.r2.setFont(QFont("Times", 18))
#         self.r2.move(100, 60)

#         self.r3 = QRadioButton("C) 4", self)
#         self.r3.setFont(QFont("Times", 18))
#         self.r3.move(180, 60)

#         self.r4 = QRadioButton("D) 1", self)
#         self.r4.setFont(QFont("Times", 18))
#         self.r4.move(260, 60)

#         p1 = QPushButton("OK", self)
#         p1.setFont(QFont("Times", 18))
#         p1.move(80, 150)
#         p1.clicked.connect(self.run1)

#     def run1(self):
#         if self.r1.isChecked():
#             self.ball += 0

#         if self.r2.isChecked():
#             self.ball += 1

#         if self.r3.isChecked():
#             self.ball += 0

#         if self.r4.isChecked():
#             self.ball += 0

#         self.window2.show()
#         self.hide()


# class Window2(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TEST")
#         self.setGeometry(100, 100, 500, 500)
#         self.window3 = Window3()
#         self.start2()

#     def start2(self):
#         self.s2 = QLabel("2.  2+2=?", self)
#         self.s2.setFont(QFont("Times", 18))
#         self.s2.move(20, 20)

#         self.r5 = QRadioButton("A) 3", self)
#         self.r5.setFont(QFont("Times", 18))
#         self.r5.move(20, 60)

#         self.r6 = QRadioButton("B) 2", self)
#         self.r6.setFont(QFont("Times", 18))
#         self.r6.move(100, 60)

#         self.r7 = QRadioButton("C) 4", self)
#         self.r7.setFont(QFont("Times", 18))
#         self.r7.move(180, 60)

#         self.r8 = QRadioButton("D) 1", self)
#         self.r8.setFont(QFont("Times", 18))
#         self.r8.move(260, 60)

#         p2 = QPushButton("OK", self)
#         p2.setFont(QFont("Times", 18))
#         p2.move(80, 150)
#         p2.clicked.connect(self.run2)

#     def run2(self):

#         if self.r5.isChecked():
#             window.ball += 0

#         if self.r6.isChecked():
#             window.ball += 0

#         if self.r7.isChecked():
#             window.ball += 1

#         if self.r8.isChecked():
#             window.ball += 0

#         self.window3.show()
#         self.hide()


# class Window3(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TEST")
#         self.setGeometry(100, 100, 500, 500)
#         self.window4 = Window4()
#         self.start3()

#     def start3(self):
#         self.s9 = QLabel("3.  3+3=?", self)
#         self.s9.setFont(QFont("Times", 20))
#         self.s9.move(20, 20)

#         self.r10 = QRadioButton("A) 9", self)
#         self.r10.setFont(QFont("Times", 18))
#         self.r10.move(20, 60)

#         self.r11 = QRadioButton("B) 6", self)
#         self.r11.setFont(QFont("Times", 18))
#         self.r11.move(100, 60)

#         self.r12 = QRadioButton("C) 4", self)
#         self.r12.setFont(QFont("Times", 18))
#         self.r12.move(180, 60)

#         self.r13 = QRadioButton("D) 3", self)
#         self.r13.setFont(QFont("Times", 18))
#         self.r13.move(260, 60)

#         p3 = QPushButton("OK", self)
#         p3.setFont(QFont("Times", 18))
#         p3.move(80, 150)
#         p3.clicked.connect(self.run3)

#     def run3(self):

#         if self.r10.isChecked():
#             window.ball += 0

#         if self.r11.isChecked():
#             window.ball += 1

#         if self.r12.isChecked():
#             window.ball += 0

#         if self.r13.isChecked():
#             window.ball += 0

#         self.window4.show()
#         self.hide()


# class Window4(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TEST")
#         self.setGeometry(100, 100, 500, 500)
#         self.window5 = Window5()
#         self.start4()

#     def start4(self):
#         self.s4 = QLabel("4.  1+0=?", self)
#         self.s4.setFont(QFont("Times", 20))
#         self.s4.move(20, 20)

#         self.r14 = QRadioButton("A) 10", self)
#         self.r14.setFont(QFont("Times", 18))
#         self.r14.move(20, 60)

#         self.r15 = QRadioButton("B) 2", self)
#         self.r15.setFont(QFont("Times", 18))
#         self.r15.move(100, 60)

#         self.r16 = QRadioButton("C) 01", self)
#         self.r16.setFont(QFont("Times", 18))
#         self.r16.move(180, 60)

#         self.r17 = QRadioButton("D) 1", self)
#         self.r17.setFont(QFont("Times", 18))
#         self.r17.move(260, 60)

#         p4 = QPushButton("OK", self)
#         p4.setFont(QFont("Times", 18))
#         p4.move(80, 150)
#         p4.clicked.connect(self.run4)

#     def run4(self):

#         if self.r14.isChecked():
#             window.ball += 0

#         if self.r15.isChecked():
#             window.ball += 0

#         if self.r16.isChecked():
#             window.ball += 0

#         if self.r17.isChecked():
#             window.ball += 1

#         self.window5.show()
#         self.hide()


# class Window5(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("TEST")
#         self.setGeometry(100, 100, 500, 500)

#         self.start5()

#     def start5(self):
#         self.s5 = QLabel("5.  1-1=?", self)
#         self.s5.setFont(QFont("Times", 20))
#         self.s5.move(20, 20)

#         self.r18 = QRadioButton("A) 0", self)
#         self.r18.setFont(QFont("Times", 18))
#         self.r18.move(20, 60)

#         self.r19 = QRadioButton("B)-2", self)
#         self.r19.setFont(QFont("Times", 18))
#         self.r19.move(100, 60)

#         self.r20 = QRadioButton("C) 1", self)
#         self.r20.setFont(QFont("Times", 18))
#         self.r20.move(180, 60)

#         self.r21 = QRadioButton("D)-1", self)
#         self.r21.setFont(QFont("Times", 18))
#         self.r21.move(260, 60)

#         p5 = QPushButton("OK", self)
#         p5.setFont(QFont("Times", 18))
#         p5.move(80, 150)
#         p5.clicked.connect(self.run5)

#     def run5(self):

#         if self.r18.isChecked():
#             window.ball += 1
#             miniwindow = QMessageBox(self)

#             text = window.ball
#             text = str(text)
#             miniwindow.setText(text)
#             miniwindow.show()

#         if self.r19.isChecked():
#             window.ball += 0
#             miniwindow = QMessageBox(self)

#             text = window.ball
#             text = str(text)
#             miniwindow.setText(text)
#             miniwindow.show()

#         if self.r20.isChecked():
#             window.ball += 0
#             miniwindow = QMessageBox(self)

#             text = window.ball
#             text = str(text)
#             miniwindow.setText(text)
#             miniwindow.show()

#         if self.r21.isChecked():
#             window.ball += 0
#             miniwindow = QMessageBox(self)

#             text = window.ball
#             text = str(text)
#             a = "Umumiy" + text + "ball"
#             miniwindow.setText(a)
#             miniwindow.show()


# window = Window()
# window.show()
# sys.exit(app.exec_())


"2-masala"


# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


# app = QApplication(sys.argv)


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 1800, 800)

#         self.start()

#     def font(self, obj, x, y):
#         self.setFont(QFont("Times", 15))
#         obj.move(x, y)

#     def start(self):

#         self.count = 0
#         self.label1 = QLabel("Ro'yxat", self)
#         self.font(self.label1, 50, 400)

#         self.label2 = QLabel("Narx", self)
#         self.font(self.label2, 300, 400)
#         self.label2.adjustSize()

#         self.count = 0
#         self.umum = QLabel("Jami so'mma", self)
#         self.font(self.umum, 550, 400)
#         self.umum.adjustSize()

#         self.work = QLabel("1-taomlar ro'yxati:", self)
#         self.font(self.work, 0, 50)
#         self.work.adjustSize()

#         self.t1 = QCheckBox("Mastava", self)
#         self.font(self.t1, 100, 100)
#         self.t1.adjustSize()

#         self.t2 = QCheckBox("Sho'rva", self)
#         self.font(self.t2, 100, 150)
#         self.t2.adjustSize()

#         self.t3 = QCheckBox("Moshxo'rda", self)
#         self.font(self.t3, 100, 200)
#         self.t3.adjustSize()

#         self.t4 = QCheckBox("Chuchvara", self)
#         self.font(self.t4, 100, 250)
#         self.t4.adjustSize()

#         self.t5 = QCheckBox("Lag'mon", self)
#         self.font(self.t5, 100, 300)
#         self.t5.adjustSize()

#         self.work2 = QLabel("2-taomlar ro'yxati: ", self)
#         self.font(self.work2, 400, 50)
#         self.work2.adjustSize()

#         self.d1 = QCheckBox("Osh", self)
#         self.font(self.d1, 500, 100)
#         self.d1.adjustSize()

#         self.d2 = QCheckBox("Kabob", self)
#         self.font(self.d2, 500, 150)
#         self.d2.adjustSize()

#         self.d3 = QCheckBox("Dimlama", self)
#         self.font(self.d3, 500, 200)
#         self.d3.adjustSize()

#         self.d4 = QCheckBox("5 barmoq", self)
#         self.font(self.d4, 500, 250)
#         self.d4.adjustSize()

#         self.d5 = QCheckBox("Jigar kabob", self)
#         self.font(self.d5, 500, 300)
#         self.d5.adjustSize()

#         self.work = QLabel("Ichimliklar ro'yxati:", self)
#         self.font(self.work, 700, 50)
#         self.work.adjustSize()

#         self.a1 = QCheckBox("Pepsi", self)
#         self.font(self.a1, 800, 100)
#         self.a1.adjustSize()

#         self.a2 = QCheckBox("Fanta", self)
#         self.font(self.a2, 800, 150)
#         self.a2.adjustSize()

#         self.a3 = QCheckBox("Ko'k choy", self)
#         self.font(self.a3, 800, 200)
#         self.a3.adjustSize()

#         self.a4 = QCheckBox("Qora choy", self)
#         self.font(self.a4, 800, 250)
#         self.a4.adjustSize()

#         self.a5 = QCheckBox("Limon choy", self)
#         self.font(self.a5, 800, 300)
#         self.a5.adjustSize()

#         self.ok = QPushButton("Ok", self)
#         self.font(self.ok, 50, 350)

#         self.ok.clicked.connect(self.Ok)

#     def Ok(self):

#         self.label1.setText("Taomlar:\n")
#         self.label2.setText("Narx\n")

#         if self.t1.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.t1.text() + '\n')
#             self.count += 20000
#             k = "20000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.t2.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.t2.text() + '\n')
#             self.count += 15000
#             k = "15000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.t3.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.t3.text() + '\n')
#             self.count += 16000
#             k = "16000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.t4.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.t4.text() + '\n')
#             self.count += 21000
#             k = "21000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.t5.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.t5.text() + '\n')
#             self.count += 25000
#             k = "25000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.d1.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.d1.text() + '\n')
#             self.count += 30000
#             k = "30000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.d2.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.d2.text() + '\n')
#             self.count += 16000
#             k = "16000"

#             self.label2.setText(self.label2.text() + "\t" + k + '\n')

#         if self.d3.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.d3.text() + '\n')
#             self.count += 15000
#             k = "15000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.d4.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.d4.text() + '\n')
#             self.count += 21000
#             k = "21000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.d5.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.d5.text() + '\n')
#             self.count += 20000
#             k = "20000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.a1.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.a1.text() + '\n')
#             self.count += 12000
#             k = "12000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.a2.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.a2.text() + '\n')
#             self.count += 12000
#             k = "12000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.a3.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.a3.text() + '\n')
#             self.count += 6000
#             k = "6000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.a4.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.a4.text() + '\n')
#             self.count += 6000
#             k = "6000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         if self.a5.isChecked():
#             self.label1.setText(self.label1.text() +
#                                 "\t " + self.a5.text() + '\n')
#             self.count += 5000
#             k = "5000"

#             self.label2.setText(self.label2.text() + "\t" + k + "\n")

#         self.umum.setText("Jami so'mma\n")
#         a = str(self.count)
#         self.umum.setText(self.umum.text() + "\t" + a)
#         self.umum.adjustSize()

#         self.label1.adjustSize()
#         self.label2.adjustSize()


# win = Window()

# win.show()
# sys.exit(app.exec_())


"""3 - masala"""


# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# import sys

# app = QApplication(sys.argv)


# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(100, 100, 1800, 800)

#         self.start()

#     def font(self, obj, x, y):
#         self.setFont(QFont("Times", 15))
#         obj.move(x, y)

#     def start(self):

#         self.work = QLabel("Ma'lumotlar", self)
#         self.font(self.work, 0, 200)

#         self.combo1 = QComboBox(self)
#         self.combo1.addItems(["", "Farg'ona", "Namangan", "Toshkent", "Navoiy",
#                              "Samarqand", "Andijon", "Buxoro", "Qashqadaryo", "Surxondaryo", "Xorazm", "Sirdaryo"])

#         self.font(self.combo1, 80, 200)
#         self.combo1.adjustSize()

#         self.combo2 = QComboBox(self)
#         self.combo2.addItems(
#             ["", "Qo'qon", "Toshkent", "Urganch", "Samarqand"])
#         self.font(self.combo2, 250, 200)
#         self.combo2.adjustSize()

#         self.combo3 = QComboBox(self)
#         self.combo3.addItems(
#             ["", "Erkak", "Ayol"])
#         self.font(self.combo3, 420, 200)
#         self.combo3.adjustSize()

#         self.combo4 = QComboBox(self)
#         self.combo4.addItems(
#             ["", "O'zbek", "Rus", "Tojik", "Qirg'iz"])
#         self.font(self.combo4, 520, 200)
#         self.combo4.adjustSize()

#         self.ok = QPushButton("Ok", self)
#         self.font(self.ok, 80, 250)

#         self.ok.clicked.connect(self.Ok)

#     def Ok(self):

#         self.text1 = self.combo1.currentText()
#         self.text2 = self.combo2.currentText()
#         self.text3 = self.combo3.currentText()
#         self.text4 = self.combo4.currentText()
#         a = [self.text1, self.text2, self.text3, self.text4]
#         a = str(a)

#         self.work.setText(a)
#         self.work.adjustSize()
#         self.combo1.hide()
#         self.combo2.hide()
#         self.combo3.hide()
#         self.combo4.hide()


# win = Window()

# win.show()
# sys.exit(app.exec_())
