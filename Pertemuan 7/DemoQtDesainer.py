import sys

from GUI_2 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoQtDesainer(QDialog):
	def __init__(self,parent = None):
		QDialog. __init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.hallo.clicked.connect(self.halloClicked)
		
	def halloClicked(self):
		QMessageBox.information(self, 'Demo Qt Designer',
		'Hallo %s, apa kabar?' % self.ui.nameEdit.text())
		
if __name__ == "__main__":
	a = QApplication(sys.argv)
	form = DemoQtDesainer()
	form.show()
	a.exec_()