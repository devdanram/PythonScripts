import maya.cmds as cmds

def moveKeys(*args):
    try:
        # Get the number of frames to move
        iNumFrames = float(cmds.textField(keysDesplazar, query=True, text=True))
        
        # Get the start and end frame range
        startFrame = int(cmds.textField(startFrameField, query=True, text=True))
        endFrame = int(cmds.textField(endFrameField, query=True, text=True))
    except ValueError:
        cmds.warning("Please enter valid numbers for all fields.")
        return

    # Get all animation curves in the scene
    anim_curves = cmds.ls(type=['animCurveTA', 'animCurveTL', 'animCurveTT', 'animCurveTU'])

    if not anim_curves:
        cmds.warning("No animation curves found in the scene.")
        return

    # Move the keys within the specified range
    for each in anim_curves:
        cmds.keyframe(each, edit=True, relative=True, timeChange=iNumFrames, time=(startFrame, endFrame))

    print(f"Keys moved by {iNumFrames} frames from frame {startFrame} to {endFrame}.")

# Create the window
window = cmds.window(title="Move Keys", widthHeight=(320, 225))
cmds.columnLayout(adjustableColumn=True)

cmds.text(label="YOU DON'T HAVE TO SELECT ANYTHING", align='center', height=20)
cmds.text(label="Enter a number to move the keys (e.g., 5, -6,):", align='center', height=20)
cmds.text(label="If its 5 , it will move the keys 5 frames forward", align='center', height=20)
cmds.text(label="If its -5 , it will move the keys 5 frames backwards", align='center', height=20)

keysDesplazar = cmds.textField()

cmds.text(label="Specify the frame range:", align='center', height=20)
cmds.rowLayout(numberOfColumns=4, adjustableColumn=2)
cmds.text(label="Start Frame:")
startFrameField = cmds.textField()
cmds.text(label="End Frame:")
endFrameField = cmds.textField()
cmds.setParent('..')

cmds.button(label="Apply MoveKeys", command=moveKeys, height=40)
cmds.button(label="Close", command=lambda _: cmds.deleteUI(window, window=True), height=30)

cmds.showWindow(window)
