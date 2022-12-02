from django.contrib import admin
<<<<<<< HEAD
from articles.models import Article

admin.site.register(Article)
=======
from articles.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
>>>>>>> b431be902d792233a1ff69e02f04e08da51719ed
