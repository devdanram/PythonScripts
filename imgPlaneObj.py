"""
#SCRIPT NAME  imagePlaneObject

# CREATOR     Daniel Ramirez
# SOURCE      https://www.danielramirez.work
# DESCRIPTION
A dynamic User Interface (UI) to create and select the ImagePlane to edit some attributes like Transparency, move in X and move in Y in Autodesk MAYA.
# USAGE
# LINKS
None
# FEATURES
- User can create an imageplane with the image selected from user
- After creating the imageplane the user can edit the selected imageplane
- Using 5 buttons with prestablished position of the image plane in every corner and full size
- move the image plane in x and y
- change transparency of the image plane
# VERSIONS 2020-08-29 / 0.1.0: first version
# TODO bugs
- There is missing some try/except in the code

---------------------------------------
Add this script to a shelf and add this 

import imgPlaneObj
imgPlaneObj.doimgPlaneObj()

"""



from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
from PySide2.QtCore import Qt

import maya.OpenMayaUI as omui

def doimgPlaneObj():

	camaras = []
	camaraLista = cmds.ls(type="camera")
	indiceCam = 0
	for objeto in camaraLista:
		if indiceCam == 0:
			camaras.append("P L E A S E S E L E C T C A M E R A --------------->")
		indiceCam += 1
		objetoSin = objeto.replace('Shape', '')
		camaras.append(objetoSin)

	def maya_main_window():
		main_window_ptr = omui.MQtUtil.mainWindow()
		return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
	#-------------------------------------------------------------------------------------------------------
	class TestDialog(QtWidgets.QDialog):
		def __init__(self, parent=maya_main_window()):
			super(TestDialog, self).__init__(parent)
			self.setWindowTitle("ImgPlane CREATOR")
			self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
			self.create_widgets()
			self.create_layouts()
			self.create_connections()

		def create_widgets(self):
			self.Instructions2 = QtWidgets.QLabel()
			self.Instructions2.setText("I N S T R U C T I O N S : IMAGEPLANE WORKS WHEN IT'S 1920 * 1080")
			self.Instructions1 = QtWidgets.QLabel()
			self.Instructions1.setText("MAKE SURE TO MAKE THE CAMERA'S FIT RESOLUTION GATE IS - O V E R S C A N - ")

			self.dividerInst = QtWidgets.QSplitter(Qt.Horizontal, self)
			self.dividerInst.setStretchFactor(50,1000)

			self.TextCam = QtWidgets.QLabel()
			self.TextCam.setText("Select Camera to put the ImagePlane")
			self.combobox = QtWidgets.QComboBox()
			self.combobox.addItems(camaras)

			self.file_text = QtWidgets.QLabel()
			self.file_text.setText("Select Path")
			self.file_path = QtWidgets.QLineEdit()
			self.file_Btn = QtWidgets.QPushButton()
			self.file_Btn.setIcon(QtGui.QIcon(":fileOpen.png"))

			self.createImagePlane_btn = QtWidgets.QPushButton("CREATE IMAGE PLANE ON SELECTED CAMERA")
			self.createImagePlane_btn.setStyleSheet("background-color: rgb(171,39,14)")
	#--------------------------------------------

			self.dividerSplit = QtWidgets.QSplitter(Qt.Horizontal, self)
			self.dividerSplit.setStretchFactor(50,1000)
	#----------------------------------------------

			self.reloadImagePlane_btn = QtWidgets.QPushButton("RELOAD IMAGEPLANES")
			self.reloadImagePlane_btn.setStyleSheet("background-color: rgb(59,112,173)")

			self.TextCamIP = QtWidgets.QLabel()
			self.TextCamIP.setText("Select ImagePlane to Edit")

			self.comboImgPlane = QtWidgets.QComboBox()

			self.selectImagePlane_btn = QtWidgets.QPushButton("PRESS TO SELECT IMAGEPLANE SELECTED TO START EDITING")
			self.selectImagePlane_btn.setStyleSheet("background-color: rgb(107,132,107)")


			self.checkImgSeq = QtWidgets.QCheckBox("Image Sequence")

			self.frameOffset = QtWidgets.QLineEdit()

			self.transX = QtWidgets.QLabel()
			self.transX.setText("Move in X")
			self.sliderX = QtWidgets.QSlider()
			self.sliderX.setOrientation(Qt.Horizontal)
			self.sliderX.setMinimum(-1300)
			self.sliderX.setMaximum(1300)
			self.sliderX.setValue(0)

			self.transY = QtWidgets.QLabel()
			self.transY.setText("Move in Y")
			self.sliderY = QtWidgets.QSlider()
			self.sliderY.setOrientation(Qt.Horizontal)
			self.sliderY.setMinimum(-700)
			self.sliderY.setMaximum(700)
			self.sliderY.setValue(0)

			self.topleft = QtWidgets.QPushButton("top left")
			self.topleft.setStyleSheet("background-color: rgb(78,152,173)")
			self.topright = QtWidgets.QPushButton("top right")
			self.topright.setStyleSheet("background-color: rgb(78,152,173)")
			self.botleft = QtWidgets.QPushButton("bottom left")
			self.botleft.setStyleSheet("background-color: rgb(78,152,173)")
			self.botright = QtWidgets.QPushButton("bottom right")
			self.botright.setStyleSheet("background-color: rgb(78,152,173)")
			self.fullsize = QtWidgets.QPushButton("Full Size")
			self.fullsize.setStyleSheet("background-color: rgb(78,152,173)")

			self.transp = QtWidgets.QLabel()
			self.transp.setText("Transparency")
			self.sliderT = QtWidgets.QSlider()
			self.sliderT.setOrientation(Qt.Horizontal)
			self.sliderT.setMinimum(0)
			self.sliderT.setMaximum(100)

		def create_layouts(self):
	#------- texto de seleccionar camara

	#------- SELECT CAMERA ----------

			form_layout = QtWidgets.QFormLayout()
			form_layout.addRow(self.Instructions2)
			form_layout.addRow(self.Instructions1)
			form_layout.addRow(self.dividerInst)
			form_layout.addRow(self.TextCam)
			form_layout.addRow("Select Camera", self.combobox)

	#------- FILE PATH -----------
			file_layout = QtWidgets.QHBoxLayout()
			file_layout.addWidget(self.file_text)
			file_layout.addWidget(self.file_path)
			file_layout.addWidget(self.file_Btn)

	#-------- BUTTON IMAGE PLANE CREATOR -----------------
			imgPlaneCreator_layout = QtWidgets.QVBoxLayout()
			imgPlaneCreator_layout.addWidget(self.createImagePlane_btn)

	#----------------------------------------------

			mySplitter = QtWidgets.QVBoxLayout()
			mySplitter.addWidget(self.dividerSplit)
	#-------------------------------------------------------------------
	#---------------- boton para reload de imagelpalens-----------------
			imgplaneReload = QtWidgets.QVBoxLayout()
			imgplaneReload.addWidget(self.reloadImagePlane_btn)

	#-------- IMAGEPLANE SELECTION BUTON -----------------------------
			imgplaneSelection = QtWidgets.QVBoxLayout()
			imgplaneSelection.addWidget(self.selectImagePlane_btn)

	#-------- IMAGEPLANE TEXT SELECTION -----------------------------
			imgplaneText = QtWidgets.QVBoxLayout()
			imgplaneText.addWidget(self.TextCamIP)
			imgplaneText.addWidget(self.comboImgPlane)

	#------- CHECKBOX PARA IMAGE SEQUENCE --------
			attr_layout = QtWidgets.QVBoxLayout()
			attr_layout.addWidget(self.checkImgSeq)

	#-------- FRAME OFFSET -------------
			formattr_layout = QtWidgets.QFormLayout()
			formattr_layout.addRow("Frame Offset", self.frameOffset)

	#-------- SLIDERS ------------------------------------------------

			hbox = QtWidgets.QHBoxLayout()
			hbox.addWidget(self.transX)
			hbox.addWidget(self.sliderX)

			hboy = QtWidgets.QHBoxLayout()
			hboy.addWidget(self.transY)
			hboy.addWidget(self.sliderY)

	#-------- BOTONES ----------------
			button_layout = QtWidgets.QHBoxLayout()
			button_layout.addWidget(self.topleft)
			button_layout.addWidget(self.topright)
			button_layout.addWidget(self.botleft)
			button_layout.addWidget(self.botright)
			button_layout.addWidget(self.fullsize)

	#------- SLIDER TRANSPARENCIA
			hbot = QtWidgets.QHBoxLayout()
			hbot.addWidget(self.transp)
			hbot.addWidget(self.sliderT)

	#------- MAIN LAYOUT ----------
			main_layout = QtWidgets.QVBoxLayout(self)
			main_layout.addLayout(form_layout)
			main_layout.addLayout(file_layout)
			main_layout.addLayout(imgPlaneCreator_layout)

			main_layout.addLayout(mySplitter)

			main_layout.addLayout(imgplaneReload)
			main_layout.addLayout(imgplaneText)

			main_layout.addLayout(imgplaneSelection)
			main_layout.addLayout(attr_layout)
			main_layout.addLayout(formattr_layout)

			main_layout.addLayout(hbox)
			main_layout.addLayout(hboy)
			main_layout.addLayout(button_layout)
			main_layout.addLayout(hbot)

		def create_connections(self):
			self.combobox.activated.connect(self.onactivated_int)
			self.combobox.activated[str].connect(self.onactivated_str)

			self.file_Btn.clicked.connect(self.show_File_Diaog)

			self.createImagePlane_btn.clicked.connect(self.create_imageplane_btndef)

			self.reloadImagePlane_btn.clicked.connect(self.load_imgplane)

			self.comboImgPlane.activated.connect(self.onactivatedImgPla_int)
			self.comboImgPlane.activated[str].connect(self.onactivatedImgPla_str)

			self.selectImagePlane_btn.clicked.connect(self.selectIPbtn)

			self.topleft.clicked.connect(self.topleft_btn)
			self.topright.clicked.connect(self.topright_btn)
			self.botleft.clicked.connect(self.botleft_btn)
			self.botright.clicked.connect(self.botright_btn)
			self.fullsize.clicked.connect(self.fullsize_btn)



			self.checkImgSeq.toggled.connect(self.on_checked_seq)
			self.frameOffset.editingFinished.connect(self.frame_offset_def)

			self.sliderX.valueChanged.connect(self.sliderXConn)
			self.sliderY.valueChanged.connect(self.sliderYConn)
			self.sliderT.valueChanged.connect(self.sliderTrConn)

		@QtCore.Slot(int)
		def onactivated_int(self, indexo):
			#print("combobox int: {0}".format(indexo))
			self.indNumero = indexo

		@QtCore.Slot(str)
		def onactivated_str(self, texto):
			#print("combobox str: {0}".format(texto))
			self.textNombre = texto

		@QtCore.Slot(int)
		def onactivatedImgPla_int(self, indexoIP):
			#print("combobox int: {0}".format(indexo))
			self.indNumeroIP = indexoIP

		@QtCore.Slot(str)
		def onactivatedImgPla_str(self, textoIP):
			#print("combobox str: {0}".format(textoIP))
			self.textNombreIP = textoIP

		def nombreCamara(self):
			self.nombreCamara = self.nombre
			return self.nombreCamara

		def imagePlaneReload(self):
			imgPlane = []
			try:
				pass

			except:
				pass

		def show_File_Diaog(self):
			file_path_text , selected_Filter = QtWidgets.QFileDialog.getOpenFileName(self,"Select File")
			self.variablePath = file_path_text
			if file_path_text:
				self.file_path.setText(file_path_text)
				self.variablePath = file_path_text

		def on_checked_seq(self):
			checado = self.checkImgSeq.isChecked()

			nomObjeto = self.textNombreIP
			extObjeto = ".useFrameExtension"
			imgSeqCheckBox = nomObjeto + extObjeto
			if checado:
				self.palomita = 1
				print("activo")
				cmds.setAttr(imgSeqCheckBox,1)
			else:
				self.palomita = 0
				print("no activo")
				cmds.setAttr(imgSeqCheckBox,0)

		def frame_offset_def(self):
			numOffFrame = self.frameOffset.text()
			frameInt = int(numOffFrame)
			nomFrOff = self.textNombreIP
			extObjetoff = ".frameOffset"
			framOffsetText = nomFrOff + extObjetoff
			cmds.setAttr(framOffsetText,frameInt)

		def create_imageplane_btndef(self):
			objeto = self.textNombre
			myImagePlane = cmds.imagePlane(name=(objeto+"ImagePlane"))
			objImg = myImagePlane[0]
			cmds.select( objImg, visible=True )
			cmds.parentConstraint( objeto, objImg )
			shapeImgPlane3 = myImagePlane[1]
			nombreImagen = ".imageName"
			imageNameAttr = shapeImgPlane3 + nombreImagen

			variableNuevoPath = str(self.variablePath)
			cmds.setAttr(imageNameAttr, variableNuevoPath, type="string")

			moverlejania = ".imageCenterZ"
			imagecenterzstring = shapeImgPlane3 + moverlejania
			cmds.setAttr(imagecenterzstring, -1)

			moveSize = ".width"
			imageSize = shapeImgPlane3 + moveSize
			sizeImg = 1.22
			cmds.setAttr(imageSize, sizeImg)

			moveSizeHeight = ".height"
			imageSize = shapeImgPlane3 + moveSizeHeight
			sizeImgHei = 0.686
			cmds.setAttr(imageSize, sizeImgHei)

	#-------------------------------------------------------------------------------------------------------------------


		def load_imgplane(self):
			self.comboImgPlane.clear()
			imgplanes = []
			imgPlaLista = cmds.ls(type="imagePlane")
			indice = 0
			try:
				if len(imgPlaLista) > 0:
					for objeto in imgPlaLista:
						if indice == 0: 					
							imgplanes.append("P L E A S E S E L E C T I M A G E P L A N E --------------->")
						imgplanes.append(objeto)
						indice += 1
					self.variableIP = imgplanes
					print(self.variableIP)
				else:
					cmds.confirmDialog( title='ERROR', message='YOU HAVE TO CREATE A NEW IMAGEPLANE IN THE TOP PART OF THIS TOOL?', button=['THANK YOU'], defaultButton='Yes', dismissString='No' )
			except:
				pass

			self.comboImgPlane.addItems(self.variableIP)
			self.comboImgPlane.update()
		def selectIPbtn(self):
			SeleccionIP = self.textNombreIP
			cmds.select(SeleccionIP)

			SeleccionNa = self.textNombreIP

	#-----------------------------------------------------------
			transparenciaName = ".alphaGain"
			transpSeleccion = SeleccionNa + transparenciaName
			getValorTransparencia = cmds.getAttr(transpSeleccion)
			valorTranspFlo = float(getValorTransparencia)
			floatValorTransp = valorTranspFlo * 100
			valTranspInt = int(floatValorTransp)
			valorTranspFinal = 100 - valTranspInt
			print(valorTranspFinal)
			#self.sliderT.setValue(valorTranspFinal)
			self.sliderT.setValue(valorTranspFinal)

			self.valorTranSelectIpbtn = valorTranspFinal
	#--------------------------------------------------------------
	#--------------------------------------------------------------
			nomObjeto = self.textNombreIP
			extObjeto = ".useFrameExtension"
			imgSeqCheckBox = SeleccionNa + extObjeto
			print(imgSeqCheckBox)
			print("este es elvalor del nombre para cambiarlo")
			checado = cmds.getAttr(imgSeqCheckBox)
			print(checado)
			print("este es el valor de checaddo arriba esta obteniendo el valor de use image sequence")
			self.checkImgSeq.setChecked(checado)
			print("este es el nombre del checkimgseq")
			print(self.checkImgSeq)
			#checado = self.checkImgSeq.isChecked()



	#--------------------------------------------------------------
	#--------------------------------------------------------------

			moveXName = ".imageCenterX"
			moveXNameComp = SeleccionNa + moveXName
			sizeX = cmds.getAttr(moveXNameComp)
			valorCienX = float(sizeX) * 1000
			self.sliderX.setValue(valorCienX)
			#cmds.setAttr(moveXNameComp, valorCienX)

			moveYName = ".imageCenterY"
			moveYNameComp = SeleccionNa + moveYName
			sizeY = cmds.getAttr(moveYNameComp)
			valorCienY = float(sizeY) * 1000
			self.sliderY.setValue(valorCienY)
			#cmds.setAttr(moveXNameComp, valorCienY)


		#-------BOTONES--------------------------------------------------------
		def topleft_btn(self):
			SeleccionNa = self.textNombreIP
			moverX = ".imageCenterX"
			imagecenterxstring = SeleccionNa + moverX
			cmds.setAttr(imagecenterxstring, -0.400)
			moverY = ".imageCenterY"
			imagecenterxstring = SeleccionNa + moverY
			cmds.setAttr(imagecenterxstring, 0.22)

			moveSize = ".width"
			imageSize = SeleccionNa + moveSize
			sizeImg = 0.4
			cmds.setAttr(imageSize, sizeImg)

			moveSizeHeight = ".height"
			imageSize = SeleccionNa + moveSizeHeight
			sizeImgHei = 0.225
			cmds.setAttr(imageSize, sizeImgHei)

		def topright_btn(self):
			SeleccionNa = self.textNombreIP
			moverX = ".imageCenterX"
			imagecenterxstring = SeleccionNa + moverX
			cmds.setAttr(imagecenterxstring, 0.400)
			moverY = ".imageCenterY"
			imagecenterxstring = SeleccionNa + moverY
			cmds.setAttr(imagecenterxstring, 0.22)
			moveSize = ".width"
			imageSize = SeleccionNa + moveSize
			sizeImg = 0.4
			cmds.setAttr(imageSize, sizeImg)

			moveSizeHeight = ".height"
			imageSize = SeleccionNa + moveSizeHeight
			sizeImgHei = 0.225
			cmds.setAttr(imageSize, sizeImgHei)

		def botleft_btn(self):
			SeleccionNa = self.textNombreIP
			moverX = ".imageCenterX"
			imagecenterxstring = SeleccionNa + moverX
			cmds.setAttr(imagecenterxstring, -0.400)
			moverY = ".imageCenterY"
			imagecenterxstring = SeleccionNa + moverY
			cmds.setAttr(imagecenterxstring, -0.22)
			moveSize = ".width"
			imageSize = SeleccionNa + moveSize
			sizeImg = 0.4
			cmds.setAttr(imageSize, sizeImg)
			moveSizeHeight = ".height" 
			imageSize = SeleccionNa + moveSizeHeight
			sizeImgHei = 0.225 
			cmds.setAttr(imageSize, sizeImgHei) 
		def botright_btn(self):
				SeleccionNa = self.textNombreIP 
				moverX = ".imageCenterX" 
				imagecenterxstring = SeleccionNa + moverX 
				cmds.setAttr(imagecenterxstring, 0.400) 
				moverY = ".imageCenterY" 
				imagecenterxstring = SeleccionNa + moverY 
				cmds.setAttr(imagecenterxstring, -0.22) 
				moveSize = ".width" 
				imageSize = SeleccionNa + moveSize 
				sizeImg = 0.4 
				cmds.setAttr(imageSize, sizeImg) 
				moveSizeHeight = ".height" 
				imageSize = SeleccionNa + moveSizeHeight 
				sizeImgHei = 0.225 
				cmds.setAttr(imageSize, sizeImgHei) 
			def fullsize_btn(self): 
				SeleccionNa = self.textNombreIP 
				moverX = ".imageCenterX" 
				imagecenterxstring = SeleccionNa + moverX 
				cmds.setAttr(imagecenterxstring, 0) 
				moverY = ".imageCenterY" 
				imagecenterxstring = SeleccionNa + moverY 
				cmds.setAttr(imagecenterxstring,0) 
				moveSize = ".width" 
				imageSize = SeleccionNa + moveSize 
				sizeImg = 1.22 
				cmds.setAttr(imageSize, sizeImg) 
				moveSizeHeight = ".height" 
				imageSize = SeleccionNa + moveSizeHeight 
				sizeImgHei = 0.686 
				cmds.setAttr(imageSize, sizeImgHei) 
			def sliderXConn(self): 
				SeleccionNa = self.textNombreIP 
				moveXName = ".imageCenterX" 
				moveXSeleccion = SeleccionNa + moveXName 
				sizeX = self.sliderX.value() 
				valorCienX = int(sizeX) * 0.001 
				cmds.setAttr(moveXSeleccion, valorCienX) 
			def sliderYConn(self): 
				SeleccionNa = self.textNombreIP 
				moveYName = ".imageCenterY" 
				moveYSeleccion = SeleccionNa + moveYName 
				sizeY = self.sliderY.value() 
				valorCienY = float(sizeY) * 0.001 
				cmds.setAttr(moveYSeleccion, valorCienY) 
			def sliderTrConn(self): 
				SeleccionNa = self.textNombreIP 
				transparenciaName = ".alphaGain" 
				transpSeleccion = SeleccionNa + transparenciaName 
				size = self.sliderT.value() 
				print("imprime elvalor size de sliderTrConn") 
				print(size) 
				val = int(size) 
				valorFinal = val * 0.01 
				#val = float(size) * 100 
				#valorCien = 100 - int(val) 
				#valorFinal = int(valorCien) / 100.00 
				cmds.setAttr(transpSeleccion, valorFinal) 
				print("imporime el valor final con set attr") 
				print(valorFinal) 
		if __name__ == "__main__": 
			try: 
				TestDialog.close() 
				TestDialog.deleteLater() 
			except: 
				pass 
		d = TestDialog() 
		d.show()
