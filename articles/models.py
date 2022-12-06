from django.db import models
from user.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(User, related_name="like_articles")
    def __str__(self):
        return f" 게시글 : {self.title} 좋아요 : {self.likes.count()}개"


class Comment(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    articles = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.content[:15]}..."


class Category(models.Model):
    articles = models.ForeignKey("articles.Article", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField("카테고리", max_length=150)

    def __str__(self) -> str:
        return self.category