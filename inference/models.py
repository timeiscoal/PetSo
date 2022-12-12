from django.db import models
from django_base64field.fields import Base64Field




class Inference(models.Model):
    # 추론 모델 (base64 인코딩)
    output_img = Base64Field(max_length=900000, blank=True, null=True)