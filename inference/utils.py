import io
import torch
from PIL import Image
import base64
import numpy as np
import cv2

def inference(input_img):
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models_train/best.pt', force_reload=True)  # 커스텀 학습 모델 사용
    npimg = np.fromstring(input_img, np.uint8)
    decode_img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(decode_img, cv2.COLOR_BGR2RGB)
    
    img = cv2.resize(img, (640, 640))
    
    results = model(img, size=640)  # inference 추론

    results.ims  # array of original images (as np array) passed to model for inference
    results.render()  # updates results.imgs with boxes and labels
    for img in results.ims:  # 'JpegImageFile' -> bytes-like object
        buffered = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(buffered, format="JPEG")
        encoded_img_data = base64.b64encode(buffered.getvalue()).decode(
            'utf-8')  # base64 encoded image with results
        
    return encoded_img_data
            
