import os

def process(checkpoint, video_path, audio_path):
    command = f"docker exec wav2lip_01 bash run.sh {checkpoint} {video_path} {audio_path}"
    os.system(command)
    return video_path