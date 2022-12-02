from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article as ArticleModel
from articles.models import Comment as CommentModel

from articles.serializers import ArticleSerializer,ArticleListSerializer ,CommentSerializer, CommentCreateSerializer



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


class CommentView(APIView):

    def get(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializers = CommentSerializer(comments, many=True)
        
        return Response(serializers.data , status=status.HTTP_200_OK)

    def post(self, request , article_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            create_comment=serializer.save(user=request.user, article_id=article_id)
            serializer = CommentCreateSerializer(create_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    
    def get(self, request, article_id ,comment_id):
        aritcle = ArticleModel.objects.get(id=article_id)
        comment = aritcle.comment_set.get(comment_id=comment_id)
        serialzier = CommentSerializer(comment)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def put(self, request, article_id ,comment_id):
        comment = CommentModel.objects.get(pk=comment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                update_comment = serializer.save()
                serializer = CommentCreateSerializer(update_comment)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한 없음",status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id ,comment_id):
        comment = CommentModel.objects.get(pk=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("권한 없음", status=status.HTTP_403_FORBIDDEN)        


