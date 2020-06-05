from PyQt5 import QtWidgets, QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
	app = QApplication(sys.argv)	
	clear = QtWidgets.QPushButton("Clear")
	update= QtWidgets.QPushButton("Update")
	hBox = QtWidgets.QHBoxLayout()
	hBox.addWidget(clear)
	hBox.addWidget(update)
	hBox.addStretch()
	vBox = QtWidgets.QVBoxLayout()
	vBox.addStretch()
	vBox.addLayout(hBox)
	#vBox.addWidget(clear)
	#vBox.addWidget(update)
	#hBox.addWidget(clear)
	#hBox.addWidget(update)
	win = QtWidgets.QWidget()	
	win.setWindowTitle("Horizontal Layout")
	win.setLayout(vBox)
	win.setGeometry(700, 350, 450, 200)
	win.show()
	sys.exit(app.exec_())
window()
