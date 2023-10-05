docker build -t wav2lip -f ./api/dockerfile/Dockerfile.wav2lip . 
docker build -t facefusion -f ./api/dockerfile/Dockerfile.facefusion .
docker build -t real-esrgan -f ./api/dockerfile/Dockerfile.real-esrgan .
docker build -t lipsync -f ./api/dockerfile/Dockerfile.lipsync .