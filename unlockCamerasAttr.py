#UNLOCK CAMERAS ATTRIBUTES

import pymel.core as pm

cameras = cmds.ls(type='camera')


#change the names of the attributes translate XYZ and rotation XYZ
attributes = ['CamTranslateX', 'CamTranslateY', 'CamTranslateZ','CamTilt', 'CamPan', 'CamRoll']

#CHANGE CAMERA NAME AS EXACTLY AS YOUR CAMERA IN YOUR SCENE

camaraFLO = "ShotCamera:L_stereoCamera"



for attri in attributes:

camara = camaraFLO + '.' + attri

print (camara)

pm.Attribute(camara).__apimplug__().setLocked(False)

