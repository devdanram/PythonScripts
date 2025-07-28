'''
#SCRIPT Shot Splitter from Sequencer

# CREATOR     Daniel Ramirez
# SOURCE      https://www.danielramirez.work
# DESCRIPTION
#  Creates shots in the specified folder or creates the folder and saves each shot in that folder moving all the keys and saves the scene with the right timeline
# USAGE  create the shots in sequencer and run the script 
# LINKS
# FEATURES
# VERSIONS 2025 / 0.1.0: first version
# TODO create a UI to select the folder 
'''
import maya.cmds as cmds
import os

def move_keys_to_zero(start_frame, i):
    anim_curves = cmds.ls(type=['animCurveTA', 'animCurveTL', 'animCurveTT', 'animCurveTU']) or []
    
    if not anim_curves:
        print("There are no keys to move.")
        return 0
    if i == 0:
        return 0
    else:
        offset = -(start_frame)-1
        for curve in anim_curves:
            cmds.keyframe(curve, edit=True, relative=True, timeChange=offset)
        
        print(f"Keyframes moved to frame 0 (offset: {offset}).")
        return offset
        

# Output directory , checks if there is a folder in the sepcified path
output_dir = os.path.expanduser("~/Desktop/shots")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
#starts which shots we have with a list 
shots = cmds.ls(type='shot')
#if there is no shots in sequencer raises a runtime error
if not shots:
    print("Could not find shots in the sequencer")
    raise RuntimeError("Ther is no shots to process ! .") 

#enumerate to check the number of the shot
for i, toma in enumerate(shots):
    print(f"\n=== Processing shot: {toma} ===")

    shot_name = cmds.shot(toma, query=True, shotName=True) or toma
    print(shot_name)
    start_frame = cmds.shot(toma, query=True, sequenceStartTime=True)
    print(start_frame)
    end_frame = cmds.shot(toma, query=True, sequenceEndTime=True)
    print(end_frame)
    camara = cmds.shot(toma, query=True, currentCamera=True)
    print(camara)
    #enters to the shots that are not the first ones
    if i > 0:
        shot_anterior = shots[i - 1]
        start_ant = cmds.shot(shot_anterior, query=True, sequenceStartTime=True)
        print(start_ant)
        end_ant = cmds.shot(shot_anterior, query=True, sequenceEndTime=True)
        print(end_ant)
        anterior = (end_ant - start_ant)
        print(f"previous shot: {shot_anterior}")
        print(anterior)
        # its the first shots goes directly to else and checks that is the first shot
    else:
        anterior = 0
        print("Its the first shot, no previous shot")
    print(f"Shot: {shot_name} (frames {start_frame}-{end_frame}, cámara: {camara})")
    
    #enteres the def to move all keys in the scene
    offset = move_keys_to_zero(anterior, i)
    
    
    #moves the playbackoptions to the right frame
    framesFinal = (end_frame - start_frame) + 1
    start_playback = 1
    end_playback = start_playback + framesFinal - 1

    cmds.playbackOptions(minTime=start_playback, maxTime=end_playback)
    cmds.playbackOptions(animationStartTime=start_playback, animationEndTime=end_playback)
    cmds.currentTime(start_playback)
    print(f"Timeline configured: minTime={start_playback}, maxTime={end_playback}")
    
    # saves the scene with the shot name
    final_output = os.path.join(output_dir, f"{shot_name}.ma")
    cmds.file(rename=final_output)
    cmds.file(save=True, type="mayaAscii", force=True)
