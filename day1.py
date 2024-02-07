# modul pada pyqt ada 3 yaitu QtGui, QtCore, QtWidgets
# CARA PERTAMA
from Pyqt5 import QtGui, QtCore, QtWidgets  # ini menampilkan ketiganya secaca bersamaan dan mudah

app = QtWidgets.QApplication([])
window = QtWidgets.QPushButton("Ini Button")
window.show()

app.exec()
# bisa juga menggunakan
# app.exec_()



# CARA PERTAMA
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# jika menggunakan kode diatas maka tidak perlu memanggil variabel Qt lagi
app = QApplication([])
window = QPushButton("Ini Button")
window.show()

app.exec()



# CARA KETIGA
# menguban variabel sesuka kita
from PyQt5 Import QtWidgets as qtw

app = qtw.QApplication([])
window = qtw.QPushButton("Ini Button")
window.show()

app.exec()



# untuk lebih menghemat memori maka jangan memanggil seluruh modul bisa memakai CARA KETIGA atau seperti ini
from PyQt5.QtWidgets import QApplication, QPushButton
# ini akan lebih ringan/ clean code

app = QApplication([])
window = QPushButton("Ini Button")
window.show()

app.exec()