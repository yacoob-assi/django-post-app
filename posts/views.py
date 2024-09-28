from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class DetailPageView(DetailView):
    model = Post
    template_name = "postDetail.html"


class AddNewPost(CreateView):
    model = Post
    template_name = "newPost.html"
    fields = ["title", "auther", "body"]


class UpdatePost(UpdateView):
    model = Post
    template_name = "updatePost.html"
    fields = ["title", "body"]


class DeletePost(DeleteView):
    model = Post
    template_name = "deletePost.html"
    success_url = reverse_lazy("home")
