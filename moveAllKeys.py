"""

#SCRIPT NAME Move All Aniamted Keys 
# CREATOR     Daniel Ramirez
# SOURCE  https://www.danielramirez.work

# DESCRIPTION
You can move all the animated keys with a UI whereever you want in the timeline
# USAGE
just run the script and put the frames you want to move the keys back or forth
# LINKS
None
# FEATURES

# VERSIONS 2022 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import moveAllKeys
moveAllKeys.doMoveAllKeys()

"""

import maya.cmds as cmds

def doMoveAllKeys():


	def moveKeys(*args):

		iNumFrames= cmds.textField( keysDesplazar , query = True, text = True)

		anim_curves = cmds.ls(type=['animCurveTA', 'animCurveTL', 'animCurveTT', 'animCurveTU'])

		print anim_curves

		for each in anim_curves:

			cmds.keyframe(each, edit=True, relative=True, timeChange=iNumFrames)



	window = cmds.window( title="Move Keys", widthHeight=(520, 100) )

	cmds.rowColumnLayout( numberOfColumns=3, columnAttach=(1, 'both', 0), columnWidth=[(1, 10), (2, 250),(3, 250)] )


	cmds.text( label='' )

	cmds.text( label='' )

	cmds.text( label='' )


	cmds.text( label='' )

	cmds.text( label='YOU DONT HAVE TO SELECT ANYTHING' )

	cmds.text( label='' )


	cmds.text( label='' )

	cmds.text( label='Put a number to move the keys' )

	cmds.text( label='(Ex.: 5, 10, -6, -9)' )


	cmds.text( label='' )

	cmds.text( label = 'Numbers in negative and positive values :' )

	keysDesplazar = cmds.textField()


	cmds.text( label='' )

	cmds.text( label='' )

	cmds.text( label='' )


	cmds.text( label='' )

	cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

	cmds.button( label='Apply MoveKeys', command=moveKeys)


	cmds.setParent( '..' )

	cmds.showWindow( window )
