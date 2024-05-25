import maya.cmds as cmds
import random

def queryTextField(*args):
    firstFraVar = cmds.textField( firstFra , query = True, text = True)
    lastFraVar = cmds.textField( lastFra , query = True, text = True)
    freqMinVar = cmds.textField( freqMin , query = True, text = True)
    freqMaxVar = cmds.textField( freqMax , query = True, text = True)
    ampValueVarRotX = cmds.textField( ampValueRotX , query = True, text = True)
    ampValueVarRotY = cmds.textField( ampValueRotY , query = True, text = True)
    ampValueVarRotZ = cmds.textField( ampValueRotZ , query = True, text = True)
    ampValueVarTransX = cmds.textField( ampValueTransX , query = True, text = True)
    ampValueVarTransY = cmds.textField( ampValueTransY , query = True, text = True)
    
    cmds.setKeyframe(at="rotateX")
    cmds.setKeyframe(at="rotateY")
    cmds.setKeyframe(at="rotateZ")
    cmds.setKeyframe(at="translateX")
    cmds.setKeyframe(at="translateY")
    
    #poner inicio y final de frames
    
    inicio = int(firstFraVar)
    final = int(lastFraVar)
    ponerKey = inicio
    	#inicio de programa
    while (ponerKey < final):
        
        selecciondecamara = cmds.ls(selection=True)
        seleccion = selecciondecamara[0]    
        gAttrCamRX = cmds.getAttr(seleccion + ".rotateX")    
        gAttrCamRY = cmds.getAttr(seleccion + ".rotateY")    
        gAttrCamRZ = cmds.getAttr(seleccion + ".rotateZ")    
        gAttrCamTX = cmds.getAttr(seleccion + ".translateX")    
        gAttrCamTY = cmds.getAttr(seleccion + ".translateY")
        frecmin = float(freqMinVar)    
        frecmax = float(freqMaxVar)
        ampvarRX = float(ampValueVarRotX)
        ampvarRY = float(ampValueVarRotY)
        ampvarRZ = float(ampValueVarRotZ)    
        ampvarTX = float(ampValueVarTransX)    
        ampvarTY = float(ampValueVarTransY)    
        ampvarRXmin = (gAttrCamRX - ampvarRX)    
        ampvarRXmax = (gAttrCamRX + ampvarRX)    
        ampvarRYmin = (gAttrCamRY - ampvarRY)    
        ampvarRYmax = (gAttrCamRY + ampvarRY)    
        ampvarRZmin = (gAttrCamRZ - ampvarRZ)    
        ampvarRZmax = (gAttrCamRZ + ampvarRZ)    
        ampvarTXmin = (gAttrCamTX - ampvarTX)    
        ampvarTXmax = (gAttrCamTX + ampvarTX)  
        ampvarTYmin = (gAttrCamTY - ampvarTY)    
        ampvarTYmax = (gAttrCamTY + ampvarTY)    
        #saca random valores de la amplitud para el movimiento de la camara    
        ampRX = random.uniform(ampvarRXmin,ampvarRXmax)   
        ampRY = random.uniform(ampvarRYmin,ampvarRYmax)   
        ampRZ = random.uniform(ampvarRZmin,ampvarRZmax)    
        ampTX = random.uniform(ampvarTXmin,ampvarTXmax)    
        ampTY = random.uniform(ampvarTYmin,ampvarTYmax)    
        #moverse alsiguiente keyframe    
        cmds.currentTime( ponerKey )    
        #poner valores en la camara    
        #print seleccion    
        cmds.setAttr(seleccion+".rotateX", ampRX)    
        cmds.setAttr(seleccion+".rotateY", ampRY)    
        cmds.setAttr(seleccion+".rotateZ", ampRZ)   
        cmds.setAttr(seleccion+".translateX", ampTX)    
        cmds.setAttr(seleccion+".translateY", ampTY)
        #set keyframe    
        cmds.setKeyframe(at="rotateX")   
        cmds.setKeyframe(at="rotateY")    
        cmds.setKeyframe(at="rotateZ")    
        cmds.setKeyframe(at="translateX")    
        cmds.setKeyframe(at="translateY")    
        #decide el siguiente keyframe de una manera random    
        siguienteFrameKey = int(random.uniform(frecmin, frecmax))    
        ponerKey = ponerKey + siguienteFrameKey
# Make a new window

window = cmds.window(title="Camera Shake", widthHeight=(600, 600))
cmds.rowColumnLayout(numberOfColumns=5, columnAttach=(1, 'both', 0), columnWidth=[(1, 200), (2, 70), (3, 70), (4, 70), (5, 70)])
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='A L E R T S E L E C T' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label=' C A M E R A F I R S T !!' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='SET THE TIME FRAME' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='Type first and Last Frame' )
cmds.text( label='First :' )
firstFra = cmds.textField()
cmds.text( label='Last :' )
lastFra = cmds.textField()

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )


cmds.text( label='SET THE FREQUENCY' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='Type the frequency' )
cmds.text( label='Freq Min :' )
freqMin = cmds.textField()
cmds.text( label='Freq Max :' )
freqMax = cmds.textField()

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='AMPLITUDE OF MOVEMENT' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='Type the amplitude in Rotation X' )
cmds.text( label='' )
cmds.text( label='Rotation X :' )
ampValueRotX = cmds.textField()
cmds.text( label='' )
cmds.text( label='Type the amplitude in Rotation Y' )
cmds.text( label='' )
cmds.text( label='Rotation Y :' )
ampValueRotY = cmds.textField()
cmds.text( label='' )

cmds.text( label='Type the amplitude in Rotation Z' )
cmds.text( label='' )
cmds.text( label='Rotation Z :' )
ampValueRotZ = cmds.textField()
cmds.text( label='' )

cmds.text( label='Type the amplitude in Translation X' )
cmds.text( label='' )
cmds.text( label='Translation X :' )
ampValueTransX = cmds.textField()
cmds.text( label='' )


cmds.text( label='Type the amplitude in Translation Y' )
cmds.text( label='' )
cmds.text( label='Translation Y :' )
ampValueTransY = cmds.textField()
cmds.text( label='' )

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )


cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.button( label='Apply CamShake', command=queryTextField)
cmds.text( label='' )
cmds.text( label='' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.text( label='' )

cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )

cmds.setParent( '..' )

cmds.showWindow(window)
