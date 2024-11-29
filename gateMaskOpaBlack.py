import maya.cdms as cmds
cameras = cmds.ls(type=("camera"), l=True)
for cam in cameras:
  camdisplayGateMask = cam + ".displayGateMaskOpacity"
  cmds.setAttr(camdisplayGateMask,1)
