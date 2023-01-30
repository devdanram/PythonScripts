 
'''
#SCRIPT NAME Master Locator

# CREATOR     Daniel Ramirez
# SOURCE      https://www.danielramirez.work
# DESCRIPTION
#  Creates a master locator in the center of the objects selected 
#  and creates a locator in the objects selected
# USAGE
# LINKS
# FEATURES
# VERSIONS 2020 / 0.1.0: first version
# TODO bugs
---------------------------------------
Add this script to a shelf and add this 

import masterLoc
masterLoc.doMasterLoc()

'''

#  Creates a master locator in the center of the objects selected 
#  and creates a locator in the objects selected

'''


'''
import maya.cmds as cmds
import re

def doMasterLoc():

	#saves the selection to sel
	sel = cmds.ls(sl=True)

	#declare variables num and list grpLocs
	num = 0
	grpLocs = []
	locSc = 5
	#iterate the selection one by one to add a locator and constraints to the curve selected
	for eachCurve in sel:
		locCurve = cmds.spaceLocator(n="consLoc0")
		#---------------------------------
	#you can change the scale of the locators for each curve, cmds.scale( ##, ##, ## )
		cmds.scale( locSc, locSc, locSc )
	#---------------------------------
		grpLocs.append(locCurve)
		#here moves the locator to the curve
		consObj = cmds.parentConstraint(eachCurve,locCurve)
		cmds.delete(consObj)
		consObj = cmds.parentConstraint(locCurve,eachCurve)
		num = num + 1
		#the IF checks if there is no more curves to add locators
		print"empieza el if para notar que ya se acabaron las curvas"
		if len(sel) == num:
				#here starts the code to find the center of the curves selected
				count = len(sel)
				sums = [0,0,0]
				for item in sel:
				pos = mc.xform(item, q=True, t=True)
				sums[0] += pos[0]
				sums[1] += pos[1]
				sums[2] += pos[2]
			center = [sums[0]/count, sums[1]/count, sums[2]/count]
			posX = float(center[0])
			posZ = float(center[2])
			print posX
			print center[1]
			print posZ
			#creates the Main Locator to move everything
			locMain = cmds.spaceLocator(n="locMainTRS")
			#moves the Main Locator to the center of the selection
			cmds.move( posX, 0, posZ )
			
	#---------------------------------
			#you can change the scale of the locators for each curve in locSc = #
			
			cmds.scale( locSc, locSc, locSc )
			#---------------------------------
			print grpLocs
			#here every locator from the curve is constrained to the main Locator
			for eachLoc in grpLocs:
				MainConst0 = cmds.parentConstraint(locMain,eachLoc,maintainOffset=True)
