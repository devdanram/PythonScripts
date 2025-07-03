import maya.cmds as cmds

# Seleccionar el locator y luego la superficie
locator = cmds.spaceLocator(name='surface_locator')[0]
surface = 'pPlane1' # change  the name of the surface in the comillas

# apply constraint to locator so it can be around the surface
cmds.geometryConstraint(surface, locator, name='geo_constraint1')
