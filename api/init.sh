sudo chmod 777 /tmp/gradio

# volume


docker run --gpus all -t -d --cpus 1 --memory=12g --name wav2lip_01 -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data -v API_DISK:/api_disk/ -v ./api/disk/checkpoints/facedetection/s3fd.pth:/home/Wav2Lip/face_detection/detection/s3fd.pth wav2lip_rudrabha
docker run --gpus all -t -d --cpus 8 --memory=4g --name swapper_face -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data -v API_DISK:/api_disk/ facefusion 
docker run --gpus all -t -d --name enhancer_esr -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data -v API_DISK:/api_disk/ real-esrgan 