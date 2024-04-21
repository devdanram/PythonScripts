"""

#SCRIPT NAME ScaleAnimation
# CREATOR     Daniel Ramirez
# SOURCE 

# DESCRIPTION
IN A UI YOU CAN SCALE FRAMES MOVING RESTING RIGHT FRAMES TO MOVE
# USAGE
SELECT THE CONTROLS YOU WANT TO SCALE AND EVERYTHING AFTER THE END FRAME WILL MOVE WHERE THE NEW END FRAME IS EVEN WITH PERCENTAGE OR SPECIFIC END FRAME
# LINKS
None
# FEATURES

# VERSIONS 2024 / 0.1.0: first version
# TODO bugs

"""


import sys
import math

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
from PySide2.QtWidgets import QApplication, QVBoxLayout, QLabel, QFrame

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

class CustomImageWidget(QtWidgets.QWidget):

    def __init__(self, width, height, image_path, parent=None):
        super(CustomImageWidget, self).__init__(parent)
        
class OpenImportDialog(QtWidgets.QDialog):

    def maya_main_window():
        """
        Return the Maya main window widget as a Python object
        """
        main_window_ptr = omui.MQtUtil.mainWindow()
        if sys.version_info.major >= 3:
            return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        else:
            return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

    def __init__(self, parent=maya_main_window()):
        super(OpenImportDialog, self).__init__(parent)
    
        self.setWindowTitle("Scale Animation")
        self.setMinimumSize(480, 160)
        self.setMaximumSize(480, 500)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
    #HERE STARTS THE WIDGET CREATION
        self.aviso        = QtWidgets.QLabel("-------------IMPORTANT:  SELECT THE CONTROLS YOU WANT TO SCALE  ---------------")
        self.linea101     = QtWidgets.QLabel("-------------------------------------------------------------------------------------------------------")
        self.instructions = QtWidgets.QLabel("Tool to scale keys from start frame to end frame, afterwards will move all frames")
        self.linea102     = QtWidgets.QLabel("-------------------------------------------------------------------------------------------------------")
        self.LabelFrText  = QtWidgets.QLabel("Type the Start Frame and End Frame that you need to Scale :")
        
        self.StartFrText = QtWidgets.QLabel("Start Frame")
        self.StartFrLine = QtWidgets.QLineEdit("")
        self.EndFrText = QtWidgets.QLabel("End Frame")
        self.EndFrLine = QtWidgets.QLineEdit("")
        
        self.linea103     = QtWidgets.QLabel("--- Add Percentage or New End Frame ---")
        self.linea104     = QtWidgets.QLabel("If you want to scale down put less than 100%. If you want to scale up more than 100%")
        self.radbxporciento = QtWidgets.QRadioButton("") 
        self.radbxpercLine = QtWidgets.QLineEdit("")
        self.radbxframe = QtWidgets.QRadioButton("") 
        self.radbxframLine = QtWidgets.QLineEdit("")
        self.radbxporciento.setChecked(True)

        
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn    = QtWidgets.QPushButton("Close")

    def create_layout(self):
        # CREATE THE LAYOUT
        text_Layout = QtWidgets.QVBoxLayout()
        text_Layout.addWidget(self.aviso)
        text_Layout.addWidget(self.linea101)
        text_Layout.addWidget(self.instructions)
        text_Layout.addWidget(self.linea102 )
        text_Layout.addWidget(self.LabelFrText)
        
        StartEndFr_Layout = QtWidgets.QHBoxLayout()
        StartEndFr_Layout.addWidget(self.StartFrText)
        StartEndFr_Layout.addWidget(self.StartFrLine)
        StartEndFr_Layout.addWidget(self.EndFrText)
        StartEndFr_Layout.addWidget(self.EndFrLine)
        StartEndFr_Layout.addWidget(self.linea103)
        
        endFrameForm = QtWidgets.QFormLayout()
        endFrameForm.addRow(self.linea103)
        endFrameForm.addRow(self.linea104)
        endFrameForm.addRow("Percentage:",self.radbxporciento)
        endFrameForm.addRow(" % :",self.radbxpercLine)
        endFrameForm.addRow("End  Frame:",self.radbxframe)
        endFrameForm.addRow("Fr :",self.radbxframLine)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("", text_Layout)
        form_layout.addRow("", StartEndFr_Layout)
        form_layout.addRow("", endFrameForm)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
    def create_connections(self):
        self.apply_btn.clicked.connect(self.runProgram)
        self.close_btn.clicked.connect(self.close)
        
    def runProgram(self):
        #get text from start frame and end frame
        stFraVal = self.StartFrLine.text()
        enFraVal = self.EndFrLine.text()
        #turns from string to int
        startNum = int(stFraVal)
        endNumOr = int(enFraVal)
        #how to get the total frames to scale
        totalFr = endNumOr - startNum
        #get the numbers of new end frame or percentage
        percentageVal = int(self.radbxpercLine.text())
        """
        endFrVal = int(self.radbxframLine.text())
        newEndFrame =int(endFrVal)
        """
        #maths to get the frames with percentage to scale
        percentValInt = int(percentageVal)
        porcentajedecimal = percentValInt / 100.00
        percentAframes = totalFr * porcentajedecimal
        framesFinales = startNum + percentAframes

        #if percentageVal > 100:
            #frameTotPercentage = round(startNum + percentAframes)
            #numAumentar = percentValInt - 100
        #elif percentageVal < 100:
            #frameTotPercentage = round(startNum + percentAframes)
            #numBajar = percentValInt - 100
        # print(frameTotPercentage)      
        #--------------------------------------------
        
        #list selection of controls to scale
        selectionCtrls = cmds.ls(sl=True)
        print(selectionCtrls)
        #checks if its checked percentage or frame
       
        frame = endNumOr + 1
        print(frame)
        LastFrame = cmds.findKeyframe(timeSlider=True, which="last")
        print(LastFrame)
        try:
            # Your existing code here...
    
            if self.radbxporciento.isChecked():
                print("dentro del if ")
                cmds.setKeyframe(selectionCtrls,time=frame)
                if percentageVal > 100:
                    resta = percentAframes - totalFr
                    print(resta)
                    frameTotPercentage = round(startNum + percentAframes)
                    print(frameTotPercentage)
                    cmds.keyframe(edit=True,relative=True, timeChange = resta, time=(frame, LastFrame) )
                    for each in selectionCtrls:
                        print(each)
                        cmds.scaleKey(each, time=(startNum, endNumOr), newStartTime=startNum, newEndTime=framesFinales)
                elif percentageVal < 100:
                    
                    percentAframesmenos = (totalFr - (totalFr * porcentajedecimal)) *(-1)
                    frameTotPercentage = round(startNum + percentAframes)
                    for each in selectionCtrls:
                        cmds.scaleKey(each, time=(startNum, endNumOr), newStartTime=startNum, newEndTime=framesFinales)
                    cmds.keyframe(edit=True,relative=True, timeChange=percentAframesmenos, time=(frame, LastFrame) )
                
                for each in selectionCtrls:
                    
                    cmds.scaleKey(each, time=(startNum, endNumOr), newStartTime=startNum, newEndTime=frameTotPercentage)

            elif self.radbxframe.isChecked():
                cmds.setKeyframe(selectionCtrls,time=newEndFrame)
                cmds.keyframe(time=(frame, LastFrame), timeChange=newEndFrame)
                for each in selectionCtrls:
                    cmds.scaleKey(each, time=(startNum, endNumOr), newStartTime=startNum, newEndTime=newEndFrame)

        except Exception as e:
            print("Error:", e)
            
            
  
        if self.radbxporciento.isChecked() == True:
            cmds.keyframe(time=(frame,offset),timeChange=frameTotPercentage)
            cmds.selectKey( time=(startNum,endNumOr) )
            for each in selectionCtrls:
                cmds.scaleKey(each, time=(startNum,endNumOr), newStartTime=startNum, newEndTime=frameTotPercentage )  
        elif self.radbxframe.isChecked() == True:
            cmds.keyframe(time=(frame,offset),timeChange=newEndFrame)
            cmds.selectKey( time=(startNum,endNumOr) )
            for each in selectionCtrls:
                cmds.scaleKey( each, time=(startNum,endNumOr), newStartTime=startNum, newEndTime=newEndFrame)
        
 
        
        
if __name__ == '__main__':
    try:
        open_import_dialog.close() # pylint: disable=E0601
        open_import_dialog.deleteLater()
    except:
        pass
        
    open_import_dialog = OpenImportDialog()
    open_import_dialog.show() 
    
    
