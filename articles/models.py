from django.db import models


class Article(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=" ", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    articles = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    articles = models.ForeignKey("articles.Article", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField("카테고리", max_length=150)

    def __str__(self) -> str:
        return self.category