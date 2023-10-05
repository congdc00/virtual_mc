
from loguru import logger
import os
import shutil
import glob
from rembg import remove
import subprocess
from PIL import Image
import time
import tqdm 
def remove_bg(type, video_path, target_path=""):
    # output_path = "/home/data/result_rmbg.mp4"
    
    # if type=="Transparent":
    #     command = f"backgroundremover -i {video_path} -tv -o {output_path}"
    # elif type=="Video":
    #     command = f"backgroundremover -i {video_path} -tov {target_path} -o {output_path}"
    # logger.info(f"Run RMBG {command}")
    # os.system(command)

    # return "./data/result_rmbg.mp4"
    if os.path.exists("./data/video_none_bg.mp4"):
        os.remove("./data/video_none_bg.mp4") 

    folder_path = "./data/frame_split"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path) 
    os.makedirs(folder_path)

    if os.path.exists("./data/frame_none_bg/"):
        shutil.rmtree("./data/frame_none_bg/") 
    os.makedirs("./data/frame_none_bg/")

    logger.info(f"Split Image")
    os.system(f"ffmpeg -i {video_path} -r 30/1 ./data/frame_split/%03d.png")
    logger.info(f"Remove Background")
    files = glob.glob(f"{folder_path}/*.png")
    for file in files:
        input = Image.open(file)
        output = remove(input)
        new_path = file.replace(folder_path, "./data/frame_none_bg/")
        output.save(new_path)
    
    logger.info(f"Merge frames")
    os.system(f"ffmpeg -framerate 30 -pattern_type glob -i './data/frame_none_bg/*.png' -c:v libx264 -pix_fmt yuv420p ./data/video_none_bg.mp4")
    return "./data/video_none_bg.mp4"