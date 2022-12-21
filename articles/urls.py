
from django.urls import path, include
from articles import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.ArticleViewSet)

urlpatterns = [
    path("viewset/", include(router.urls)),
    path("bookmark/<int:article_id>/", views.BookmarkView.as_view(), name="bookmark_view"),
    path("mybookmark/", views.MybookmarkView.as_view(), name="my_bookmark_view"),
    path('', views.ArticlelistView.as_view(), name='article_list_view'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='like_view'),
    path('<int:article_id>/comment/', views.CommentView.as_view() , name="commentview"),
    path("<int:article_id>/comment/<int:id>/", views.CommentDetailView.as_view(), name="commentdetailview"),
    path("myarticle/", views.MyarticleView.as_view(), name="my_article_view"),
    path("<int:article_id>/user/", views.ArticleUserView.as_view(), name="article_user_view"),
    path("user/<int:user_id>/", views.UserArticleView.as_view(), name="user_article_view"),
    path("<category_name>/", views.CategoryView.as_view(), name="categoryview")
    
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

