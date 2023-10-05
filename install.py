# export virtual_mc_path=$PWD
import os 
from loguru import logger
from huggingface_hub import hf_hub_download
import tqdm
API_DISK_PATH = f"{os.getcwd()}/api/disk"
CHECKPOINT_PATH = f"{API_DISK_PATH}/checkpoints"
LIST_MODEL = ["facefusion","facedetection", "gfpgan", "real_esrgan", "wav2lip"] #"lipsync"

DATA_PATH = f"{os.getcwd()}/ui/data"
def make_direction(path):
    if not os.path.exists(path):
        os.system(f"mkdir {path}")
        return True
    else:
        return False
def update_model(model, filename):
    dst_path = f"{CHECKPOINT_PATH}/{model}"
    model_path = f"{dst_path}/{filename}"
    if os.path.exists(model_path):
        logger.success(f"{filename} OK!") 
    else:
        file_path =f"{CHECKPOINT_PATH}/{model}"
        hf_hub_download(repo_id=f"Cong-HGMedia/{model}", local_dir=file_path, filename=filename, local_dir_use_symlinks=False)
        logger.info(f"Add {filename}") 

def download_model(list_model):
    for model in list_model:
        if not os.path.exists(f"{CHECKPOINT_PATH}/{model}"):
            os.mkdir(f"{CHECKPOINT_PATH}/{model}")
        if model=="facedetection":
            update_model(model, "s3fd.pth")
        elif model=="facefusion":
            update_model(model, "open_nsfw_weights.h5")
        elif model=="gfpgan":
            update_model(model, "detection_Resnet50_Final.pth")
            update_model(model, "parsing_parsenet.pth")
        elif model=="real_esrgan":
            update_model(model, "RealESRGAN_x4plus.pth")
        elif model=="wav2lip":
            update_model(model, "lipsync_expert.pth")
            update_model(model, "visual_quality_disc.pth")
            update_model(model, "wav2lip_gan.pth")
            update_model(model, "wav2lip.pth")
        elif model=="lipsync":
            os.mkdir(f"{CHECKPOINT_PATH}/lipsync")
            os.system(f"gdown --id 1lW4mf5YNtS4MAD7ZkAauDDWp2N3_Qzs7 -O {CHECKPOINT_PATH}/lipsync/checkpoints.tar.gz")

if __name__=="__main__":

    os.system(f"sudo chmod 777 /tmp/gradio")
    
    logger.info("Prepare model")
    make_direction(API_DISK_PATH)
    make_direction(CHECKPOINT_PATH)
    download_model(LIST_MODEL)

    logger.info("Prepare data")
    make_direction(DATA_PATH)
    make_direction(F"{DATA_PATH}/frame_enhancer")
    make_direction(F"{DATA_PATH}/frame_none_bg")
    make_direction(F"{DATA_PATH}/frame_split")
    make_direction(F"{DATA_PATH}/new_images")
    make_direction(F"{DATA_PATH}/result_enhancer")

    logger.info("Build Image")
    os.system(f"bash ./api/build.sh")

    