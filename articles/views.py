from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article as ArticleModel
from articles.models import Comment as CommentModel

from articles.serializers import ArticleSerializer
from rest_framework import status, permissions
from articles.models import Article
from articles.models import Category
from django.db.models import Q
from rest_framework.exceptions import NotAuthenticated, ParseError, PermissionDenied

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import transaction

# from restframework_simplejwt.tokens import AccessToken

from articles.serializers import ArticleSerializer,ArticleCreateSerializer,ArticleListSerializer ,CommentSerializer, CommentCreateSerializer
from user.serializers import UserSerializer



from django.shortcuts import render

# 디테일페이지 아티클 유저뷰
class ArticleUserView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        user = article.author
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 게시글 상세페이지_수정,삭제
class ArticleView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, article_id):

            article = ArticleModel.objects.get(id=article_id)
            if request.user==article.author:
                serializer = ArticleCreateSerializer(article, data=request.data , partial=True)

                if serializer.is_valid():
                    category_name = request.data.get("category")
                    if not category_name:
                        raise ParseError("카테고리를 선택해주세요.")
                    try:
                        with transaction.atomic():
                                category = Category.objects.get(name=category_name)
                                create_article = serializer.save(author_id=request.user.id,category=category)
                                serializer = ArticleCreateSerializer(create_article)
                                return Response(serializer.data, status=status.HTTP_200_OK)
                    except Exception:
                        raise ParseError("카테고리를 찾을 수 없습니다.") 
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("잘못된 접근입니다", status=status.HTTP_403_FORBIDDEN)
        

    def delete(self, request, article_id):
        article = get_object_or_404(ArticleModel, id=article_id)
        if request.user==article.author:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("잘못된 접근입니다", status=status.HTTP_403_FORBIDDEN)
            


# 게시글 조회, 생성
class ArticlelistView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
            serializer = ArticleCreateSerializer(data=request.data)
            if serializer.is_valid():
                category_name = request.data.get("category")
                if not category_name:
                    raise ParseError("카테고리를 선택해주세요.")
                try:
                    with transaction.atomic():
                            category = Category.objects.get(name=category_name)
                            create_article = serializer.save(author_id=request.user.id,category=category)
                            serializer = ArticleCreateSerializer(create_article)
                            return Response(serializer.data, status=status.HTTP_201_CREATED)

                except Exception:
                    raise ParseError("카테고리를 찾을 수 없습니다.")        
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
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
    
         
class LikeView(APIView):
    def post(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)

# 댓글
class CommentView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializers = CommentSerializer(comments, many=True)
        
        return Response(serializers.data , status=status.HTTP_200_OK)

    def post(self, request , article_id):
        datas = request.data
        datas.update({"author":request.user.id})
        serializer = CommentCreateSerializer(data=datas)


        if serializer.is_valid():
            create_comment=serializer.save()
            print(create_comment)
            serializer = CommentCreateSerializer(create_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, article_id ,id):
        aritcle = ArticleModel.objects.get(id=article_id)
        comment = aritcle.comment_set.get(id=id)
        serialzier = CommentSerializer(comment)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def put(self, request, article_id ,id):
        comment = CommentModel.objects.get(pk=id)
        datas = request.data
        datas.update({"author":request.user.id})

        if request.user == comment.author:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                update_comment = serializer.save()
                serializer = CommentCreateSerializer(update_comment)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한 없음",status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id ,id):
        comment = CommentModel.objects.get(pk=id)
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("권한 없음", status=status.HTTP_403_FORBIDDEN)        




# 나의 아티클 리스트
class MyarticleView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        articles = user.article_set.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 카테고리

class CategoryView(APIView):

    def get(self ,request, category_name):
        categories = Category.objects.get(name=category_name)
        articles = ArticleModel.objects.filter(Q(category__id__contains=categories.pk))

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

