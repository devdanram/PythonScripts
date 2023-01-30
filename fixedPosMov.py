 
'''
#SCRIPT NAME Fixed Position Movement Object

# CREATOR     Daniel Ramirez
# SOURCE      https://www.danielramirez.work
# DESCRIPTION
# You can put an object to make it remain the position of an object even the main rig is moving
#  example when you have the rig, and is moving, you can make static the foot that shouldnt be moving
# USAGE
# LINKS
# FEATURES
# VERSIONS 2020 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import fixedPosMov
fixedPosMov.doFixedPoMo()

'''

import maya.cmds as cmds

def doFixedPoMo():

	def queryTextField(*args):
		firstFraVar = cmds.textField( firstFra , query = True, text = True)
		lastFraVar = cmds.textField( lastFra , query = True, text = True)
		inicio = int(firstFraVar)
		final = int(lastFraVar)
		print inicio
		print final
		frInicial = inicio
		frConteo = frInicial
		frFinal = final
		frFinalmasuno = frFinal + 1
		cantFrames = frFinalmasuno - frInicial
		print cantFrames

		sele = cmds.ls(sl=True, fl=True)

		selCirc = sele[0]

		cmds.currentTime(frInicial)

		locCurve = cmds.spaceLocator(n="consLoc0")
		cmds.scale( 5, 5, 5 )
		consObj = cmds.parentConstraint(sele,locCurve)
		cmds.delete(consObj)

		while frConteo < frFinalmasuno:
			cmds.currentTime( frConteo )
			print frConteo
			consObj = cmds.parentConstraint(locCurve,sele)
			cmds.setKeyframe(sele)
			cmds.delete(consObj)
			frConteo = frConteo + 1
			print frConteo




	window = cmds.window( title="Maintain Position", widthHeight=(600, 100) )

	cmds.rowColumnLayout( numberOfColumns=5, columnAttach=(1, 'both', 0), columnWidth=[(1, 200), (2, 70), (3, 70), (4, 70), (5, 70)] )

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

	cmds.button( label='Apply', command=queryTextField)

	cmds.text( label='' )

	cmds.text( label='' )

	cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

	cmds.text( label='' )

	cmds.setParent( '..' )

	cmds.showWindow( window )