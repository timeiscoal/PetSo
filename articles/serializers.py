from rest_framework import serializers
from articles.models import Article as ArticleModel
from articles.models import Category as CategoryModel
from articles.models import Comment as CommentModel



# 게시글 리스트
class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.name
    
    class Meta:
        model = ArticleModel
        fields = (
            "title",
            "pk",
            "user",
            "image",
        )

# 게시글 생성
class ArticleCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArticleModel
        fields = (
            "title",
            "image",
            "content",
        )        
        
        
# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"

# 댓글 생성
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ("content",)


# 카테고리
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


# 게시글
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.name
    #comments = CommentSerializer(many=True)
    #categorys = CategorySerializer(many=True)


    class Meta:
        model = ArticleModel
        fields = ("title",
                  "content",
                  "user",
                  )