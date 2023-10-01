#wav2lip
sudo chmod 777 /tmp/gradio
docker run --gpus all -t -d --cpus 1 --memory=6g --name wav2lip_01 -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data wav2lip_rudrabha
docker run --gpus all -t -d --cpus 8 --memory=4g --name swapper_face -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data facefusion
docker run --gpus all -t -d --name enhancer_esr -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data real-esrgan
#docker run -it --rm -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data bgremover:latest 

#bash run.sh /home/data/source.mp4 /home/data/example/extras/swap/target.jpg /home/data  "face_enhancer frame_enhancer"
#bash run.sh RealESRGAN_x4plus /home/data/source.png /home/data/result_enhancer 2