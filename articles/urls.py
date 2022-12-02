from django.urls import path, include
from articles import views

urlpatterns = [

    path('', views.ArticleView, ),
    path('comment/', views.CommentView.as_view() , name="commentview"),
    path("comment/<int:comment_id/", views.CommentDetailView.as_view(), name="commentdetailview")

]

