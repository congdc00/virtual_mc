docker build -t wav2lip -f ./api/dockerfile/Dockerfile.wav2lip .
docker build -t facefusion -f ./api/dockerfile/Dockerfile.facefusion .
docker build -t real-esrgan -f ./api/dockerfile/Dockerfile.real-esrgan .

# volume
docker volume create --opt device=./api/disk/ --opt type=none --opt o=bind API_DISK