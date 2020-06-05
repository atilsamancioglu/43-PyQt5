from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(700, 350, 450, 400)
		self.setWindowTitle("Image Changer")
		self.initUI()
	def initUI(self):
		self.label = QtWidgets.QLabel()
		self.label.setPixmap(QtGui.QPixmap("QT5.png"))
		# Buton Previous
		self.b1 = QtWidgets.QPushButton()
		self.b1.setText("previous <")
		# Buton Next
		self.b2 = QtWidgets.QPushButton()
		self.b2.setText("Next >")
		# Butona tıklama
		self.b1.clicked.connect(self.clickedPrevious)
		self.b2.clicked.connect(self.clickedNext)
		# Yerleştirme
		self.possition(self.b1,self.b2,self.label)
	def possition(self,previous,next,text):
		# Yerleştirme Fonksiyonu
		hBox = QtWidgets.QHBoxLayout()
		vBox = QtWidgets.QVBoxLayout()
		vBox.addWidget(text)
		vBox.addStretch()
		vBox.addWidget(previous)
		vBox.addWidget(next)
		hBox.addStretch()
		hBox.addLayout(vBox)
		hBox.addStretch()
		self.setLayout(hBox)
	def clickedNext(self):
		self.label.setPixmap(QtGui.QPixmap("python.png"))
	def clickedPrevious(self):
		self.label.setPixmap(QtGui.QPixmap("QT5.png"))

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()