import os
import docker
from loguru import logger
import shutil

client = docker.from_env()
def swap(list_choice, video_path, image_path, audio_path, enhancer):
    result_path = ""
    if "Face" in list_choice:
        container = client.containers.get('swapper_face')
        output = "/home/data/result_voice.mp4"
        command = f"bash run.sh {video_path} {image_path} {output} face_swapper"

        logger.info(f"Running Swap face {command}") 
        container.exec_run(command)
        logger.success("Process done!")
        result_path ="./data/result_voice.mp4"

    if "Lip" in list_choice:
        if os.path.exists("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4"):
            os.remove("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4")
        
        container = client.containers.get('wav2lip_01')
        if result_path=="":
            video_input = video_path
        else:
            video_input = result_path.replace("./data", "/home/data")
        command = f'bash run.sh wav2lip {video_input} {audio_path}'
        logger.info(f"Running Swap lip {command}") 
        container.exec_run(command)
        logger.success("Process done!")
        result_path ="./data/result_voice.mp4"

    if enhancer==True:
        container = client.containers.get('swapper_face')
        input_video = "/home/data/result_voice.mp4"
        output = "/home/data/result_voice.mov"
        command = f"bash run.sh {input_video} {image_path} {output} 'frame_enhancer face_enhancer'"

        logger.info(f"Running Enhancer {command}") 
        container.exec_run(command)
        logger.success("Process done!")
        result_path ="./data/result_voice.mov"

    return result_path