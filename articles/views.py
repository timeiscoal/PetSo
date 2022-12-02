from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article as ArticleModel
from articles.models import Comment as CommentModel
from articles.serializers import ArticleSerializer,ArticleListSerializer


from django.shortcuts import render

class ArticleView(APIView):
    def get(self, request, article_id):
        articles = ArticleModel.objet.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, article_id):
        pass 
    
    def delete(self, request, article_id):
        pass
     

class ArticlelistView(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass
    
         
    


class LikeView(APIView):
    def post(self,request):
        pass