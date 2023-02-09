"""

#SCRIPT NAME Bake Animation in 1s or 2s
# CREATOR     Daniel Ramirez
# SOURCE 

# DESCRIPTION
you can bake a control animated into 1s or 2s
# USAGE
select a control to bake the animation in 2s so i can look like it is animated in 2s and looks like stop motion
# LINKS
None
# FEATURES

# VERSIONS 2022 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import bakeAnim1or2
bakeAnim1or2.doBakeAnim1or2()

"""


import sys
import maya.cmds as cmds
from PySide2 import QtCore
from PySide2 import QtWidgets

import random

class TabWidgetDialog(QtWidgets.QDialog):

    WINDOW_TITLE = "MMM 1s & 2s"

    def __init__(self, parent=None):
        super(TabWidgetDialog, self).__init__(parent)

        self.setWindowTitle(self.WINDOW_TITLE)
        if cmds.about(ntOS=True):
            self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        elif cmds.about(macOS=True):
            self.setWindowFlags(QtCore.Qt.Tool)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.baketext1 = QtWidgets.QLabel("Animation in 1s and 2s")
        self.baketext2 = QtWidgets.QLabel("-------------------IMPORTANT-----------------------")
        self.baketext3 = QtWidgets.QLabel("Please select the controls to bake in 1s or 2s")
        self.baketext4 = QtWidgets.QLabel("----------------------------------------------------------")

        self.baketext5 = QtWidgets.QLabel("Start Frame")
        self.bakeStartFrame = QtWidgets.QLineEdit("")
        self.baketext6 = QtWidgets.QLabel("End Frame")
        self.bakeEndFrame = QtWidgets.QLineEdit("")

        self.baketext7 = QtWidgets.QLabel("Please Select if its 1's or 2's")
        self.bakeradio1s = QtWidgets.QRadioButton("1's", parent=None)
        self.bakeradio2s = QtWidgets.QRadioButton("2's", parent=None)

        self.baketext7 = QtWidgets.QLabel("------------------------------------------------------------------------")
        self.checboxRandom = QtWidgets.QCheckBox("Check if you want Randomization ")
        self.randomtext8 = QtWidgets.QLabel("------------------------------------------------------------------------")
        self.randomtextRandTr = QtWidgets.QLabel("Random Translation Value ex. 0.05")
        self.randomValueTr = QtWidgets.QLineEdit("0")
        self.randomtextRandRo = QtWidgets.QLabel("Random Rotation Value ex. 0.05")
        self.randomValueRo = QtWidgets.QLineEdit("0")
        self.randomtext9 = QtWidgets.QLabel("Please add Frequency Value ")

        self.randomtext11 = QtWidgets.QLabel("Frequency ex. 6")
        self.randomFreq = QtWidgets.QLineEdit("0")

        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):

        layouttext = QtWidgets.QVBoxLayout() 
        layouttext.addWidget(self.baketext1)
        layouttext.addWidget(self.baketext2)
        layouttext.addWidget(self.baketext3)
        layouttext.addWidget(self.baketext4)

        layoutStfra = QtWidgets.QHBoxLayout() 
        layoutStfra.addWidget(self.baketext5)
        layoutStfra.addWidget(self.bakeStartFrame)

        layoutEndfra = QtWidgets.QHBoxLayout()
        layoutEndfra.addWidget(self.baketext6)
        layoutEndfra.addWidget(self.bakeEndFrame)

        layouttext.addWidget(self.bakeradio1s)
        layouttext.addWidget(self.bakeradio2s)


        radioBtnLayout = QtWidgets.QHBoxLayout()
        radioBtnLayout.addWidget(self.bakeradio1s)
        radioBtnLayout.addWidget(self.bakeradio2s)

        layoutCheckTrRot = QtWidgets.QVBoxLayout()
        layoutCheckTrRot.addWidget(self.baketext7)
        layoutCheckTrRot.addWidget(self.checboxRandom)
        layoutCheckTrRot.addWidget(self.randomtext8)

        layoutValTrInt = QtWidgets.QHBoxLayout()
        layoutValTrInt.addWidget(self.randomtextRandTr)
        layoutValTrInt.addWidget(self.randomValueTr)

        layoutValRotInt = QtWidgets.QHBoxLayout()
        layoutValRotInt.addWidget(self.randomtextRandRo)
        layoutValRotInt.addWidget(self.randomValueRo)

        layoutFreq = QtWidgets.QVBoxLayout()
        layoutFreq.addWidget(self.randomtext9)

        layoutFreqVal = QtWidgets.QHBoxLayout()
        layoutFreqVal.addWidget(self.randomtext11)
        layoutFreqVal.addWidget(self.randomFreq)

        btnlayout = QtWidgets.QVBoxLayout() 
        btnlayout.addWidget(self.apply_btn)
        btnlayout.addWidget(self.close_btn)

        form_Layout = QtWidgets.QFormLayout()
        form_Layout.addRow(layouttext)
        form_Layout.addRow(layoutStfra)
        form_Layout.addRow(layoutEndfra)
        form_Layout.addRow(radioBtnLayout)

        form_Layout.addRow(layoutCheckTrRot)

        form_Layout.addRow(layoutValTrInt)
        form_Layout.addRow(layoutValRotInt)

        form_Layout.addRow(layoutFreq)

        form_Layout.addRow(layoutFreqVal)

        form_Layout.addRow(btnlayout)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addLayout(form_Layout)

    def create_connections(self):

        self.bakeradio1s.toggled.connect(self.baketoggle(self.bakeradio1s))
        self.bakeradio2s.toggled.connect(self.baketoggle(self.bakeradio2s))
        self.checboxRandom.toggled.connect(self.randomcheck(self.checboxRandom))

        self.apply_btn.clicked.connect(self.runProgram)
        self.close_btn.clicked.connect(self.close)
    def randomcheck(self, chec):
        if self.checboxRandom.isChecked() ==True:
            self.checboxRandomTrue = True
            return self.checboxRandomTrue
    def baketoggle(self, radio):
        if self.bakeradio1s.isChecked() == True:        
            self.radio1s = 1 
            print self.radio1s
            return self.radio1s
        if self.bakeradio1s.isChecked() == True:        
            self.radio2s = 2
            print self.radio2s
            return self.radio2s         

        #------------------Program Starts HERE--------------------------  
    def runProgram(self):
        #variables
        stFraVal = self.bakeStartFrame.text()
        enFraVal = self.bakeEndFrame.text()
        startNum = int(stFraVal)
        endNumOr = int(enFraVal)
        endNum = endNumOr + 1
        trvalue = self.randomValueTr.text()
        rovalue = self.randomValueRo.text()
        trvalint= float(trvalue)
        rovalueint = float(rovalue)
        freqvalue = self.randomFreq.text()
        print endNum
        print startNum
        #checks if the radio 1s is checked
        if self.bakeradio1s.isChecked() == True:
            radionum  = 1 
            cmds.currentTime(startNum)
            startEraseFrames = startNum + 1
            frameVar = startNum
            frameJump = radionum
            endOfScene = endNum
            selesin = cmds.ls(sl=True)
            while frameVar <= endOfScene:
                for each in selesin:
                    cmds.setKeyframe(each,insert=True)
                    #heres check if the random checkbox is checked to see if it wiill add randomization only if its true
                    if self.checboxRandom.isChecked() == True:
                        low = 1
                        high = freqvalue
                        ran_number = int(random.randint(low, high))
                        minValT = trvalint * -1
                        maxValT = trvalint
                        minValR = rovalueint * -1
                        maxValR = rovalueint
                        TXselA = each + ".translateX"
                        TYselA = each + ".translateY"
                        TZselA = each + ".translateZ"
                        RXselA = each + ".rotateX"
                        RYselA = each + ".rotateY"
                        RZselA = each + ".rotateZ"

                        if not (cmds.getAttr(TXselA, lock=True)):
                            ran_numberTX = int(random.randint(low, high))
                            if ran_numberTX == 1:
                                getTX = cmds.getAttr(TXselA)
                                valTX = getTX + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TXselA, valTX)

                        if not (cmds.getAttr(TYselA, lock=True)):
                            ran_numberTY = int(random.randint(low, high))
                            if ran_numberTY == 1:
                                getTY = cmds.getAttr(TYselA)
                                valTY = getTY + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TYselA, valTY)

                        if not (cmds.getAttr(TZselA, lock=True)):
                            ran_numberTZ = int(random.randint(low, high))
                            if ran_numberTZ == 1:
                                getTZ = cmds.getAttr(TZselA)
                                valTZ = getTZ + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TZselA, valTZ)

                        if not (cmds.getAttr(RXselA, lock=True)):
                            ran_numberRX = int(random.randint(low, high))
                            if ran_numberRX == 1:
                                getRX = cmds.getAttr(RXselA)
                                valRX = getRX + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RXselA, valRX)

                        if not (cmds.getAttr(RYselA, lock=True)):
                            ran_numberRY = int(random.randint(low, high))
                            if ran_numberRY == 1:
                                getRY = cmds.getAttr(RYselA)
                                valRY = getRY + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RYselA, valRY)

                        if not (cmds.getAttr(RZselA, lock=True)):
                            ran_numberRZ = int(random.randint(low, high))
                            if ran_numberRZ == 1:
                                getRZ = cmds.getAttr(RZselA)
                                valRZ = getRZ + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RZselA, valRZ)


                cmds.currentTime(frameVar)
                frameVar = frameVar + 1

            for each in selesin:
                endTang = endOfScene - 3
                cmds.keyTangent(each,edit=True, outTangentType='step', time=(startNum,endTang) )

            selesin = 0                   

        elif self.bakeradio2s.isChecked() == True: 
            radionum  = 2       
            cmds.currentTime(startNum)
            startEraseFrames = startNum + 1
            frameVar = startNum
            frameJump = radionum
            endOfScene = endNum
            selesin = cmds.ls(sl=True)
            print selesin
            while frameVar <= endOfScene:
                for each in selesin:
                    cmds.setKeyframe(each,insert=True)
                    if self.checboxRandom.isChecked() == True:
                        low = 1
                        high = 2
                        ran_number = int(random.randint(low, high))
                        minValT = trvalint * -1
                        maxValT = trvalint
                        minValR = rovalueint * -1
                        maxValR = rovalueint
                        TXselA = each + ".translateX"
                        TYselA = each + ".translateY"
                        TZselA = each + ".translateZ"
                        RXselA = each + ".rotateX"
                        RYselA = each + ".rotateY"
                        RZselA = each + ".rotateZ"                       
                        if not (cmds.getAttr(TXselA, lock=True)):
                            ran_numberTX = int(random.randint(low, high))
                            if ran_numberTX == 1:
                                getTX = cmds.getAttr(TXselA)
                                valTX = getTX + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TXselA, valTX)

                        if not (cmds.getAttr(TYselA, lock=True)):
                            ran_numberTY = int(random.randint(low, high))
                            if ran_numberTY == 1:
                                getTY = cmds.getAttr(TYselA)
                                valTY = getTY + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TYselA, valTY)

                        if not (cmds.getAttr(TZselA, lock=True)):
                            ran_numberTZ = int(random.randint(low, high))
                            if ran_numberTZ == 1:
                                getTZ = cmds.getAttr(TZselA)
                                valTZ = getTZ + (random.uniform(minValT, maxValT))
                                cmds.setAttr(TZselA, valTZ)

                        if not (cmds.getAttr(RXselA, lock=True)):
                            ran_numberRX = int(random.randint(low, high))
                            if ran_numberRX == 1:
                                getRX = cmds.getAttr(RXselA)
                                valRX = getRX + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RXselA, valRX)

                        if not (cmds.getAttr(RYselA, lock=True)):
                            ran_numberRY = int(random.randint(low, high))
                            if ran_numberRY == 1:
                                getRY = cmds.getAttr(RYselA)
                                valRY = getRY + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RYselA, valRY)

                        if not (cmds.getAttr(RZselA, lock=True)):
                            ran_numberRZ = int(random.randint(low, high))
                            if ran_numberRZ == 1:
                                getRZ = cmds.getAttr(RZselA)
                                valRZ = getRZ + (random.uniform(minValR, maxValR))
                                cmds.setAttr(RZselA, valRZ)


                cmds.currentTime(frameVar)
                frameVar = frameVar + 1
            EraseFrames = startEraseFrames
            while EraseFrames <= endOfScene:
                cmds.currentTime(EraseFrames)
                for each in selesin:
                    cmds.cutKey(each, time=(EraseFrames,EraseFrames), option="keys", clear=True)
                EraseFrames = EraseFrames + frameJump
            #cmds.selectKey( time=(frameVar,endOfScene) )
            #cmds.keyTangent(inTangentType='spline')

            for each in selesin:

                endTang = endOfScene - 3
                cmds.keyTangent(each,edit=True, outTangentType='step', time=(startNum,endTang) ) 


            selesin = 0
        #------------------Prograam ends HERE--------------------------               
def runAnim():
    try:
        tabbar_dialog.close() # pylint: disable=E0601
        tabbar_dialog.deleteLater()
    except:
        pass
    tabbar_dialog = TabWidgetDialog()
    tabbar_dialog.show()

if __name__ == '__main__':
    runAnim()
        
