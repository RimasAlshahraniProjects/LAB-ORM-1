from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from posts.models import Post 

def home_view(request: HttpRequest):
    posts = Post.objects.all() 
    return render(request, "main/home.html", {"posts": posts})