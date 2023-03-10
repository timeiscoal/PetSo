from django.contrib import admin
from .models import Article ,Category

# Register your models here.
from articles.models import Article
from articles.models import Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display= ("title","content","created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
