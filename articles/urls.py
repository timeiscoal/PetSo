from django.urls import path, include
from articles import views

urlpatterns = [
    path("bookmark/<int:article_id>/", views.BookmarkView.as_view(), name="bookmark_view"),
    path("mybookmark/", views.MybookmarkView.as_view(), name="my_bookmark_view"),
]
