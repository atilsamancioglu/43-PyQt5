from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

class MyWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(700, 350, 300, 200)
		self.setWindowTitle("Find number")
		self.number = random.randrange(100)
		self.initUI()
	def initUI(self):
		# Text area
		self.label = QtWidgets.QLabel()
		self.label.setText("Go")
		# input Label
		self.line = QtWidgets.QLineEdit()
		self.line.setText("Enter your guess")
		# Buton Reset
		self.b1 = QtWidgets.QPushButton()
		self.b1.setText("Clear")
		# Buton Send
		self.b2 = QtWidgets.QPushButton()
		self.b2.setText("Send")
		# Butona tıklama
		self.b1.clicked.connect(self.clicked)
		self.b2.clicked.connect(self.clicked)
		# Yerleştirme
		self.possition(self.b1,self.b2,self.line,self.label)
	def possition(self,clear,guess,line,label):
		# Yerleştirme Fonksiyonu
		hBox = QtWidgets.QHBoxLayout()
		vBox = QtWidgets.QVBoxLayout()
		vBox.addWidget(line)
		vBox.addStretch()
		vBox.addWidget(label)
		vBox.addStretch()
		vBox.addWidget(clear)
		vBox.addWidget(guess)
		hBox.addStretch()
		hBox.addLayout(vBox)
		hBox.addStretch()
		self.setLayout(hBox)
	def clicked(self):
		sender = self.sender()
		if sender.text() == "Clear":
			self.label.setText("Go")
			self.line.setText("Enter your guess")
		else:
			if self.line.text() == str(self.number):
				self.label.setText("You Win")
			else:
				self.label.setText("Wrong")



def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()