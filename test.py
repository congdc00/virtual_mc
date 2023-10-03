from huggingface_hub import hf_hub_download
import os
downloaded_model_path = hf_hub_download(repo_id="Cong-HGMedia/face-detection",filename="s3fd.pth")
os.system(f"mv {downloaded_model_path} ./")
print(downloaded_model_path)