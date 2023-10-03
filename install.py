# export virtual_mc_path=$PWD
import os 
from loguru import logger
from huggingface_hub import hf_hub_download
import tqdm
API_DISK_PATH = "./api/disk"
CHECKPOINT_PATH = f"{API_DISK_PATH}/checkpoints"
LIST_MODEL = ["facedetection", "gfpgan", "real_esrgan", "wav2lip"]

def make_direction(path):
    if not os.path.exists(path):
        os.system(f"mkdir {path}")
        return True
    else:
        return False

def download_model(list_model):
    for model in list_model:
        if model=="facedetection":
            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/face-detection",filename="s3fd.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/facedetection/")
        elif model=="gfpgan":
            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/gfp-gan",filename="detection_Resnet50_Final.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/gfpgan/")

            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/gfp-gan",filename="parsing_parsenet.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/gfpgan/")
        elif model=="real_esrgan":
            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/real_esrgan",filename="RealESRGAN_x4plus.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/real_esrgan/")
        elif model=="wav2lip":
            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/wav2lip",filename="lipsync_expert.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/wav2lip/")

            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/wav2lip",filename="visual_quality_disc.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/wav2lip/")
            
            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/wav2lip",filename="wav2lip_gan.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/wav2lip/")

            downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/wav2lip",filename="wav2lip.pth")
            os.system(f"mv {downloaded_model_path} {CHECKPOINT_PATH}/wav2lip/")

if __name__=="__main__":

    
    logger.info("Prepare model")
    done = make_direction(API_DISK_PATH)
    if done:
        make_direction(CHECKPOINT_PATH)
        download_model(LIST_MODEL)
    
        logger.info("Build Image")
        os.system(f"bash ./api/build.sh")

        logger.info("Build Environment")
        os.system(f"pip install -r requirements.txt")
        os.system(f"sudo chmod 777 /tmp/gradio")
    else:
        logger.warning("You have run the program before.")