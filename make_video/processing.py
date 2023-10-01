import os
import docker
from loguru import logger
import shutil

client = docker.from_env()

def wav2lip(checkpoint, video_path, audio_path, smooth=True, config=False, x_top=0, y_top=0, x_bot=0, y_bot=0, face_enhancer=True, frame_enhancer=True):
    

    
    if os.path.exists("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4"):
        os.remove("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4")
    
    container = client.containers.get('wav2lip_01')
    command = f'bash run.sh {checkpoint.lower()} {video_path} {audio_path}'
    #Add params
    if not smooth:
        command+=" --nosmooth"
    if config:
        command+=f" --pads {x_top} {y_top} {x_bot} {y_bot}"
    logger.info(f"Running Wav2Lip {command}") 
    container.exec_run(command)
    logger.success("Process done!")
    result_path ="./data/result_voice.mp4"

    # Enhancer
    command_add =""
    if face_enhancer==True:
        command_add+="face_enhancer"
    if frame_enhancer==True:
        if command_add=="":
            command_add+="frame_enhancer"
        else:
            command_add+=" frame_enhancer"
    if command_add!="":
        container = client.containers.get('swapper_face')
        input_video = "/home/data/result_voice.mp4"
        target="/home/data/example/extras/swap/target.jpg"
        output = "/home/data/result_facefusion.mp4"
        command = f"bash run.sh {input_video} {target} {output} '{command_add}'"
        logger.info(f"Running Enhancer {command}") 
        container.exec_run(command)
        logger.success("Process done!")
        result_path ="./data/result_facefusion.mp4"
    
    #Merge video with audio
    os.system(f"ffmpeg -i {result_path} -i {audio_path} -c:v copy -c:a aac ./data/output.mp4")

    return "./data/output.mp4"

def enhancer():
    pass