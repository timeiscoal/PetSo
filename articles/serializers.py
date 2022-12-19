from rest_framework import serializers
from articles.models import Article as ArticleModel
# from articles.models import Category as CategoryModel
from articles.models import Comment as CommentModel



# 게시글 리스트
class ArticleListSerializer(serializers.ModelSerializer):

    def get_bookmarks(self, obj):
        return obj.bookmarks.count()

    user = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.name
    
    def get_category_id(self, obj):
        return obj.id
    
    class Meta:
        model = ArticleModel
        fields = (
            "title",
            "pk",
            "user",
            "image",
            "category",
            "category_id",
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
    user = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()


    def get_user(self, obj):
        return obj.author.name

    def get_user_email(self,obj):
        return obj.author.email


    class Meta:
        model = CommentModel
        fields = ("content","user","author" ,"created_at","id","user_email")

# 댓글 생성
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"

# 카테고리
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryModel
#         fields = "__all__"


# 게시글
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.author.name

    def get_likes(self, obj):
        return obj.likes.count()

    def get_bookmarks(self, obj):
        return obj.bookmarks.count()    




    class Meta:
        model = ArticleModel
        fields = ("title",
                  "content",
                  "user",
                  "author",
                  "bookmarks",
                  "likes",
                  "created_at",
                  'image',
                  'category',
                  "id",
                  )