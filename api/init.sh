sudo chmod 777 /tmp/gradio

docker run --gpus all -t -d --cpus 1 --memory=12g --name wav2lip_01 -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data --mount source=API_DISK,target=/api_disk/ -v ./api/disk/checkpoints/facedetection/s3fd.pth:/home/Wav2Lip/face_detection/detection/s3fd.pth wav2lip
docker run --gpus all -t -d --cpus 8 --memory=4g --name swapper_face -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data --mount source=API_DISK,target=/api_disk/ -v ./api/disk/checkpoints/gfpgan/:/facefusion/gfpgan/weights/ facefusion 
# python run.py --execution-providers cpu -t /tmp/gradio/7c7bb468329d666f6c5e2b6e8d9c75c96b8a5e25/clip_10s.mp4 -s /tmp/gradio/1557989dce7bd0a4a743f4d5bca2bdc4c202a21b/image.png -o /home/data/result_voice.mp4 --headless --keep-fps --frame-processors face_swapper
docker run --gpus all -t -d --name enhancer_esr -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data --mount source=API_DISK,target=/api_disk/ -v ./api/disk/checkpoints/gfpgan/:/Real-ESRGAN/gfpgan/weights/ -v ./api/disk/checkpoints/real_esrgan/:/Real-ESRGAN/weights/ real-esrgan 
# docker run --gpus all -it --name api_lip_sync -v /tmp/gradio:/tmp/gradio -v ./ui/data:/home/data --mount source=API_DISK,target=/api_disk/ lip-sync

docker volume create --opt device=./api/disk/ --opt type=none --opt o=bind API_DISK