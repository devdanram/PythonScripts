"""

#SCRIPT NAME Mirror One Control in Rig

# CREATOR     Daniel Ramirez
# SOURCE  https://www.danielramirez.work

# DESCRIPTION
Use this script to mirror one control you select in the Character rig like a IK hand or in a IK foot or FKs
# USAGE
Just control the curve and the control will mirror in the other side
only works with this name in the control ':r_' or ':l_'
# LINKS
None
# FEATURES

# VERSIONS 2022 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import mirrorControl
mirrorControl.doMirrorControl()

"""



import maya.cmds as cmds
import re


def doMirrorControl():

	selesin = cmds.ls(sl=True)
	sele = selesin[0]

	TXselA = sele + ".translateX"
	TYselA = sele + ".translateY"
	TZselA = sele + ".translateZ"
	RXselA = sele + ".rotateX"
	RYselA = sele + ".rotateY"
	RZselA = sele + ".rotateZ"
	getTXA = cmds.getAttr(TXselA)
	getTYA = cmds.getAttr(TYselA)
	getTZA = cmds.getAttr(TZselA)
	getRXA = cmds.getAttr(RXselA)
	getRYA = cmds.getAttr(RYselA)
	getRZA = cmds.getAttr(RZselA)

	getTXAint = float(getTXA)
	getTYAint = float(getTYA)
	getTZAint = float(getTZA)
	getRXAint = float(getRXA)
	getRYAint = float(getRYA)
	getRZAint = float(getRZA)


	seleStr = str(selesin)

	phoneNumRegex = re.compile(r':l_')
	resultadostr = str(phoneNumRegex.findall(seleStr))

	resultado = (resultadostr[2:-2:])

	lfvar = ':l_'

	if lfvar == resultado:
		outputrt = seleStr.replace(':l_',':r_')
	else:
		outputrt = seleStr.replace(':r_',':l_')

	cambioLado = (outputrt[3:-2:])


	nameSelected = cmds.select(cambioLado)
	sel = cmds.ls(sl=True)
	seleB = sel[0]

	TXselB = seleB + ".translateX"
	TYselB = seleB + ".translateY"
	TZselB = seleB + ".translateZ"
	RXselB = seleB + ".rotateX"
	RYselB = seleB + ".rotateY"
	RZselB = seleB + ".rotateZ"

	if not (cmds.getAttr(TXselA, lock=True)):
		cmds.setAttr(TXselB, getTXAint)

	if not (cmds.getAttr(TYselA, lock=True)):
		cmds.setAttr(TYselB, getTYAint)

	if not (cmds.getAttr(TZselA, lock=True)):
		cmds.setAttr(TZselB, getTZAint)

	if not (cmds.getAttr(RXselA, lock=True)):
		cmds.setAttr(RXselB, getRXAint)

	if not (cmds.getAttr(RYselA, lock=True)):
		cmds.setAttr(RYselB, getRYAint)

	if not (cmds.getAttr(RZselA, lock=True)):
		cmds.setAttr(RZselB, getRZAint)
