# virtual_mc

# Yêu cầu
- python>=3.11

# Chuẩn bị môi trường
```pip install -r requirements.txt```
```python install.py```

# Hướng dẫn
## Bước 1: Khởi động WebUI
(from /visual_mc)  
```cd ./ui```  
```gradio main.sh```  

## Bước 2: Khởi động API
(from /visual_mc)  
```docker-compose -f ./api/docker-compose.yml up```  