from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article as ArticleModel
from articles.models import Comment as CommentModel
from articles.serializers import ArticleSerializer
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from articles.models import Article


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


# 북마크 등록/취소
class BookmarkView(APIView):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.bookmarks.all():
            article.bookmarks.remove(request.user)
            return Response({"message":"북마크 취소 완료!"}, status=status.HTTP_200_OK)
        else:
            article.bookmarks.add(request.user)
            return Response({"message":"북마크 등록 완료!"}, status=status.HTTP_200_OK)

# 나의 북마크 리스트
class MybookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        bookmarks = user.article_bookmarks.all()
        serializer = ArticleSerializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)