from django.urls import path
from .views import HomePageView, DetailPageView, AddNewPost, UpdatePost, DeletePost

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", DetailPageView.as_view(), name="post_detail"),
    path("post/new/", AddNewPost.as_view(), name="post_new"),
    path("post/update/<int:pk>/", UpdatePost.as_view(), name="post_update"),
    path("post/delete/<int:pk>", DeletePost.as_view(), name="delete_post"),
]
