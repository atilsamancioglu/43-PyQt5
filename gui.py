from PyQt5 import QtWidgets, QtGui #özellikleri oluşturacak modüldür
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys#komut satırından çalıştıracağımızdan vereceğimiz argümanlar için önemli


def window():
	app = QApplication(sys.argv)#uygulama objesi gerekli olduğundan.
	win = QtWidgets.QWidget() #pencere oluşturmamızı sağlar
	win.setWindowTitle("Hello!")# pencerenin başlığı
	win.setGeometry(700, 350, 450, 400)
	labels(win)
	#button(win)
	win.show()#pencereyi göstermek için.
	sys.exit(app.exec_())# sürekli çalışır olması için 
def button(win):
	btn1 = QtWidgets.QPushButton(win)#buton oluşturma
	btn1.setText("Click") # buton text ekleme
	btn1.clicked.connect(clicked) # buton ve fonksiyon bağlantısı
def labels(win):
	label1 = QtWidgets.QLabel(win)#Yazı etiketi oluşturup ardınan pencereye verdik
	label1.setText("How are you?")#etiket içeriği
	label1.move(200,50)#etiketin taşınacak alanı
	label2 = QtWidgets.QLabel(win)
	label2.setPixmap(QtGui.QPixmap("QT5.png"))
	label2.move(100,60)
def clicked(label):
	print("OK")
window()
