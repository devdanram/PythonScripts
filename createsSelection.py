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

---------------------------------------
Add this script to a shelf and add this 

import createsSelection
createsSelection.doCreatesSelection()

"""


import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def doCreatesSelection():

    def maya_main_window():
        """
        Return the Maya main window widget as a Python object
        """
        main_window_ptr = omui.MQtUtil.mainWindow()
        if sys.version_info.major >= 3:
            return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        else:
            return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


    class CustomImageWidget(QtWidgets.QWidget):

        def __init__(self, width, height, image_path, parent=None):
            super(CustomImageWidget, self).__init__(parent)

    class OpenImportDialog(QtWidgets.QDialog):

        def __init__(self, parent=maya_main_window()):
            super(OpenImportDialog, self).__init__(parent)

            self.setWindowTitle("Create Custom Selections REDEFINE")
            self.setMinimumSize(320, 160)
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

            self.create_widgets()
            self.create_layout()
            self.create_connections()

        def create_widgets(self):
            #HERE STARTS THE WIDGET CREATION
            
            #FIRST LINE IN THE GUI
            self.filepath_le = QtWidgets.QPushButton("Create new Selection")
            self.filepath_le.setMinimumSize(200,32)        
            self.select_trash_btn = QtWidgets.QPushButton()
            self.select_trash_btn.setIcon(QtGui.QIcon(":trash.png"))        
            self.select_buttonView_btn = QtWidgets.QPushButton()
            self.select_buttonView_btn.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))                
            
            #SECOND LINE IN THE GUI
            self.filepath_le2 = QtWidgets.QPushButton("Create new Selection")
            self.filepath_le2.setMinimumSize(200,32)       
            self.select_trash_btn2 = QtWidgets.QPushButton()
            self.select_trash_btn2.setIcon(QtGui.QIcon(":trash.png"))        
            self.select_buttonView_btn2 = QtWidgets.QPushButton()
            self.select_buttonView_btn2.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))       
                
            #THIRD LINE IN THE GUI    
            self.filepath_le3 = QtWidgets.QPushButton("Create new Selection")
            self.filepath_le3.setMinimumSize(200,32)       
            self.select_trash_btn3 = QtWidgets.QPushButton()
            self.select_trash_btn3.setIcon(QtGui.QIcon(":trash.png"))        
            self.select_buttonView_btn3 = QtWidgets.QPushButton()
            self.select_buttonView_btn3.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))
              
            #FOURTH LINE IN THE GUI      
            self.filepath_le4 = QtWidgets.QPushButton("Create new Selection")
            self.filepath_le4.setMinimumSize(200,32)        
            self.select_trash_btn4 = QtWidgets.QPushButton()
            self.select_trash_btn4.setIcon(QtGui.QIcon(":trash.png"))        
            self.select_buttonView_btn4 = QtWidgets.QPushButton()
            self.select_buttonView_btn4.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))
                
            #FIFTH LINE IN THE GUI    
            self.filepath_le5 = QtWidgets.QPushButton("Create new Selection")
            self.filepath_le5.setMinimumSize(200,32)        
            self.select_trash_btn5 = QtWidgets.QPushButton()
            self.select_trash_btn5.setIcon(QtGui.QIcon(":trash.png"))
            self.select_buttonView_btn5 = QtWidgets.QPushButton()
            self.select_buttonView_btn5.setIcon(QtGui.QIcon(":defaultSingleLayout.png"))
            
            # SIXTH LINE IN THE GUI BUTTON CLOSE
            self.close_btn = QtWidgets.QPushButton("Close")

        def create_layout(self):
            # CREATE THE LAYOUT
            # FIRST LINE HORIZONTAL LAYOUT
            file_path_layout = QtWidgets.QHBoxLayout()
            file_path_layout.addWidget(self.filepath_le)
            file_path_layout.addWidget(self.select_buttonView_btn)
            file_path_layout.addWidget(self.select_trash_btn)
            # SECOND LINE HORIZONTAL LAYOUT
            file_path_layout2 = QtWidgets.QHBoxLayout()
            file_path_layout2.addWidget(self.filepath_le2)
            file_path_layout2.addWidget(self.select_buttonView_btn2)
            file_path_layout2.addWidget(self.select_trash_btn2)
            # THIRD LINE HORIZONTAL LAYOUT
            file_path_layout3 = QtWidgets.QHBoxLayout()
            file_path_layout3.addWidget(self.filepath_le3)
            file_path_layout3.addWidget(self.select_buttonView_btn3)
            file_path_layout3.addWidget(self.select_trash_btn3)
            # FOURTH LINE HORIZONTAL LAYOUT
            file_path_layout4 = QtWidgets.QHBoxLayout()
            file_path_layout4.addWidget(self.filepath_le4)
            file_path_layout4.addWidget(self.select_buttonView_btn4)
            file_path_layout4.addWidget(self.select_trash_btn4)
            # FIFTH LINE HORIZONTAL LAYOUT
            file_path_layout5 = QtWidgets.QHBoxLayout()
            file_path_layout5.addWidget(self.filepath_le5)
            file_path_layout5.addWidget(self.select_buttonView_btn5)
            file_path_layout5.addWidget(self.select_trash_btn5)
            
            #CREATES THE LAYOUT OF 5 LINES
            form_layout = QtWidgets.QFormLayout()
            form_layout.addRow("", file_path_layout)
            form_layout.addRow("", file_path_layout2)
            form_layout.addRow("", file_path_layout3)
            form_layout.addRow("", file_path_layout4)
            form_layout.addRow("", file_path_layout5)
            # ADDDS THE LINE OF THE BUTTON CLOSE
            button_layout = QtWidgets.QHBoxLayout()
            button_layout.addStretch()
            button_layout.addWidget(self.close_btn)
            
            # ADDS BOTH LINES TO THE FINAL LAYOUT
            main_layout = QtWidgets.QVBoxLayout(self)
            main_layout.addLayout(form_layout)
            main_layout.addLayout(button_layout)

        def create_connections(self):
            #CREATES THE CONNECTION OF THE FIRST BUTTONS IN EACH LINE 
            self.filepath_le.clicked.connect(self.selection01)
            self.filepath_le2.clicked.connect(self.selection02)
            self.filepath_le3.clicked.connect(self.selection03)
            self.filepath_le4.clicked.connect(self.selection04)
            self.filepath_le5.clicked.connect(self.selection05)
            # CREATES THE CONNECTION TO CREATE THE BUTTON IN THE VIEWPORT
            self.select_buttonView_btn.clicked.connect(self.viewButton01)
            self.select_buttonView_btn2.clicked.connect(self.viewButton02)
            self.select_buttonView_btn3.clicked.connect(self.viewButton03)
            self.select_buttonView_btn4.clicked.connect(self.viewButton04)
            self.select_buttonView_btn5.clicked.connect(self.viewButton05)
            #CREATES THE CONNECTION TO THE TRASH BUTTON THAT BREAKS THE SELECTION
            self.select_trash_btn.clicked.connect(self.select_trash01)
            self.select_trash_btn2.clicked.connect(self.select_trash02)
            self.select_trash_btn3.clicked.connect(self.select_trash03)
            self.select_trash_btn4.clicked.connect(self.select_trash04)
            self.select_trash_btn5.clicked.connect(self.select_trash05)
            # CREATES CONNECTION TO THE BUTTON CLOSE TO CLOSE THE GUI
            self.close_btn.clicked.connect(self.close)
        
        #CONNECTION OF FIRST BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
        def selection01(self):        
            self.sel01 = cmds.ls(sl=True)
            print self.sel01
            self.textinButton = self.filepath_le.text()
            self.textInButtonCheck = "Create new Selection"

            if self.textinButton == self.textInButtonCheck :
                if ( len(self.sel01) == 0): 
                    cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                else:
                    if ( len(self.sel01) == 1):  
                        print "entre al if para seleccionar un solo objeto"
                        self.seleStr = str(self.sel01)
                        self.resultado = (self.seleStr[3:-2:])         
                        self.filepath_le.setText(self.resultado)

                    else:
                        self.seleStr = str(self.sel01)
                        self.resultado = (self.seleStr)
                        self.filepath_le.setText("Multiple Selection")
                   
            else:
                print self.resultado
                cmds.select(self.resultado)
        #CONNECTION OF SECOND BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
        def selection02(self):        
            self.sel02 = cmds.ls(sl=True)
            self.textinButton2 = self.filepath_le2.text()
            self.textInButtonCheck2 = "Create new Selection"

            if self.textinButton2 == self.textInButtonCheck2 :
                if ( len(self.sel02) == 0): 
                    cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                else:
                    if ( len(self.sel02) == 1):  
                        print "entre al if para seleccionar un solo objeto"
                        self.seleStr2 = str(self.sel02)
                        self.resultado2 = (self.seleStr2[3:-2:])         
                        self.filepath_le2.setText(self.resultado2)
                        return self.resultado2
                        """
                    else:
                        print "entre al else para cambiar el texto a multiptle selection" 
                        self.filepath_le.setText("Multiple Selection")
                        seleccionado02 = cmds.select(self.sel02)
                        return self.resultado2
                        print'esta seleccionando lo guardado sel 02'
                        """
                    
            else:
                cmds.select(self.resultado2)
                
        #CONNECTION OF THRID BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON        
        def selection03(self):        
            self.sel03 = cmds.ls(sl=True)
            self.textinButton3 = self.filepath_le3.text()
            self.textInButtonCheck3 = "Create new Selection"

            if self.textinButton3 == self.textInButtonCheck3:
                if ( len(self.sel03) == 0): 
                    cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                else:
                    if ( len(self.sel03) == 1):  
                        print "entre al if para seleccionar un solo objeto"
                        self.seleStr3 = str(self.sel03)
                        self.resultado3 = (self.seleStr3[3:-2:])         
                        self.filepath_le3.setText(self.resultado3)
                        return self.resultado3
                        """
                    else:
                        print "entre al else para cambiar el texto a multiptle selection" 
                        self.filepath_le.setText("Multiple Selection")
                        seleccionado03 = cmds.select(self.sel03)
                        return self.resultado3
                        print'esta seleccionando lo guardado sel 03'
                        """
                    
            else:
                cmds.select(self.resultado3)
        
        #CONNECTION OF FOURTH BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON       
        def selection04(self):        
            self.sel04 = cmds.ls(sl=True)
            self.textinButton4 = self.filepath_le4.text()
            self.textInButtonCheck4 = "Create new Selection"

            if self.textinButton4 == self.textInButtonCheck4 :
                if ( len(self.sel04) == 0): 
                    cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                else:
                    if ( len(self.sel04) == 1):  
                        print "entre al if para seleccionar un solo objeto"
                        self.seleStr4 = str(self.sel04)
                        self.resultado4 = (self.seleStr4[3:-2:])         
                        self.filepath_le4.setText(self.resultado4)
                        return self.resultado4
                    
            else:
                cmds.select(self.resultado4)


        #CONNECTION OF FIFTH BUTTON TO CHANGE THE NAME OF BUTTON AND ASSIGNS NEW SELECTION TO BUTTON
        def selection05(self):        
            self.sel05 = cmds.ls(sl=True)
            self.textinButton5 = self.filepath_le5.text()
            self.textInButtonCheck5 = "Create new Selection"
            #if len(self.sel01) == 0:
                #print 'entre al nuevo if nuevo que acabo de crear en esteinstante'

            if self.textinButton5 == self.textInButtonCheck5 :
                if ( len(self.sel05) == 0): 
                    cmds.warning( "You have no Selection, Please Select One or More Objects for new Selection" )
                else:
                    if ( len(self.sel05) == 1):  
                        print "entre al if para seleccionar un solo objeto"
                        self.seleStr5 = str(self.sel05)
                        self.resultado5 = (self.seleStr5[3:-2:])         
                        self.filepath_le5.setText(self.resultado5)
                        setterName(resultado5)
                        #self.seleccionado01 = cmds.select(self.sel01)
                        return self.resultado5
                        """
                    else:
                        print "entre al else para cambiar el texto a multiptle selection" 
                        self.filepath_le.setText("Multiple Selection")
                        seleccionado05 = cmds.select(self.sel05)
                        return self.resultado
                        print'esta seleccionando lo guardado sel 01'
                        """
                    
            else:
                cmds.select(self.resultado5)
        #CREATES THE BUTTON IN VIEWPORT
        def viewButton01(self):
            self.labelHUD01 = str(self.sel01)
            self.labelHUD01Str = (self.labelHUD01[3:-2:]) 
            def HUDButton1(*args):
                cmds.select(self.labelHUD01Str)              
            cmds.hudButton('HUDButton01', s=5, b=14, vis=1, l=self.labelHUD01Str, bw=80, bsh='roundRectangle', pc=HUDButton1)     
        #CREATES THE BUTTON IN VIEWPORT       
        def viewButton02(self):
            self.labelHUD02 = str(self.sel02)
            self.labelHUD02Str = (self.labelHUD02[3:-2:]) 
            def HUDButton2(*args):
                cmds.select(self.labelHUD02Str)                     
            cmds.hudButton('HUDButton02', s=5, b=12, vis=1, l=self.labelHUD02Str, bw=80, bsh='roundRectangle', pc=HUDButton2)
        #CREATES THE BUTTON IN VIEWPORT        
        def viewButton03(self):
            self.labelHUD03 = str(self.sel03)
            self.labelHUD03Str = (self.labelHUD03[3:-2:]) 
            def HUDButton3(*args):
                cmds.select(self.labelHUD03Str)                     
            cmds.hudButton('HUDButton03', s=5, b=10, vis=1, l=self.labelHUD03Str, bw=80, bsh='roundRectangle', pc=HUDButton3)
        #CREATES THE BUTTON IN VIEWPORT 
        def viewButton04(self):
            self.labelHUD04 = str(self.sel04)
            self.labelHUD04Str = (self.labelHUD04[3:-2:]) 
            def HUDButton4(*args):
                cmds.select(self.labelHUD04Str)                     
            cmds.hudButton('HUDButton04', s=5, b=8, vis=1, l=self.labelHUD04Str, bw=80, bsh='roundRectangle', pc=HUDButton4)
          
        #CREATES THE BUTTON IN VIEWPORT 
        def viewButton05(self):  
            self.labelHUD05 = str(self.sel05)
            self.labelHUD05Str = (self.labelHUD05[3:-2:]) 
            def HUDButton5(*args):
                cmds.select(self.labelHUD05Str)                     
            cmds.hudButton('HUDButton05', s=5, b=6, vis=1, l=self.labelHUD04Str, bw=80, bsh='roundRectangle', pc=HUDButton5)  
         
         
        #REMOVES THE HUD BUTTON FROM VIEWPORT AND REMOVES NAME IN FIRST BUTTON
        def select_trash01(self):
            cmds.headsUpDisplay( 'HUDButton01', rem=True )
            self.textforTrash = "Create new Selection"
            self.filepath_le.setText(self.textforTrash)          
        #REMOVES THE HUD BUTTON FROM VIEWPORT AND REMOVES NAME IN FIRST BUTTON
        def select_trash02(self):
            cmds.headsUpDisplay( 'HUDButton02', rem=True )
            self.textforTrash2 = "Create new Selection"
            self.filepath_le2.setText(self.textforTrash2)
        #REMOVES THE HUD BUTTON FROM VIEWPORT AND REMOVES NAME IN FIRST BUTTON
        def select_trash03(self):
            cmds.headsUpDisplay( 'HUDButton03', rem=True )
            self.textforTrash3 = "Create new Selection"
            self.filepath_le3.setText(self.textforTrash3)
        #REMOVES THE HUD BUTTON FROM VIEWPORT AND REMOVES NAME IN FIRST BUTTON
        def select_trash04(self):
            cmds.headsUpDisplay( 'HUDButton04', rem=True )
            self.textforTrash4 = "Create new Selection"
            self.filepath_le4.setText(self.textforTrash4)
        #REMOVES THE HUD BUTTON FROM VIEWPORT AND REMOVES NAME IN FIRST BUTTON
        def select_trash05(self):
            cmds.headsUpDisplay( 'HUDButton05', rem=True )
            self.textforTrash5 = "Create new Selection"
            self.filepath_le5.setText(self.textforTrash5)


    if __name__ == "__main__":

        try:
            open_import_dialog.close() # pylint: disable=E0601
            open_import_dialog.deleteLater()
        except:
            pass

        open_import_dialog = OpenImportDialog()
        open_import_dialog.show()