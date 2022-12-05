from django.contrib import admin
from articles.models import Article
from articles.models import Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display= ("title","content","created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

