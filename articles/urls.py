<<<<<<< HEAD
from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticlelistView.as_view(), name='article_list_view'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='article_view'),
    path('like/', views.LikeView.as_view(), name='like_view'),
    
]
=======
from django.urls import path, include
from articles import views

urlpatterns = [

    path('', views.ArticleView, ),
    path('comment/', views.CommentView.as_view() , name="commentview"),
    path("comment/<int:comment_id/", views.CommentDetailView.as_view(), name="commentdetailview")

]

>>>>>>> b431be902d792233a1ff69e02f04e08da51719ed
