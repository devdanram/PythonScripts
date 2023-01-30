"""




"""


"""

#SCRIPT NAME Invert Camera

# CREATOR     Daniel Ramirez
# SOURCE  https://www.danielramirez.work

# DESCRIPTION
This script helps to invert the camera if its upside down.   What it does is create 2 locators and parent one to the other one adding to the child  a rotation in Z of 180.  Then constraints to the camera, bakes the main locator.  Deletes the constraint.  Then erase the anim of the camera and constraints the camera to the child locator that has the rotation and then removes the constraint in the camera.  
# USAGE
AFTER YOU RUN THE SCRIPT
After you run the script ,Now you can delete the locators.
HOW TO MAKE IT WORK
Select the second control of the camera “renderCam01camera01:steadycam_matchmove_ctrl”
And then run the script
# LINKS
None
# FEATURES

# VERSIONS 2022 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import inverseCamera
inverseCamera.doInvCamera()

"""



import maya.cmds as cmds

def doInvCamera():

    mainLOC = cmds.spaceLocator(n="mainLOC")

    cmds.scale( 5, 5, 5 )

    rotLOC = cmds.spaceLocator(n="rotLOC")

    cmds.scale( 5, 5, 5 )

    cmds.parent(rotLOC, mainLOC)


    cmds.rotate( 0, 0, 180, 'rotLOC' )



    camCTRL = 'renderCam01camera01:steadycam_matchmove_ctrl'

    constCamLoc = cmds.parentConstraint(camCTRL, mainLOC)


    firstFrame = cmds.playbackOptions(q=True, min=True)

    lastFrame = cmds.playbackOptions(q=True, max=True)


    cmds.bakeSimulation(mainLOC, t=(firstFrame,lastFrame))


    cmds.delete(constCamLoc)


    cmds.select(camCTRL, r=True )


    mySel = cmds.ls(sl=1)

        

    test = []

    try:

        test += cmds.listConnections(mySel,s=True, type="animCurveTU")

    except:

        pass

    try:

        test += cmds.listConnections(mySel,s=True, type="animCurveTL")

    except:

        pass

    try:

        test += cmds.listConnections(mySel,s=True, type="animCurveTA")

    except:

        pass

        

    cmds.delete(test)


    constInverseCam = cmds.parentConstraint(rotLOC ,camCTRL)


    cmds.bakeSimulation(camCTRL, t=(firstFrame,lastFrame))


    cmds.delete(constInverseCam)
