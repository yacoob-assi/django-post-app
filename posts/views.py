from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class DetailPageView(DetailView):
    model = Post
    template_name = "postDetail.html"
