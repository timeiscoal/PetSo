from rest_framework import serializers
from .models import Inference as InferenceModel


class InferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InferenceModel
        fields = "__all__"