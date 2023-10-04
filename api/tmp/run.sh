cd facefusion
python3.10 run.py --execution-providers cpu cuda -t $1 -s $2 -o $3 --headless --keep-fps --frame-processors $4
