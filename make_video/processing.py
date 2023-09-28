import os
import docker
from loguru import logger
import shutil

client = docker.from_env()

def process(checkpoint, video_path, audio_path):
    if os.path.exists("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4"):
        os.remove("/home/hgmedia/Project/virtual_mc/data/result_voice.mp4")
    
    container = client.containers.get('wav2lip_01')
    command = f'bash run.sh {checkpoint.lower()} {video_path} {audio_path}'
    logger.info(f"Running Wav2Lip") 
    container.exec_run(command)
    logger.success("Process done!")
    result_path ="./data/result_voice.mp4"
    return result_path
