# este es normal va para atras Wz. 50 a 25
import maya.cmds as cmds



def queryTextField(*args):
	firstFraVar = cmds.textField( firstFra , query = True, text = True)
	lastFraVar = cmds.textField( lastFra , query = True, text = True)
	inicio = int(firstFraVar)
	final = int(lastFraVar)
	print (inicio)
	print (final)
	frInicial = inicio
	frConteo = frInicial
	frFinal = final
	frFinalmenosuno = frInicial - 1
	#cantFrames = frFinalmenosuno - frInicial
	cantFrame =  frInicial - frFinal
	print (cantFrame)

	sele = cmds.ls(sl=True, fl=True)

	selCirc = sele[0]

	cmds.currentTime(frInicial)

	locCurve = cmds.spaceLocator(n="consLoc0")
	cmds.scale( 5, 5, 5 )
	consObj = cmds.parentConstraint(sele,locCurve)
	cmds.delete(consObj)

	while frConteo >=  frFinal:
		cmds.currentTime( frConteo )
		print (frConteo)
		consObj = cmds.parentConstraint(locCurve,sele)
		cmds.setKeyframe(sele)
		cmds.delete(consObj)
		frConteo = frConteo - 1
		print (frConteo)
	
	

window = cmds.window( title="Maintain Position REVERSE", widthHeight=(600, 100) )

cmds.rowColumnLayout( numberOfColumns=5, columnAttach=(1, 'both', 0), columnWidth=[(1, 200), (2, 70), (3, 70), (4, 70), (5, 70)] )

cmds.text( label='SET THE TIME FRAME' )

cmds.text( label='' )

cmds.text( label='' )

cmds.text( label='' )

cmds.text( label='' )

cmds.text( label='Type first and Last Frame REVERSE' )

cmds.text( label='First :' )

firstFra = cmds.textField()

cmds.text( label='Last :' )

lastFra = cmds.textField()

cmds.button( label='Apply', command=queryTextField)

cmds.text( label='' )

cmds.text( label='' )

cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

cmds.text( label='' )

cmds.setParent( '..' )

cmds.showWindow( window )
