#PASSES ALL THE ANIMATION FROM THE SECONDARY SELECTION TO THE MAIN FIRST SELECTION

"""


INSTRUCTIONS


1. Select the outer control and then inwards until you select the camera


2. RUN SCRIPT


"""





import maya.cmds as cmds


#CHANGE HERE how many frames in range you want to bake


RANGO = 10





#checks the selection and return it as a variable


def selected_object():


curvaslist = []


selected_objects = cmds.ls(selection=True)


print(selected_objects)


if not selected_objects:


return


return selected_objects





def constParts(curvaslist):


#Checks the start and end of the timeslide, it will do it depending on the timeslide that you have in your maya


minPlay = cmds.playbackOptions(q=True, min=True)


maxPlay = cmds.playbackOptions(q=True, max=True)


#this is the curve that is going to use , to put the animation


uno = curvaslist[0]


#selects the camera and save it in a variable


camara = curvaslist[-1]


#creates the locator for the whole movement


camLoc = cmds.spaceLocator(n='camaraLOC')


#passes all the animation to the camera and erases constraint


const = cmds.parentConstraint( camara, camLoc)


cmds.select(camLoc)


cmds.bakeResults( camLoc, sr=True, t=(minPlay, maxPlay))


cmds.delete(const)


#removes animation from curves and camera


for curvas in selected_objects:


cmds.cutKey(curvas, time=(minPlay,maxPlay))


cmds.move( 0, 0, 0, curvas, relative=True )


cmds.rotate( 0, 0, 0, curvas, relative=True )




const = cmds.parentConstraint(camLoc,uno)


cmds.bakeResults( uno, sr=True, t=(minPlay, maxPlay))


cmds.delete(const)


cmds.delete(camLoc)


#this commands starts the program


selected_objects = selected_object()


constParts(selected_objects)

