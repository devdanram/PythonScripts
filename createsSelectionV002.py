"""
 
#SCRIPT NAME Create Selection
# CREATOR     Daniel Ramirez
# SOURCE
 
# DESCRIPTION
in a UI you can store 5 controls so you can use it faster, or you can put buttons in the viewport selected
# USAGE
select the control , then press the button where you want to store the slection, if you wan tthe HUD button in the viewport ,
press the button like the square and to erase it select the trash can button
# LINKS
None
# FEATURES
 
# VERSIONS 2022 / 0.1.0: first version
# TODO bugs
 
"""
import sys
 
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
 
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds
 
class CustomImageWidget(QtWidgets.QWidget):
 
    def __init__(self, width, height, image_path, parent=None):
        super(CustomImageWidget, self).__init__(parent)
 
def maya_main_window():
    # Obtiene el puntero de la ventana principal de Maya
    # y lo envuelve como un QWidget utilizable desde Python.
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
 
class OpenImportDialog(QtWidgets.QDialog):
 
    def __init__(self):
        super(OpenImportDialog, self).__init__(maya_main_window())
        # antes estaba en __init__(self,parent=maya_main_window)
        # super(OpenImportDialog, self).__init__(parent)
 
        self.setWindowTitle("Create 5 Custom Selections")
        self.setMinimumSize(320, 160)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
 
        self.create_widgets()
        self.create_layout()
        self.create_connections()
 
    def buttonCreation(self):
 
        suma = 1
 
        while suma <= 5:
 
            sel_btn = "sel_btn" + str(suma)
            sel_trash_btn = "trash_btn" + str(suma)
            sel_hud_btn = "hud_btn" + str(suma)
 
            button = QtWidgets.QPushButton("Create new Selection")
            button.setMinimumSize(200, 32)
 
            trash_btn = QtWidgets.QPushButton()
            trash_btn.setIcon(QtGui.QIcon(":trash.png"))
 
            hud_btn = QtWidgets.QPushButton()
            hud_btn.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))
 
            setattr(self, sel_btn, button)
            setattr(self, sel_trash_btn, trash_btn)
            setattr(self, sel_hud_btn, hud_btn)
 
            suma += 1
 
    def create_widgets(self):
        # HERE STARTS THE WIDGET CREATION
        self.buttonCreation()       
        # SIXTH LINE IN THE GUI BUTTON CLOSE
        self.close_btn = QtWidgets.QPushButton("Close")
 
    def layoutCreation(self):
        suma = 1
        while suma <= 5:
            fileVar = "file_path_layout" + str(suma)
 
            file_layout = QtWidgets.QHBoxLayout()
 
            selection_btn = "sel_btn" + str(suma)
            selection_trash_btn = "trash_btn" + str(suma)
            selection_hud_btn = "hud_btn" + str(suma)
 
            getselection_btn = getattr(self, selection_btn)
            getselection_trash_btn = getattr(self, selection_trash_btn)
            getselection_hud_btn = getattr(self, selection_hud_btn)
 
            file_layout.addWidget(getselection_btn)
            file_layout.addWidget(getselection_trash_btn)
            file_layout.addWidget(getselection_hud_btn)
 
            setattr(self, fileVar, file_layout)
 
            suma += 1
 
        form_layout = QtWidgets.QFormLayout()
        suma = 1
        #CREATES THE LAYOUT OF 5 LINES
        while suma <= 5:
            filepathLayout = "file_path_layout" + str(suma)
            getLayout = getattr(self, filepathLayout)
            form_layout.addRow("", getLayout)
            suma += 1
 
        # ADDDS THE LINE OF THE BUTTON CLOSE
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)
 
        # ADDS BOTH LINES TO THE FINAL LAYOUT
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
 
    def create_layout(self):
        self.layoutCreation()
 
    def create_connections(self):
        suma= 1
        while suma <= 5:
            sel_btn_conn = "sel_btn" + str(suma)
            sel_button = getattr(self, sel_btn_conn)
 
            view_btn_conn = "hud_btn" + str(suma)
            view_button = getattr(self, view_btn_conn)
 
            trash_btn_conn = "trash_btn"+str(suma)
            trash_button = getattr(self, trash_btn_conn)
 
            selfselconn = "selection"+str(suma).zfill(2)
            functionsel = getattr(self, selfselconn)
 
            selfviewconn = "viewButton"+str(suma).zfill(2)
            functionview = getattr(self, selfviewconn)
 
            selftrashconn = "select_trash"+str(suma).zfill(2)
            functiontrash = getattr(self, selftrashconn)
 
            sel_button.clicked.connect(functionsel)
            view_button.clicked.connect(functionview)
            trash_button.clicked.connect(functiontrash)
            suma += 1
        self.close_btn.clicked.connect(self.close)
 
    #CONNECTION OF FIRST BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
    def selection01(self):
        self.textinButton = self.sel_btn1.text()  
        self.textInButtonCheck = "Create new Selection"
        if self.textinButton == self.textInButtonCheck :
            self.resultado01 = cmds.ls(sl=True) or []
            if not self.resultado01:
                cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                return
            if len(self.resultado01) == 1:
                self.sel_btn1.setText(self.resultado01[0])
            else:
                self.sel_btn1.setText("Multiple Selection")
        else:
            cmds.select(self.resultado01)
    #CONNECTION OF SECOND BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
    def selection02(self):
        self.textinButton = self.sel_btn2.text()  
        self.textInButtonCheck = "Create new Selection"
        if self.textinButton == self.textInButtonCheck :
            self.resultado02 = cmds.ls(sl=True) or []
            if not self.resultado02:
                cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                return
            if len(self.resultado02) == 1:
                self.sel_btn2.setText(self.resultado02[0])
            else:
                self.sel_btn2.setText("Multiple Selection")
        else:
            cmds.select(self.resultado02)
    #CONNECTION OF SECOND BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
    def selection03(self):
        self.textinButton = self.sel_btn3.text()  
        self.textInButtonCheck = "Create new Selection"
        if self.textinButton == self.textInButtonCheck :
            self.resultado03 = cmds.ls(sl=True) or []
            if not self.resultado03:
                cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                return
            if len(self.resultado03) == 1:
                self.sel_btn3.setText(self.resultado03[0])
            else:
                self.sel_btn3.setText("Multiple Selection")
        else:
            cmds.select(self.resultado03)
 
    #CONNECTION OF SECOND BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
    def selection04(self):
        self.textinButton = self.sel_btn4.text()  
        self.textInButtonCheck = "Create new Selection"
        if self.textinButton == self.textInButtonCheck :
            self.resultado04 = cmds.ls(sl=True) or []
            if not self.resultado04:
                cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                return
            if len(self.resultado04) == 1:
                self.sel_btn4.setText(self.resultado04[0])
            else:
                self.sel_btn4.setText("Multiple Selection")
        else:
            cmds.select(self.resultado04)
 
    #CONNECTION OF SECOND BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
    def selection05(self):
        self.textinButton = self.sel_btn5.text()  
        self.textInButtonCheck = "Create new Selection"
        if self.textinButton == self.textInButtonCheck :
            self.resultado05 = cmds.ls(sl=True) or []
            if not self.resultado05:
                cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                return
            if len(self.resultado05) == 1:
                self.sel_btn5.setText(self.resultado05[0])
            else:
                self.sel_btn5.setText("Multiple Selection")
        else:
            cmds.select(self.resultado05)
 
    #CREATES THE BUTTON IN VIEWPORT
    HUD_SECTION = 1  # todos los botones van en la misma sección
 
    def create_hud_button(self, index):
        HUD_SECTION = 1  # todos los botones van en la misma sección
        result = getattr(self, "resultado%02d" % index, None)
        if not result:
            cmds.warning("No selection stored in button %d" % index)
            return
     
        name = "HUDButton%02d" % index
     
        # Solo si ESTE botón ya existe, lo quita para recrearlo
        # (no se tocan los otros 4)
        if cmds.headsUpDisplay(name, exists=True):
            cmds.headsUpDisplay(name, rem=True)
     
        label = "Selection%d" % index if len(result) > 1 else result[0]
     
        # Maya devuelve el siguiente bloque que no esté ocupado,
        # contando los HUD que ya creaste antes
        block = cmds.headsUpDisplay(nextFreeBlock=HUD_SECTION)
     
        # Guarda una copia de la selección dentro de la función
        stored = list(result)
        def select_stored(*args):
            cmds.select(stored)
     
        cmds.hudButton(name, s=HUD_SECTION, b=block, vis=1, l=label,
                       bw=80, bsh='roundRectangle', pc=select_stored)
 
    def viewButton01(self): self.create_hud_button(1)
    def viewButton02(self): self.create_hud_button(2)
    def viewButton03(self): self.create_hud_button(3)
    def viewButton04(self): self.create_hud_button(4)
    def viewButton05(self): self.create_hud_button(5)   
    
    
    
    
 
    # Removes the corresponding HUD and resets its selection button.
    def select_trash01(self):
        cmds.headsUpDisplay( 'HUDButton01', rem=True )
        self.resultado01 = []  
        self.textforTrash = "Create new Selection"
        self.sel_btn1.setText(self.textforTrash)        
    # Removes the corresponding HUD and resets its selection button.
    def select_trash02(self):
        cmds.headsUpDisplay( 'HUDButton02', rem=True )
        self.resultado02 = []  
        self.textforTrash2 = "Create new Selection"
        self.sel_btn2.setText(self.textforTrash2)
    # Removes the corresponding HUD and resets its selection button.
    def select_trash03(self):
        cmds.headsUpDisplay( 'HUDButton03', rem=True )
        self.resultado03 = []  
        self.textforTrash3 = "Create new Selection"
        self.sel_btn3.setText(self.textforTrash3)
    # Removes the corresponding HUD and resets its selection button.
    def select_trash04(self):
        cmds.headsUpDisplay( 'HUDButton04', rem=True )
        self.resultado04 = []  
        self.textforTrash4 = "Create new Selection"
        self.sel_btn4.setText(self.textforTrash4)
    # Removes the corresponding HUD and resets its selection button.
    def select_trash05(self):
        cmds.headsUpDisplay( 'HUDButton05', rem=True )
        self.resultado05 = []
        self.textforTrash5 = "Create new Selection"
        self.sel_btn5.setText(self.textforTrash5)
 
open_import_dialog = None
 
def runSelection():
    global open_import_dialog
 
    # Close previous window if it exists
    if open_import_dialog is not None:
        open_import_dialog.close()
        open_import_dialog.deleteLater()
 
    # Create and show a new window
    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()
        
                
if __name__ == "__main__":
    runSelection()
 
