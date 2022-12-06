
from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticlelistView.as_view(), name='article_list_view'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='like_view'),
    path('comment/', views.CommentView.as_view() , name="commentview"),
    path("comment/<int:comment_id/", views.CommentDetailView.as_view(), name="commentdetailview")
    
]

