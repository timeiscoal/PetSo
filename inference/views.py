from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Inference as InferenceModel
from .serializers import InferenceSerializer
from .utils import inference

class InferenceView(APIView):
    def get(self, request):
        inference = InferenceModel.objects.latest("id")
        serializer = InferenceSerializer(inference)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        output_img = inference(input_img=request.FILES["input_img"].read())
        
        data = {"output_img": output_img}
        serializer = InferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)