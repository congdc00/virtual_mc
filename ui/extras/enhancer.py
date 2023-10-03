from loguru import logger
import os
import shutil
import glob
from rembg import remove
import subprocess
from PIL import Image
import time
import docker
client = docker.from_env()
def enhancer(video_path, scale):

    folder_path = "./data/frame_split"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path) 
    os.makedirs(folder_path)

    logger.info(f"Split Image")
    os.system(f"ffmpeg -i {video_path} -r 30/1 ./data/frame_split/%03d.png")

    logger.info(f"Enhancer")
    output_path="./data/frame_enhancer/"
    if os.path.exists("./data/frame_enhancer/"):
        shutil.rmtree("./data/frame_enhancer/") 
    os.makedirs("./data/frame_enhancer/")
    files = glob.glob(f"{folder_path}/*.png")
    container = client.containers.get('enhancer_esr')
    for image_path in files:
        input_path = image_path.replace("./data", "/home/data")
        command = f"bash run.sh RealESRGAN_x4plus {input_path} /home/data/frame_enhancer {scale}"
        print(command)
        container.exec_run(command)
    
    logger.info(f"Merge frame")
    if os.path.exists("./data/video_enhancer.mp4"):
        shutil.rmtree("./data/video_enhancer.mp4")
    os.system(f"ffmpeg -framerate 30 -pattern_type glob -i '{output_path}/*.png' -c:v libx264 -pix_fmt yuv420p ./data/video_enhancer.mp4")
    return "./data/video_enhancer.mp4"