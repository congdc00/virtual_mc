# virtual_mc

# Yêu cầu
- GPU: Nvidia

# Environment
- python >= 3.11


# Chuẩn bị dữ liệu (example)

# Chuẩn bị môi trường
```pip install -r requirements.txt```  
```python install.py```

* Lưu ý: Nếu chạy install bị lỗi, hãy thử  ```docker logout``` và chạy lại 

# Hướng dẫn
## Bước 1: Khởi động WebUI
(from /visual_mc)  
```cd ./ui```  
```gradio main.sh```  

## Bước 2: Khởi động API
(from /visual_mc)  
```docker-compose -f ./api/docker-compose.yml up```  
