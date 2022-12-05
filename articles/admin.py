from django.contrib import admin
from articles.models import Article
from articles.models import Comment




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
