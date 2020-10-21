import style
import sys
import wikipedia
from PyQt5 import QtWidgets, QtCore, QtGui

class Busqueda(QtWidgets.QMainWindow):
	def __init__(self):
		super(Busqueda,self).__init__()
		self.setWindowTitle("WIKIPEDIA GUI")
		self.setFixedSize(1280, 660)
		self.setStyleSheet(style.style)
		# Contenedor
		self.contenedor = QtWidgets.QFrame(self)
		self.contenedor.setObjectName("contenedor")
		self.contenedor.setGeometry(40,30,1200, 591)
		# Etiquetas
		self.labelBusqueda=QtWidgets.QLabel("BUSCAR:",
		self.contenedor)
		self.labelBusqueda.setObjectName("labelBusqueda")
		self.labelBusqueda.setGeometry(210, 35, 85, 41)
		# Editar texto
		self.EditBusqueda = QtWidgets.QLineEdit(
			self.contenedor)
		self.EditBusqueda.setGeometry(300,30, 590, 31)
		self.EditBusqueda.setAlignment(
			QtCore.Qt.AlignCenter)
		#Botones
		self.Btnbuscar = QtWidgets.QPushButton(
			self.contenedor)
		self.Btnbuscar.setGeometry(920, 25, 80, 41)
		self.Btnbuscar.clicked.connect(self.Busqueda)
		self.Btnbuscar.setIcon(QtGui.QIcon(
			"busqueda.png"))
		self.BtnBorrar = QtWidgets.QPushButton(
			"Borrar",
		self.contenedor)
		self.BtnBorrar.setGeometry(550, 85, 131, 41)
		self.BtnBorrar.clicked.connect(self.Borrar)
		self.BtnBorrar.setObjectName("BtnBorrar") 
		# Area de texto
		self.Textinfo = QtWidgets.QTextEdit(self.contenedor)
		self.Textinfo.setGeometry(40, 150, 1115, 400)
		self.Textinfo.setEnabled(False)
		#Mensaje de error
		self.error_dialog = QtWidgets.QMessageBox()
		self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
		self.error_dialog.setWindowTitle("Error")
		
	def Busqueda(self,event):
		try:
			search = self.EditBusqueda.text()
			wikipedia.set_lang("es")
			result=wikipedia.summary(search, 
			sentences = 3) 
			self.Textinfo.setPlainText(result)
			self.Textinfo.setEnabled(True)
			self.Textinfo.setAlignment(
				QtCore.Qt.AlignJustify)
		except:
			self.error_dialog.setInformativeText(
				'¡Oh no! algo salió mal :(')
			self.error_dialog.exec_()
			self.EditBusqueda.setText("")
			self.Textinfo.setPlainText("")
	
	def Borrar(self):
		self.EditBusqueda.setText("")
		self.Textinfo.setPlainText("")
		self.Textinfo.setEnabled(False)
			
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	application = Busqueda()
	application.show()
	sys.exit(app.exec())