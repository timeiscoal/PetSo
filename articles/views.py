from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article as ArticleModel
from articles.models import Comment as CommentModel
from articles.serializers import ArticleSerializer


from django.shortcuts import render

class ArticleView():
    
    def get(self, request):
        articles = ArticleModel.objet.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




class CommentView(APIView):
    pass


class CommentDetailView(APIView):
    pass
