from django.db import models
from user.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="%Y", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookmarks = models.ManyToManyField(User, related_name="article_bookmarks")
    likes = models.ManyToManyField(User, related_name="like_articles")
    category = models.ForeignKey("articles.Category", on_delete=models.SET_NULL, null=True)

    


class Comment(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    articles = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

