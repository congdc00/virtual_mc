#wav2lip
sudo chmod 777 /tmp/gradio
docker run --gpus all -t -d --cpus 1 --memory=4g --name wav2lip_01 -v /tmp/gradio:/tmp/gradio -v /home/hgmedia/Project/virtual_mc/data:/home/data wav2lip_rudrabha