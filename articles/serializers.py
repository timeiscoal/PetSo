from rest_framework import serializers
from articles.models import Article as ArticleModel
from articles.models import Category as CategoryModel
from articles.models import Comment as CommentModel


# 게시글 리스트
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = (
            "title",
            "pk",
            "author",
            "image",
        )
        
# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"


# 카테고리
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"


# 게시글
class ArticleSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True)
    #categorys = CategorySerializer(many=True)


    class Meta:
        model = ArticleModel
        fields = "__all__"