"""

#SCRIPT NAME NukeScript
# CREATOR     Daniel Ramirez
# SOURCE 

# DESCRIPTION

# USAGE

# LINKS
None
# FEATURES

# VERSIONS 2022 / 0.1.0: first version
# TODO bugs

---------------------------------------
Add this script to a shelf and add this 

import nukeScript
nukeScript.doNukeScript()

"""

def doNukeScript():

    node = nuke.selectedNode()

    savex = node.xpos()

    savey = node.ypos()

    print(savex, savey)



    initialx = savex 

    initialy = savey

    initialxcons = savex

    initialycons = savey+300

    initialyconsText = savey+400

    initialyconsConSh = savey+600

    sumax = 100

    sumay = 360

    selectedNodeVar = nuke.selectedNode()

    print selectedNodeVar

    layerList = [i for i in nuke.layers(selectedNodeVar)]

    print layerList



    sumLayerList = len(layerList)

    print sumLayerList

    if 1 <= sumLayerList <= 10:

        widthValue = 6000

        heightValue = 2000

        rowValue = 2

        columnValue = 5

    elif 11 <= sumLayerList <= 20:

        widthValue = 5800

        heightValue = 3200

        rowValue = 4

        columnValue = 5

    elif 21 <= sumLayerList <= 30:

        widthValue = 6500

        heightValue = 2000

        rowValue = 5

        columnValue = 6

    elif 31 <= sumLayerList <= 40:

        widthValue = 6500

        heightValue = 4500

        rowValue = 6

        columnValue = 6



    print widthValue

    print heightValue

    print rowValue

    print columnValue



    ConShVal = savey + 400

    contactSheetVar = nuke.nodes.ContactSheet()

    contactSheetVar['xpos'].setValue(savex)

    contactSheetVar['ypos'].setValue(initialyconsConSh)

    contactSheetVar.knob('width').setValue(widthValue)

    contactSheetVar.knob('height').setValue(heightValue)

    contactSheetVar.knob('rows').setValue(rowValue)

    contactSheetVar.knob('columns').setValue(columnValue)

    contactSheetVar.knob('roworder').setValue('TopBottom')

    contactSheetVar.knob('colorder').setValue('LeftRight')

    sumatoria = 0

    for i in layerList:

        initialx = initialx + sumax      

        print i

        shuffleVar = nuke.nodes.Shuffle()

        shuffleVar['label'].setValue(i)

        shuffleVar['xpos'].setValue(initialx)

        shuffleVar['ypos'].setValue(initialycons)

        shuffleVar['in'].setValue(i)

        

        textVar = nuke.nodes.Text(box = '2222 240 1646 512', translate = '290 -170', center = '1010 690')

        textVar['label'].setValue(i)

        textVar['xpos'].setValue(initialx)

        textVar['ypos'].setValue(initialyconsText)

        textVar.knob('message').setValue(i)

        textVar.knob('size').setValue(80)

        textVar.knob('xjustify').setValue('right')

        textVar.knob('yjustify').setValue('bottom')

        textVar.knob('font').setValue('/usr/share/fonts/msttcore/trebuc.ttf')

        textVar.knob('box').setValue(2222, 240)

        textVar.knob('translate').setValue(290,690)


        textVar.setInput(0, shuffleVar)


        shuffleVar.setInput(0, selectedNodeVar)


        contactSheetVar.setInput(sumatoria, textVar)

        sumatoria = sumatoria + 1