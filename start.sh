sudo chmod 777 /tmp/gradio
docker run --gpus all -t -d --cpus 1 --memory=12g --name wav2lip_01 -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data wav2lip_rudrabha
docker run --gpus all -t -d --cpus 8 --memory=4g --name swapper_face -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data facefusion
docker run --gpus all -t -d --name enhancer_esr -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data real-esrgan