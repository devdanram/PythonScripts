import maya.cmds as cmds

def doFixedCom():
    def queryTextField(*args):
        try:
            inicio = int(cmds.textField(firstFra, query=True, text=True))
            final = int(cmds.textField(lastFra, query=True, text=True))
        except ValueError:
            cmds.warning("Los valores de frame deben ser números enteros.")
            return

        sele = cmds.ls(selection=True, flatten=True)
        if not sele:
            cmds.warning("Selecciona al menos un controlador.")
            return

        for obj in sele:
            # Ir al frame inicial y crear locator de referencia
            cmds.currentTime(inicio)
            loc = cmds.spaceLocator(name=obj + "_LocTemp")[0]
            cmds.delete(cmds.parentConstraint(obj, loc))
            cmds.setAttr(loc + ".scaleX", 5)
            cmds.setAttr(loc + ".scaleY", 5)
            cmds.setAttr(loc + ".scaleZ", 5)

            # Determinar dirección de animación
            if inicio <= final:
                frame_range = range(inicio, final + 1)
            else:
                frame_range = range(inicio, final - 1, -1)
            
            for frame in frame_range:
                cmds.currentTime(frame)
                con = cmds.parentConstraint(loc, obj, maintainOffset=False)
                cmds.setKeyframe(obj, attribute=["translate", "rotate"])
                cmds.delete(con)

            # Eliminar locator
            cmds.delete(loc)

        cmds.inViewMessage(amg='Bake completado.', pos='midCenter', fade=True)

    # UI
    if cmds.window("fixedWin", exists=True):
        cmds.deleteUI("fixedWin")

    window = cmds.window("fixedWin", title="Maintain Position", widthHeight=(400, 100))
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10)
    cmds.text(label='Selecciona el objeto a fijar y define el rango de frames.')
    
    cmds.rowLayout(numberOfColumns=4, columnWidth4=(80, 100, 80, 100), adjustableColumn=2)
    cmds.text(label='Inicio:')
    firstFra = cmds.textField()
    cmds.text(label='Final:')
    lastFra = cmds.textField()
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 200))
    cmds.button(label='Aplicar', command=queryTextField)
    cmds.button(label='Cerrar', command=lambda *args: cmds.deleteUI(window, window=True))
    cmds.setParent('..')

    cmds.showWindow(window)

"""
import constTransFoot
constTransFoot.doFixedCom()
"""
